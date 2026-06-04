# 📊 Real Estate Management Excel Generator

## نحوه استفاده

### ۱. نصب وابستگی‌ها

```bash
pip install openpyxl
```

### ۲. اجرای برنامه

```bash
python scripts/create_excel.py
```

### ۳. خروجی

فایل `Real_Estate_Management_System.xlsx` ایجاد می‌شود.

---

## 📋 Sheets موجود در فایل

### 1️⃣ **Settings** - تنظیمات سیستم
- نام سیستم
- نسخه
- تاریخ ایجاد
- تنظیمات عمومی

### 2️⃣ **Persons** - اشخاص و کاربران
- ID
- نام و نام خانوادگی
- کد ملی
- شماره تماس
- ایمیل
- موجودی کیف پول
- وضعیت (فعال/غیرفعال)
- نوع نقش

### 3️⃣ **Units** - واحدها و ملک‌ها
- ID
- عنوان واحد
- آدرس
- مساحت
- وضعیت کیفیت (raw, full_luxury, ...)
- وضعیت وام
- وضعیت عرصه
- تاریخ دفترخانه خرید
- تاریخ ثبت

### 4️⃣ **Roles** - نقش‌ها
- ID
- نام نقش (Owner, Contractor, Alfa, Beta, ...)
- توضیح

### 5️⃣ **Unit-Role Assignments** - تخصیص نقش‌ها ⭐
**ارتباط بین Persons, Units, Roles**
- ID
- **Unit** (Dropdown از Units)
- **Person** (Dropdown از Persons)
- **Role** (Dropdown از Roles)
- درصد سهم
- مبلغ سهم
- حقوق/اجرت
- وضعیت

### 6️⃣ **Transactions** - تراکنش‌ها
- ID
- Unit ID
- Person ID
- **نوع** (Dropdown: deposit, withdrawal, transfer, income, expense)
- مبلغ
- توضیح
- **وضعیت** (Dropdown: pending, confirmed, rejected)
- تاریخ
- زمان ایجاد

### 7️⃣ **Contractor Expenses** - هزینه‌های پیمانکار
- ID
- Unit ID
- Contractor ID
- عنوان هزینه
- مبلغ
- تاریخ
- توضیح
- **وضعیت** (Dropdown: pending, approved, rejected)

### 8️⃣ **Reports** - گزارش‌های خودکار
تقسیم سود و درآمد:
- Unit ID
- نام فرد
- نقش
- درصد سهم
- مبلغ سهم
- حقوق
- **کل درآمد** (فرمول خودکار: سهم + حقوق)

### 9️⃣ **Alerts** - هشدارها و یادآورها
- ID
- Unit ID
- **نوع هشدار** (Dropdown: notary_purchase, notary_sale, free_money, loan, land)
- پیام
- **وضعیت** (Dropdown: open, acknowledged, closed)
- تاریخ ایجاد
- تاریخ تأیید

---

## 🔗 ارتباطات بین Sheets

```
Unit-Role Assignments (میانی)
    ↓
    ├─→ Persons (برای انتخاب فرد)
    ├─→ Units (برای انتخاص واحد)
    └─→ Roles (برای انتخاب نقش)

Transactions & Contractor Expenses
    ↓
    └─→ Unit-Role Assignments (برای مرجع)

Reports
    ↓
    └─→ Unit-Role Assignments (برای محاسبات)

Alerts
    ↓
    └─→ Units (برای متصل شدن به واحد)
```

---

## ✨ ویژگی‌های Dropdown

### 🎯 Unit-Role Assignments:
- **Unit Column**: انتخاب از لیست Units
- **Person Column**: انتخاب از لیست Persons
- **Role Column**: انتخاب از لیست Roles
- **Status Column**: active / inactive

### 🎯 Transactions:
- **Type Column**: deposit / withdrawal / transfer / income / expense
- **Status Column**: pending / confirmed / rejected

### 🎯 Contractor Expenses:
- **Status Column**: pending / approved / rejected

### 🎯 Alerts:
- **Alert Type Column**: notary_purchase / notary_sale / free_money / loan / land
- **Status Column**: open / acknowledged / closed

---

## 📝 نکات مهم

1. **ID Column** - ستون شناسه را خالی نگذار (خودکار پر می‌شود)
2. **Dropdowns** - برای انتخاب از دروپ‌داون روی سلول کلیک کن
3. **Dates** - تاریخ را به فرمت YYYY-MM-DD وارد کن
4. **Calculations** - ستون‌های محاسبه شده خودکار آپدیت می‌شوند
5. **References** - وقتی در Persons یا Units اضافه کنی، بلافاصله در Dropdowns ظاهر می‌شوند

---

## 🚀 استفاده

1. **فایل را دانلود کن** یا **Python Script را اجرا کن**
2. **فایل Excel را باز کن** در Excel یا LibreOffice
3. **اطلاعات اساسی را وارد کن** (Persons, Units, Roles)
4. **Assignments را انجام بده** (تخصیص نقش‌ها)
5. **Transactions و Expenses را ثبت کن**
6. **گزارش‌ها را ببین** (خودکار محاسبه می‌شوند)

---

## 📞 مشکلات و راه‌حل‌ها

### مشکل: Dropdown کار نمی‌کند
- ✅ اطمینان بخش که Persons/Units/Roles ستون‌های صحیح را دارند
- ✅ سلول‌های جدید را اضافه کن (فرمول به صورت خودکار ت��ظیم می‌شود)

### مشکل: فرمول‌ها کار نمی‌کنند
- ✅ اطمینان بخش که Excel به محاسبه‌ی خودکار فعال است
- ✅ Ctrl+Shift+F9 را فشار بده تا تمام فرمول‌ها محاسبه شوند

---

**آماده‌ای برای استفاده؟** 🎉
