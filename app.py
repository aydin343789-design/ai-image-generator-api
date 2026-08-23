from flask import Flask, request, jsonify, send_file
from diffusers import StableDiffusionPipeline
import torch
from PIL import Image
import io
import os
from datetime import datetime
import logging

app = Flask(__name__)

# تنظیمات
UPLOAD_FOLDER = 'generated_images'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# لاگ
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# بارگذاری مدل
print("🔄 بارگذاری مدل... این کار ممکن است ۵ دقیقه طول بکشد...")
try:
    device = "cuda" if torch.cuda.is_available() else "cpu"
    print(f"استفاده از: {device}")
    
    pipe = StableDiffusionPipeline.from_pretrained(
        "runwayml/stable-diffusion-v1-5",
        torch_dtype=torch.float16 if device == "cuda" else torch.float32,
        safety_checker=None
    )
    pipe = pipe.to(device)
    print("✅ مدل بارگذاری شد!")
except Exception as e:
    print(f"❌ خطا در بارگذاری مدل: {e}")
    pipe = None

@app.route('/health', methods=['GET'])
def health():
    """بررسی وضعیت سرور"""
    return jsonify({
        "status": "alive",
        "device": "cuda" if torch.cuda.is_available() else "cpu",
        "model_loaded": pipe is not None
    })

@app.route('/api/generate', methods=['POST'])
def generate_image():
    """
    API برای تولید تصویر
    
    ورودی JSON:
    {
        "prompt": "توصیف تصویر",
        "steps": 50,
        "guidance_scale": 7.5,
        "height": 512,
        "width": 512
    }
    """
    try:
        data = request.get_json()
        
        # بررسی ورودی
        if not data or 'prompt' not in data:
            return jsonify({"error": "خطا: prompt الزامی است"}), 400
        
        prompt = data.get('prompt')
        steps = data.get('steps', 50)
        guidance_scale = data.get('guidance_scale', 7.5)
        height = data.get('height', 512)
        width = data.get('width', 512)
        
        if not pipe:
            return jsonify({"error": "مدل هنوز بارگذاری نشده است"}), 503
        
        logger.info(f"🎨 تولید تصویر برای: {prompt}")
        
        # تولید تصویر
        with torch.no_grad():
            image = pipe(
                prompt=prompt,
                num_inference_steps=steps,
                guidance_scale=guidance_scale,
                height=height,
                width=width
            ).images[0]
        
        # ذخیره تصویر
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"image_{timestamp}.png"
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        image.save(filepath)
        
        logger.info(f"✅ تصویر ذخیره شد: {filename}")
        
        return jsonify({
            "status": "success",
            "message": "تصویر با موفقیت تولید شد",
            "image_url": f"/api/image/{filename}",
            "filename": filename,
            "prompt": prompt
        }), 200
        
    except Exception as e:
        logger.error(f"❌ خطا: {str(e)}")
        return jsonify({"error": str(e)}), 500

@app.route('/api/image/<filename>', methods=['GET'])
def get_image(filename):
    """دانلود تصویر"""
    try:
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        if os.path.exists(filepath):
            return send_file(filepath, mimetype='image/png')
        else:
            return jsonify({"error": "تصویر پیدا نشد"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/images', methods=['GET'])
def list_images():
    """لیست تمام تصاویر تولید شده"""
    try:
        images = os.listdir(app.config['UPLOAD_FOLDER'])
        images = sorted(images, reverse=True)
        return jsonify({
            "status": "success",
            "count": len(images),
            "images": [f"/api/image/{img}" for img in images]
        }), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/', methods=['GET'])
def index():
    """صفحه اصلی - فایل HTML"""
    return send_file('index.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)