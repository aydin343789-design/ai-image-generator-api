# AI Image Generator API | تولید تصویر آفلاین

API و رابط وب فارسی برای تولید تصویر با **Stable Diffusion**. این پروژه برای اجرای محلی، استفاده در شبکهٔ داخلی و دسترسی از گوشی طراحی شده است.

## قابلیت‌ها

- API تولید تصویر با Flask
- رابط وب فارسی برای دسکتاپ و موبایل
- ذخیره‌سازی و تاریخچهٔ تصاویر تولیدشده
- پشتیبانی از GPU در محیط‌های سازگار
- endpoint سلامت سرویس و دریافت فهرست تصاویر

## پیش‌نیازها

- Python 3.10 یا بالاتر
- حداقل ۸ گیگابایت RAM و فضای کافی برای مدل
- GPU سازگار، در صورت نیاز به تولید سریع‌تر

## نصب و اجرا

```bash
git clone https://github.com/aydin343789-design/ai-image-generator-api.git
cd ai-image-generator-api
python -m venv .venv
# Linux/macOS
source .venv/bin/activate
# Windows: .venv\Scripts\activate
pip install -r requirements.txt
python app.py
```

سپس به `http://localhost:5000` بروید. برای استفاده از گوشی، آن را به همان شبکهٔ Wi‑Fi وصل کنید و آدرس IP رایانه را با پورت ۵۰۰۰ باز کنید.

## API نمونه

```bash
curl -X POST http://localhost:5000/api/generate \
  -H "Content-Type: application/json" \
  -d '{"prompt":"یک گربهٔ قهوه‌ای روی صندلی آبی","steps":50,"guidance_scale":7.5,"height":512,"width":512}'
```

| متد | مسیر | کاربرد |
|---|---|---|
| GET | `/health` | بررسی سلامت سرویس |
| POST | `/api/generate` | تولید تصویر |
| GET | `/api/image/<filename>` | دریافت تصویر |
| GET | `/api/images` | فهرست تصاویر |

## استقرار

فایل‌های `Dockerfile`، `docker-compose.yml` و `Procfile` برای آماده‌سازی استقرار در محیط‌های مختلف در مخزن قرار دارند. اجرای مدل‌های بزرگ به منابع سخت‌افزاری و فضای ذخیره‌سازی مناسب نیاز دارد.

## وضعیت و نکات امنیتی

پروژه برای اجرای محلی و شبکهٔ مورد اعتماد مناسب است. قبل از انتشار عمومی، احراز هویت API، محدودسازی درخواست‌ها و سیاست نگهداری تصاویر را اضافه کنید. کلیدها و فایل‌های محیطی را در Git commit نکنید.
