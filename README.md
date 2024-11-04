# Security Management DBMS(ODBC TOOL)

## Overview
A Security Management Database Management System (DBMS) using MySQL, with a Python interface for managing security-related data.

## Features
- Insert, update, delete, and retrieve security data
- User-friendly interface
- Secure connection handling

## Requirements
- Python 3.6+
- MySQL Server
- `mysql-connector-python` package

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/vtbossss/security-management-dbms.git
   cd security-management-dbms
   ```

2. **Install the required Python packages:**
   ```bash
   pip install mysql-connector-python
   ```

3. **Set up the MySQL database:**
   ```sql
   CREATE DATABASE securitydbms;
   ```

4. **Create tables:**
   ```sql
   CREATE TABLE VIP (
       vip_id INT PRIMARY KEY,
       name VARCHAR(50),
       dob DATE,
       gender CHAR(1),
       address VARCHAR(255),
       phone BIGINT
   );

   CREATE TABLE BODYGUARD (
       bodyguard_id INT PRIMARY KEY,
       name VARCHAR(50),
       gender CHAR(1),
       dob DATE,
       address VARCHAR(255),
       phone BIGINT
   );

   CREATE TABLE GUN (
       gun_id INT PRIMARY KEY,
       model VARCHAR(50),
       type VARCHAR(50),
       serial_number VARCHAR(50)
   );

   CREATE TABLE RESOURCES (
       resource_id INT PRIMARY KEY,
       bodyguard_id INT,
       gun_id INT,
       resources VARCHAR(255),
       FOREIGN KEY (bodyguard_id) REFERENCES BODYGUARD(bodyguard_id),
       FOREIGN KEY (gun_id) REFERENCES GUN(gun_id)
   );

   CREATE TABLE SECURITY (
       vip_id INT,
       bodyguard_id INT,
       assignment_id INT PRIMARY KEY,
       startdate DATE,
       enddate DATE,
       FOREIGN KEY (vip_id) REFERENCES VIP(vip_id),
       FOREIGN KEY (bodyguard_id) REFERENCES BODYGUARD(bodyguard_id)
   );
   ```

## Configuration
Update `config.py` with your database credentials:
```python
DB_CONFIG = {
    'user': 'your_mysql_username',
    'password': 'your_mysql_password',
    'host': '127.0.0.1',
    'database': 'securitydbms'
}
```

## Usage
Run the main Python program:
```python
python security_dbms.py
```
