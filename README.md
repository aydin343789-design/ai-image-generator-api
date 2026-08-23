# 🎨 تصویر‌ساز هوش مصنوعی (AI Image Generator API)

یک پروژه آفلاین برای تولید تصاویر هنری با هوش مصنوعی using **Stable Diffusion**

## ✨ ویژگی‌ها

- ✅ **API کامل** برای تولید تصاویر
- ✅ **رابط وب جذاب** برای استفاده از گوشی و کامپیوتر
- ✅ **پشتیبانی GPU** (CUDA/ROCm)
- ✅ **ذخیره‌سازی خودکار** تمام تصاویر
- ✅ **تاریخچه تصاویر** برای مشاهده سریع
- ✅ **واسط فارسی** کامل

---

## 🚀 شروع سریع

### ۱. نصب Python

اگر Python نصب ندارید، از [python.org](https://www.python.org/downloads/) دانلود کنید (Python 3.10 یا بالاتر)

### ۲. کلون کردن پروژه

```bash
git clone https://github.com/aydin343789-design/ai-image-generator-api.git
cd ai-image-generator-api
```

### ۳. ایجاد محیط مجازی (اختیاری اما توصیه‌شده)

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### ۴. نصب وابستگی‌ها

```bash
pip install -r requirements.txt
```

**⚠️ این مرحله ۲۰-۳۰ دقیقه طول می‌کشد!**

### ۵. اجرای برنامه

```bash
python app.py
```

سپس مرورگر خود را باز کنید و برو به:
```
http://localhost:5000
```

---

## 📱 استفاده از گوشی

اگر می‌خواهی از گوشی استفاده کنی:

1. دستگاه‌ها باید در **شبکه یکسانی** باشند (WiFi یکسان)
2. IP آدرس کامپیوتر را پیدا کن:
   - **Windows**: `ipconfig` را اجرا کن و IPv4 Address را پیدا کن
   - **macOS/Linux**: `ifconfig` را اجرا کن

3. در گوشی، برو به:
   ```
   http://<YOUR_COMPUTER_IP>:5000
   ```

---

## 🔌 استفاده از API

### مثال: تولید تصویر با cURL

```bash
curl -X POST http://localhost:5000/api/generate \
  -H "Content-Type: application/json" \
  -d '{
    "prompt": "یک گربه قهوه‌ای روی صندلی آبی",
    "steps": 50,
    "guidance_scale": 7.5,
    "height": 512,
    "width": 512
  }'
```

### مثال: استفاده از Python

```python
import requests
import json

url = "http://localhost:5000/api/generate"
data = {
    "prompt": "یک منظره زیبای کوهستانی در غروب",
    "steps": 50,
    "guidance_scale": 7.5
}

response = requests.post(url, json=data)
result = response.json()

print(result)
# {'status': 'success', 'image_url': '/api/image/image_20240101_120000.png', ...}
```

### مثال: استفاده از JavaScript

```javascript
fetch('/api/generate', {
    method: 'POST',
    headers: {
        'Content-Type': 'application/json'
    },
    body: JSON.stringify({
        prompt: "یک پرنده قرمز در درخت سیب",
        steps: 50,
        guidance_scale: 7.5
    })
})
.then(res => res.json())
.then(data => {
    console.log(data.image_url);
    // دانلود یا نمایش تصویر
});
```

---

## 📡 Endpoints API

| متد | مسیر | توضیح |
|-----|------|-------|
| GET | `/health` | بررسی وضعیت سرور |
| POST | `/api/generate` | تولید تصویر جدید |
| GET | `/api/image/<filename>` | دانلود تصویر |
| GET | `/api/images` | لیست تمام تصاویر |

---

## ⚙️ پارامترهای API

### POST /api/generate

```json
{
  "prompt": "توصیف تصویر (الزامی)",
  "steps": 50,              // مراحل: 20-100 (بیشتر = بهتر اما کندتر)
  "guidance_scale": 7.5,    // کیفیت: 1-20 (بیشتر = نزدیک‌تر به prompt)
  "height": 512,            // ارتفاع: 512 یا 768
  "width": 512              // عرض: 512 یا 768
}
```

---

## 🌐 استقرار آنلاین (Deployment)

### گزینه ۱: Hugging Face Spaces (رایگان و سریع)

1. به [huggingface.co](https://huggingface.co) برو
2. Create → New Space
3. انتخاب Docker اور Flask
4. فایل‌های پروژه را آپلود کن
5. تمام شد! ✅

### گزینه ۲: Render.com

1. ثبت‌نام در [render.com](https://render.com)
2. Create → New Web Service
3. اتصال repository GitHub
4. `python app.py` را به عنوان start command وارد کن

### گزینه ۳: Railway.app

1. ثبت‌نام در [railway.app](https://railway.app)
2. اتصال GitHub repo
3. Deploy کن!

---

## 🖥️ نیاز‌های سیستمی

### حداقل:
- **RAM**: ۸ GB
- **Disk**: ۲۰ GB (برای مدل و تصاویر)
- **Python**: ۳.۱۰+

### بهتر است:
- **GPU**: NVIDIA (CUDA) یا AMD (ROCm)
- **RAM**: ۱۶ GB
- **Disk**: ۵۰ GB

---

## 🐛 حل مشکلات رایج

### ❌ خطا: "CUDA out of memory"

```bash
# استفاده از CPU (کندتر اما دقیق‌تر)
# app.py میں این خط را بیابید:
# device = "cuda" if torch.cuda.is_available() else "cpu"
# آن را تغییر دهید به:
device = "cpu"
```

### ❌ خطا: "Connection refused"

اطمینان دهید که:
1. سرور در حال اجرا است (`python app.py`)
2. Port ۵۰۰۰ در حال استفاده نیست
3. Firewall مانع نیست

### ❌ خطا: "Model download fails"

```bash
# تنظیم cache
export HF_HOME=/path/to/large/storage
python app.py
```

---

## 📚 منابع مفید

- [Stable Diffusion Documentation](https://huggingface.co/docs/diffusers/)
- [Flask Documentation](https://flask.palletsprojects.com/)
- [PyTorch Guide](https://pytorch.org/get-started/locally/)

---

## 📄 لایسنس

MIT License - آزاد برای استفاده شخصی و تجاری

---

## 🤝 مشارکت

اگر بهبودی پیشنهاد دارید:

1. Fork کن
2. Branch جدید ایجاد کن: `git checkout -b feature/amazing-feature`
3. تغییرات را commit کن: `git commit -m 'Add amazing feature'`
4. Push کن: `git push origin feature/amazing-feature`
5. Pull Request ایجاد کن

---

## ⭐ اگر این پروژه برایت مفید بود، ستاره بده!

```bash
git star aydin343789-design/ai-image-generator-api
```

---

**سوالات یا مشکلات؟ Issues ایجاد کن! 🙋**