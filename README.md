# 🏢 سیستم مدیریت ملک و حسابداری دفتر

## Property Management & Real Estate Accounting System

سیستم جامع مدیریت ملک، سرمایه‌گذاری و حسابداری برای دفاتر معاملات ملک با قابلیت‌های حرفه‌ای و امنیت بالا.

---

## ✨ ویژگی‌های اصلی

- ✅ **مدیریت واحدها**: ثبت و مدیریت ملک‌ها با وضعیت‌های مختلف
- ✅ **سیستم حسابداری کامل**: تراکنش‌ها، کیف پول، موجودی پول آزاد
- ✅ **مدیریت نقش‌ها**: مالک، پیمانکار، الفا، بتا، تتا، مشاور
- ✅ **ریز هزینه‌های پیمانکار**: ثبت هزینه‌ها از موبایل و PC
- ✅ **تقسیم سود و درآمد**: محاسبه خودکار سهم هر شخص
- ✅ **دفترخانه خرید و فروش**: مدیریت و هشدار خودکار
- ✅ **سیستم هشدار**: ریمایندرهای هوشمند برای دفترخانه و پول آزاد
- ✅ **کنترل تراز**: تشخیص خودکار مغایرت ورود و خروج
- ✅ **گزارش‌گیری پیشرفته**: چاپ شخصی‌سازی‌شده برای هر کاربر
- ✅ **بکاپ و ریستور**: حفاظت کامل داده‌ها
- ✅ **لاگ تمام عملیات**: تاریخچه کامل هر تغییر
- ✅ **امنیت بالا**: رمزنگاری، JWT، احراز هویت دو مرحله‌ای

---

## 🛠️ تکنولوژی‌های استفاده‌شده

### Backend
- **Laravel 11** - Framework قدرتمند PHP
- **PostgreSQL** - Database محکم و معتبر
- **JWT** - احراز هویت امن
- **API RESTful** - معماری مدرن

### Frontend
- **React 18** - کتاب‌خانه قدرتمند UI
- **TypeScript** - امنیت نوع
- **Tailwind CSS** - طراحی مدرن و واکنش‌پذیر
- **Redux** - مدیریت state

---

## 📋 ساختار پروژه

```
Real-estate/
├── backend/                      # Laravel Backend
│   ├── app/
│   │   ├── Http/Controllers/
│   │   ├── Services/
│   │   ├── Models/
│   │   └── Events/
│   ├── database/
│   │   ├── migrations/
│   │   └── seeds/
��   ├── routes/
│   ├── .env.example
│   └── composer.json
│
├── frontend/                     # React Frontend
│   ├── src/
│   │   ├── pages/
│   │   ├── components/
│   │   ├── hooks/
│   │   ├── redux/
│   │   ├── api/
│   │   └── App.tsx
│   ├── package.json
│   └── vite.config.ts
│
├── database/
│   ├── schema.sql
│   └── migrations/
│
├── docs/
│   ├── DATABASE_STRUCTURE.md
│   ├── API_SPECIFICATION.md
│   └── ARCHITECTURE.md
│
├── .gitignore
└── README.md
```

---

## 🚀 نصب و اجرا

### پیش‌نیازها
- PHP 8.2+
- Node.js 18+
- PostgreSQL 13+
- Composer
- npm یا yarn

### Backend Setup

```bash
# رفتن به دایرکتوری backend
cd backend

# نصب dependencies
composer install

# کپی کردن فایل .env
cp .env.example .env

# تولید APP_KEY
php artisan key:generate

# تولید JWT_SECRET
php artisan jwt:secret

# اجرای migrations
php artisan migrate --seed

# شروع سرور
php artisan serve
```

### Frontend Setup

```bash
# رفتن به دایرکتوری frontend
cd frontend

# نصب dependencies
npm install

# کپی کردن .env
cp .env.example .env

# شروع سرور توسعه
npm run dev
```

---

## 📚 مستندات

- [**DATABASE_STRUCTURE.md**](docs/DATABASE_STRUCTURE.md) - ساختار دیتابیس و جداول
- [**API_SPECIFICATION.md**](docs/API_SPECIFICATION.md) - مشخصات کامل API
- [**ARCHITECTURE.md**](ARCHITECTURE.md) - معماری سیستم

---

## 🔐 امنیت

- ✅ JWT Authentication
- ✅ Password Hashing (Bcrypt)
- ✅ SQL Injection Prevention
- ✅ CORS Configuration
- ✅ Rate Limiting
- ✅ Complete Activity Logging

---

**توسعه‌دهنده:** Copilot  
**تاریخ شروع:** 1403/03/15  
**نسخه:** 1.0.0
