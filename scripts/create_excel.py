"""
Real Estate Management System - Excel Generator
Generates a comprehensive Excel file with linked sheets
"""

from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter
from openpyxl.worksheet.datavalidation import DataValidation
import datetime

def create_header_style():
    """Create header styling"""
    header_fill = PatternFill(start_color="1F4E78", end_color="1F4E78", fill_type="solid")
    header_font = Font(bold=True, color="FFFFFF", size=12)
    return header_fill, header_font

def create_border():
    """Create cell border"""
    thin_border = Border(
        left=Side(style='thin'),
        right=Side(style='thin'),
        top=Side(style='thin'),
        bottom=Side(style='thin')
    )
    return thin_border

def setup_persons_sheet(ws):
    """Setup Persons sheet"""
    ws.title = "Persons"
    
    headers = ["ID", "First Name", "Last Name", "National Code", "Phone", "Email", "Wallet Balance", "Status", "Role Type"]
    ws.append(headers)
    
    header_fill, header_font = create_header_style()
    border = create_border()
    
    for cell in ws[1]:
        cell.fill = header_fill
        cell.font = header_font
        cell.alignment = Alignment(horizontal="center", vertical="center")
        cell.border = border
    
    # Sample data
    sample_data = [
        [1, "علی", "احمدی", "0012345678", "09121234567", "ali@example.com", 1000000, "active", "owner"],
        [2, "فاطمه", "محمدی", "0012345679", "09129876543", "fatima@example.com", 500000, "active", "contractor"],
        [3, "محمد", "اصغری", "0012345680", "09125555555", "mohammad@example.com", 2000000, "active", "alfa"],
    ]
    
    for row in sample_data:
        ws.append(row)
    
    # Set column widths
    ws.column_dimensions['A'].width = 8
    ws.column_dimensions['B'].width = 15
    ws.column_dimensions['C'].width = 15
    ws.column_dimensions['D'].width = 15
    ws.column_dimensions['E'].width = 15
    ws.column_dimensions['F'].width = 20
    ws.column_dimensions['G'].width = 15
    ws.column_dimensions['H'].width = 12
    ws.column_dimensions['I'].width = 12

def setup_units_sheet(ws):
    """Setup Units sheet"""
    ws.title = "Units"
    
    headers = ["ID", "Title", "Address", "Area", "Quality Status", "Loan Status", "Land Status", "Notary Purchase Date", "Created Date"]
    ws.append(headers)
    
    header_fill, header_font = create_header_style()
    border = create_border()
    
    for cell in ws[1]:
        cell.fill = header_fill
        cell.font = header_font
        cell.alignment = Alignment(horizontal="center", vertical="center")
        cell.border = border
    
    # Sample data
    sample_data = [
        [1, "آذین بلوک 29", "خیابان ولیعصر، پلاک 100", 120.5, "raw", "no_loan", "no_land", "1403-03-20", datetime.date.today()],
        [2, "قادس پلاس", "خیابان ستارخان، پلاک 50", 95.0, "full_luxury", "settled", "updated", "1403-02-15", datetime.date.today()],
    ]
    
    for row in sample_data:
        ws.append(row)
    
    # Set column widths
    for col in range(1, 10):
        ws.column_dimensions[get_column_letter(col)].width = 15

def setup_roles_sheet(ws):
    """Setup Roles sheet"""
    ws.title = "Roles"
    
    headers = ["ID", "Role Name", "Description"]
    ws.append(headers)
    
    header_fill, header_font = create_header_style()
    
    for cell in ws[1]:
        cell.fill = header_fill
        cell.font = header_font
        cell.alignment = Alignment(horizontal="center", vertical="center")
    
    roles = [
        [1, "Owner", "مالک/سرمایه‌گذار"],
        [2, "Contractor", "پیمانکار"],
        [3, "Alfa", "الفا - مشاور ارشد"],
        [4, "Beta", "بتا - همکار"],
        [5, "Theta", "تتا - آگهی‌دهنده"],
        [6, "Advisor", "مشاور/کارگزار"],
        [7, "Manager", "مدیر"],
        [8, "Operator", "اپراتور"],
        [9, "Accountant", "حسابدار"],
    ]
    
    for role in roles:
        ws.append(role)
    
    ws.column_dimensions['A'].width = 5
    ws.column_dimensions['B'].width = 15
    ws.column_dimensions['C'].width = 30

def setup_unit_role_assignments_sheet(ws, wb):
    """Setup Unit-Role Assignments sheet with dropdowns"""
    ws.title = "Unit-Role Assignments"
    
    headers = ["ID", "Unit", "Person", "Role", "Share %", "Share Amount", "Wage", "Status", "Notes"]
    ws.append(headers)
    
    header_fill, header_font = create_header_style()
    
    for cell in ws[1]:
        cell.fill = header_fill
        cell.font = header_font
        cell.alignment = Alignment(horizontal="center", vertical="center")
    
    # Create dropdowns for Units
    unit_dv = DataValidation(type="list", formula1="=Units!$A$2:$A$3", allow_blank=True)
    unit_dv.error = 'Please select a unit'
    unit_dv.errorTitle = 'Invalid Entry'
    ws.add_data_validation(unit_dv)
    unit_dv.add(f'B2:B100')
    
    # Create dropdowns for Persons
    person_dv = DataValidation(type="list", formula1="=Persons!$A$2:$A$4", allow_blank=True)
    person_dv.error = 'Please select a person'
    person_dv.errorTitle = 'Invalid Entry'
    ws.add_data_validation(person_dv)
    person_dv.add(f'C2:C100')
    
    # Create dropdowns for Roles
    role_dv = DataValidation(type="list", formula1="=Roles!$A$2:$A$9", allow_blank=True)
    role_dv.error = 'Please select a role'
    role_dv.errorTitle = 'Invalid Entry'
    ws.add_data_validation(role_dv)
    role_dv.add(f'D2:D100')
    
    # Create dropdowns for Status
    status_dv = DataValidation(type="list", formula1='"active,inactive"', allow_blank=True)
    ws.add_data_validation(status_dv)
    status_dv.add(f'H2:H100')
    
    # Sample data
    ws.append([1, 1, 1, 1, 40, 400000000, 0, "active", "مالک اصلی"])
    ws.append([2, 1, 2, 2, 0, 0, 30000000, "active", "پیمانکار"])
    ws.append([3, 1, 3, 3, 60, 600000000, 0, "active", "الفا"])
    
    # Set column widths
    for col in range(1, 10):
        ws.column_dimensions[get_column_letter(col)].width = 15

def setup_transactions_sheet(ws):
    """Setup Transactions sheet"""
    ws.title = "Transactions"
    
    headers = ["ID", "Unit ID", "Person ID", "Type", "Amount", "Description", "Status", "Date", "Created At"]
    ws.append(headers)
    
    header_fill, header_font = create_header_style()
    
    for cell in ws[1]:
        cell.fill = header_fill
        cell.font = header_font
        cell.alignment = Alignment(horizontal="center", vertical="center")
    
    # Create dropdowns for Type
    type_dv = DataValidation(type="list", formula1='"deposit,withdrawal,transfer,income,expense"', allow_blank=True)
    ws.add_data_validation(type_dv)
    type_dv.add('D2:D1000')
    
    # Create dropdowns for Status
    status_dv = DataValidation(type="list", formula1='"pending,confirmed,rejected"', allow_blank=True)
    ws.add_data_validation(status_dv)
    status_dv.add('G2:G1000')
    
    # Sample data
    ws.append([1, 1, 1, "deposit", 100000000, "واریز حق سهم", "confirmed", datetime.date.today(), datetime.datetime.now()])
    ws.append([2, 1, 2, "expense", 5000000, "هزینه کار", "pending", datetime.date.today(), datetime.datetime.now()])
    
    for col in range(1, 10):
        ws.column_dimensions[get_column_letter(col)].width = 15

def setup_contractor_expenses_sheet(ws):
    """Setup Contractor Expenses sheet"""
    ws.title = "Contractor Expenses"
    
    headers = ["ID", "Unit ID", "Contractor ID", "Title", "Amount", "Date", "Description", "Status"]
    ws.append(headers)
    
    header_fill, header_font = create_header_style()
    
    for cell in ws[1]:
        cell.fill = header_fill
        cell.font = header_font
        cell.alignment = Alignment(horizontal="center", vertical="center")
    
    # Create dropdowns for Status
    status_dv = DataValidation(type="list", formula1='"pending,approved,rejected"', allow_blank=True)
    ws.add_data_validation(status_dv)
    status_dv.add('H2:H1000')
    
    ws.append([1, 1, 2, "کاشی آشپزخانه", 3000000, datetime.date.today(), "سفارش درجه یک", "pending"])
    ws.append([2, 1, 2, "سرامیک سالن", 5000000, datetime.date.today(), "سرامیک ایتالیایی", "approved"])
    
    for col in range(1, 9):
        ws.column_dimensions[get_column_letter(col)].width = 15

def setup_reports_sheet(ws):
    """Setup Reports sheet with auto-calculated data"""
    ws.title = "Reports"
    
    ws['A1'] = "تقسیم سود و درآمد"
    ws['A1'].font = Font(bold=True, size=14, color="1F4E78")
    
    ws['A3'] = "Unit ID"
    ws['B3'] = "Person Name"
    ws['C3'] = "Role"
    ws['D3'] = "Share %"
    ws['E3'] = "Share Amount"
    ws['F3'] = "Wage"
    ws['G3'] = "Total Income"
    
    header_fill, header_font = create_header_style()
    for col in range(1, 8):
        cell = ws.cell(row=3, column=col)
        cell.fill = header_fill
        cell.font = header_font
        cell.alignment = Alignment(horizontal="center", vertical="center")
    
    # Sample calculations (using formulas would require more complex setup)
    ws.append([1, "علی احمدی", "Owner", 40, 400000000, 0, "=E4+F4"])
    ws.append([1, "فاطمه محمدی", "Contractor", 0, 0, 30000000, "=E5+F5"])
    ws.append([1, "محمد اصغری", "Alfa", 60, 600000000, 0, "=E6+F6"])
    
    for col in range(1, 8):
        ws.column_dimensions[get_column_letter(col)].width = 18

def setup_alerts_sheet(ws):
    """Setup Alerts sheet"""
    ws.title = "Alerts"
    
    headers = ["ID", "Unit ID", "Alert Type", "Message", "Status", "Created At", "Acknowledged At"]
    ws.append(headers)
    
    header_fill, header_font = create_header_style()
    
    for cell in ws[1]:
        cell.fill = header_fill
        cell.font = header_font
        cell.alignment = Alignment(horizontal="center", vertical="center")
    
    # Create dropdowns for Status
    status_dv = DataValidation(type="list", formula1='"open,acknowledged,closed"', allow_blank=True)
    ws.add_data_validation(status_dv)
    status_dv.add('E2:E1000')
    
    # Create dropdowns for Alert Type
    alert_type_dv = DataValidation(type="list", formula1='"notary_purchase,notary_sale,free_money,loan,land"', allow_blank=True)
    ws.add_data_validation(alert_type_dv)
    alert_type_dv.add('C2:C1000')
    
    ws.append([1, 1, "notary_purchase", "دفترخانه خرید تا 5 روز دیگر", "open", datetime.date.today(), ""])
    ws.append([2, 1, "free_money", "پول آزاد برای استفاده", "acknowledged", datetime.date.today(), datetime.date.today()])
    
    for col in range(1, 8):
        ws.column_dimensions[get_column_letter(col)].width = 18

def setup_settings_sheet(ws):
    """Setup Settings sheet"""
    ws.title = "Settings"
    
    ws['A1'] = "System Settings"
    ws['A1'].font = Font(bold=True, size=14, color="1F4E78")
    
    settings = [
        ["System Name", "Real Estate Management System"],
        ["Version", "1.0.0"],
        ["Created Date", datetime.date.today()],
        ["Last Updated", datetime.datetime.now()],
        ["Currency", "IRR (تومان)"],
        ["Default Language", "Persian (فارسی)"],
    ]
    
    for row in settings:
        ws.append(row)
    
    ws.column_dimensions['A'].width = 20
    ws.column_dimensions['B'].width = 30

def create_excel_file():
    """Create the main Excel workbook"""
    wb = Workbook()
    
    # Remove default sheet
    if 'Sheet' in wb.sheetnames:
        wb.remove(wb['Sheet'])
    
    # Setup sheets in order
    setup_settings_sheet(wb.create_sheet())
    setup_persons_sheet(wb.create_sheet())
    setup_units_sheet(wb.create_sheet())
    setup_roles_sheet(wb.create_sheet())
    setup_unit_role_assignments_sheet(wb.create_sheet(), wb)
    setup_transactions_sheet(wb.create_sheet())
    setup_contractor_expenses_sheet(wb.create_sheet())
    setup_reports_sheet(wb.create_sheet())
    setup_alerts_sheet(wb.create_sheet())
    
    # Save file
    filename = "Real_Estate_Management_System.xlsx"
    wb.save(filename)
    print(f"✅ فایل Excel با موفقیت ایجاد شد: {filename}")
    print(f"📊 تعداد Sheets: {len(wb.sheetnames)}")
    print(f"📝 Sheets: {', '.join(wb.sheetnames)}")

if __name__ == "__main__":
    create_excel_file()
