FROM python:3.10-slim

WORKDIR /app

# نصب وابستگی‌های سیستمی
RUN apt-get update && apt-get install -y \
    git \
    && rm -rf /var/lib/apt/lists/*

# کپی فایل‌های مورد نیاز
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# کپی کد برنامه
COPY . .

# ایجاد دایرکتوری برای تصاویر
RUN mkdir -p generated_images

# Expose port
EXPOSE 5000

# اجرای برنامه
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app"]
