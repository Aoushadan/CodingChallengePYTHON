-- 1. User Table
CREATE TABLE Users (
    userId INT IDENTITY(1,1) PRIMARY KEY,
    username NVARCHAR(50) NOT NULL UNIQUE,
    password NVARCHAR(255) NOT NULL,
    role NVARCHAR(50) NOT NULL
);

-- 2. Policy Table
CREATE TABLE Policies (
    policyId INT IDENTITY(1,1) PRIMARY KEY,
    policyName NVARCHAR(100) NOT NULL,
    policyType NVARCHAR(50),
    coverageAmount DECIMAL(18, 2),
    premiumAmount DECIMAL(18, 2)
    -- Add other relevant fields if needed
);

-- 3. Client Table
CREATE TABLE Clients (
    clientId INT IDENTITY(1,1) PRIMARY KEY,
    clientName NVARCHAR(100) NOT NULL,
    contactInfo NVARCHAR(150),
    policyId INT,
    FOREIGN KEY (policyId) REFERENCES Policies(policyId)
);

-- 4. Claim Table
CREATE TABLE Claims (
    claimId INT IDENTITY(1,1) PRIMARY KEY,
    claimNumber NVARCHAR(50) NOT NULL,
    dateFiled DATE NOT NULL,
    claimAmount DECIMAL(18, 2) NOT NULL,
    status NVARCHAR(50),
    policyId INT,
    clientId INT,
    FOREIGN KEY (policyId) REFERENCES Policies(policyId),
    FOREIGN KEY (clientId) REFERENCES Clients(clientId)
);

-- 5. Payment Table
CREATE TABLE Payments (
    paymentId INT IDENTITY(1,1) PRIMARY KEY,
    paymentDate DATE NOT NULL,
    paymentAmount DECIMAL(18, 2) NOT NULL,
    clientId INT,
    FOREIGN KEY (clientId) REFERENCES Clients(clientId)
);


-- Insert Users
INSERT INTO Users (username, password, role) VALUES
('admin', 'admin123', 'Administrator'),
('john_doe', 'jd2024!', 'Client'),
('jane_smith', 'js2024!', 'Agent');

-- Insert Policies
INSERT INTO Policies (policyName, policyType, coverageAmount, premiumAmount) VALUES
('Health Secure', 'Health', 500000.00, 12000.00),
('Life Shield', 'Life', 1000000.00, 18000.00),
('Auto Protect', 'Vehicle', 300000.00, 8000.00);

-- Insert Clients
INSERT INTO Clients (clientName, contactInfo, policyId) VALUES
('Alice Johnson', 'alice.johnson@example.com', 1),
('Bob Williams', 'bob.williams@example.com', 2),
('Charlie Davis', 'charlie.davis@example.com', 3);

-- Insert Claims
INSERT INTO Claims (claimNumber, dateFiled, claimAmount, status, policyId, clientId) VALUES
('CLM1001', '2025-01-15', 45000.00, 'Approved', 1, 1),
('CLM1002', '2025-02-20', 120000.00, 'Pending', 2, 2),
('CLM1003', '2025-03-10', 30000.00, 'Rejected', 3, 3);

-- Insert Payments
INSERT INTO Payments (paymentDate, paymentAmount, clientId) VALUES
('2025-01-01', 12000.00, 1),
('2025-02-01', 18000.00, 2),
('2025-03-01', 8000.00, 3);

SELECT * FROM Users;
SELECT * FROM Policies;
SELECT * FROM Clients;
SELECT * FROM Claims;
SELECT * FROM Payments;