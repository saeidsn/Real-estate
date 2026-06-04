-- =========================================================
-- Real Estate Management System - Database Schema
-- PostgreSQL v13+
-- =========================================================

-- Create schema
CREATE SCHEMA IF NOT EXISTS real_estate;
SET search_path TO real_estate, public;

-- 1. Persons Table (Users/Individuals)
CREATE TABLE persons (
    id BIGSERIAL PRIMARY KEY,
    first_name VARCHAR(100) NOT NULL,
    last_name VARCHAR(100) NOT NULL,
    national_code VARCHAR(20) UNIQUE,
    phone_number VARCHAR(20),
    email VARCHAR(150) UNIQUE,
    password_hash VARCHAR(255),
    wallet_balance BIGINT DEFAULT 0,
    wallet_free_balance BIGINT DEFAULT 0,
    status VARCHAR(50) DEFAULT 'active',
    role_type VARCHAR(50),
    last_login TIMESTAMP,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    created_by BIGINT,
    updated_by BIGINT
);

CREATE INDEX idx_persons_email ON persons(email);
CREATE INDEX idx_persons_national_code ON persons(national_code);
CREATE INDEX idx_persons_status ON persons(status);

-- 2. Units Table (Properties)
CREATE TABLE units (
    id BIGSERIAL PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    address TEXT NOT NULL,
    area DECIMAL(10, 2),
    quality_status VARCHAR(50) DEFAULT 'raw',
    loan_status VARCHAR(50) DEFAULT 'no_loan',
    land_status VARCHAR(50) DEFAULT 'no_land',
    notary_purchase_date DATE,
    notary_purchase_office VARCHAR(255),
    notary_purchase_status VARCHAR(50) DEFAULT 'pending',
    notary_purchase_note TEXT,
    notary_sale_date DATE,
    notary_sale_office VARCHAR(255),
    notary_sale_status VARCHAR(50) DEFAULT 'pending',
    notary_sale_note TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    created_by BIGINT,
    updated_by BIGINT
);

CREATE INDEX idx_units_title ON units(title);
CREATE INDEX idx_units_quality_status ON units(quality_status);
CREATE INDEX idx_units_loan_status ON units(loan_status);

-- 3. Roles Table
CREATE TABLE roles (
    id BIGSERIAL PRIMARY KEY,
    name VARCHAR(100) UNIQUE NOT NULL,
    description TEXT,
    permissions TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- 4. Unit Role Assignments
CREATE TABLE unit_role_assignments (
    id BIGSERIAL PRIMARY KEY,
    unit_id BIGINT NOT NULL REFERENCES units(id) ON DELETE CASCADE,
    person_id BIGINT NOT NULL REFERENCES persons(id) ON DELETE CASCADE,
    role_id BIGINT NOT NULL REFERENCES roles(id) ON DELETE RESTRICT,
    share_percentage NUMERIC(5, 2),
    share_amount BIGINT,
    wage BIGINT DEFAULT 0,
    status VARCHAR(50) DEFAULT 'active',
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    created_by BIGINT,
    updated_by BIGINT,
    UNIQUE(unit_id, person_id, role_id)
);

CREATE INDEX idx_assignments_unit ON unit_role_assignments(unit_id);
CREATE INDEX idx_assignments_person ON unit_role_assignments(person_id);

-- 5. Transactions Table
CREATE TABLE transactions (
    id BIGSERIAL PRIMARY KEY,
    unit_id BIGINT REFERENCES units(id) ON DELETE SET NULL,
    person_id BIGINT NOT NULL REFERENCES persons(id) ON DELETE CASCADE,
    type VARCHAR(50) NOT NULL,
    amount BIGINT NOT NULL,
    description TEXT,
    status VARCHAR(50) DEFAULT 'pending',
    transaction_date DATE NOT NULL,
    created_by BIGINT REFERENCES persons(id) ON DELETE SET NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_by BIGINT
);

CREATE INDEX idx_transactions_person ON transactions(person_id);
CREATE INDEX idx_transactions_type ON transactions(type);
CREATE INDEX idx_transactions_status ON transactions(status);
CREATE INDEX idx_transactions_date ON transactions(transaction_date);

-- 6. Contractors Table
CREATE TABLE contractors (
    id BIGSERIAL PRIMARY KEY,
    person_id BIGINT NOT NULL UNIQUE REFERENCES persons(id) ON DELETE CASCADE,
    default_wage BIGINT DEFAULT 0,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- 7. Contractor Expenses
CREATE TABLE contractor_expenses (
    id BIGSERIAL PRIMARY KEY,
    unit_id BIGINT NOT NULL REFERENCES units(id) ON DELETE CASCADE,
    contractor_id BIGINT NOT NULL REFERENCES contractors(id) ON DELETE CASCADE,
    title VARCHAR(255) NOT NULL,
    amount BIGINT NOT NULL,
    expense_date DATE NOT NULL,
    description TEXT,
    attachment_path VARCHAR(500),
    status VARCHAR(50) DEFAULT 'pending',
    created_by BIGINT REFERENCES persons(id) ON DELETE SET NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_by BIGINT
);

CREATE INDEX idx_expenses_unit ON contractor_expenses(unit_id);
CREATE INDEX idx_expenses_contractor ON contractor_expenses(contractor_id);

-- 8. Alerts Table
CREATE TABLE alerts (
    id BIGSERIAL PRIMARY KEY,
    unit_id BIGINT REFERENCES units(id) ON DELETE CASCADE,
    person_id BIGINT REFERENCES persons(id) ON DELETE CASCADE,
    alert_type VARCHAR(50) NOT NULL,
    title VARCHAR(255) NOT NULL,
    message TEXT NOT NULL,
    status VARCHAR(50) DEFAULT 'open',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    acknowledged_at TIMESTAMP,
    closed_at TIMESTAMP
);

CREATE INDEX idx_alerts_status ON alerts(status);
CREATE INDEX idx_alerts_type ON alerts(alert_type);
CREATE INDEX idx_alerts_created ON alerts(created_at);

-- 9. Loans Table
CREATE TABLE loans (
    id BIGSERIAL PRIMARY KEY,
    unit_id BIGINT NOT NULL REFERENCES units(id) ON DELETE CASCADE,
    amount BIGINT NOT NULL,
    status VARCHAR(50) DEFAULT 'active',
    loan_date DATE NOT NULL,
    settlement_date DATE,
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    created_by BIGINT REFERENCES persons(id) ON DELETE SET NULL
);

-- 10. Lands Table
CREATE TABLE lands (
    id BIGSERIAL PRIMARY KEY,
    unit_id BIGINT NOT NULL REFERENCES units(id) ON DELETE CASCADE,
    amount BIGINT NOT NULL,
    status VARCHAR(50) DEFAULT 'active',
    land_date DATE NOT NULL,
    settlement_date DATE,
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    created_by BIGINT REFERENCES persons(id) ON DELETE SET NULL
);

-- 11. Activity Logs
CREATE TABLE activity_logs (
    id BIGSERIAL PRIMARY KEY,
    user_id BIGINT REFERENCES persons(id) ON DELETE SET NULL,
    action VARCHAR(255) NOT NULL,
    entity_type VARCHAR(100),
    entity_id BIGINT,
    old_value TEXT,
    new_value TEXT,
    ip_address VARCHAR(50),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX idx_logs_user ON activity_logs(user_id);
CREATE INDEX idx_logs_created ON activity_logs(created_at);

-- 12. Backups Table
CREATE TABLE backups (
    id BIGSERIAL PRIMARY KEY,
    backup_name VARCHAR(255) NOT NULL,
    backup_path VARCHAR(500) NOT NULL,
    backup_size BIGINT,
    backup_type VARCHAR(50) DEFAULT 'manual',
    created_by BIGINT REFERENCES persons(id) ON DELETE SET NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Insert default roles
INSERT INTO roles (name, description, permissions) VALUES
('owner', 'مالک/سرمایه‌گذار', '{"view_own_shares": true, "view_reports": true}'),
('contractor', 'پیمانکار', '{"add_expenses": true, "view_own_expenses": true}'),
('alfa', 'الفا - مشاور ارشد', '{"manage_units": true, "manage_transactions": true}'),
('beta', 'بتا - همکار', '{"add_transactions": true, "view_reports": true}'),
('theta', 'تتا - آگهی‌دهنده', '{"view_units": true}'),
('advisor', 'مشاور/کارگزار', '{"view_units": true, "view_reports": true}'),
('manager', 'مدیر', '{"admin": true}'),
('operator', 'اپراتور', '{"data_entry": true, "view_reports": true}'),
('accountant', 'حسابدار', '{"view_transactions": true, "view_reports": true, "verify_transactions": true}');
