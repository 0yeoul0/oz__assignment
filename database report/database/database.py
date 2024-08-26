import sqlite3

def initialize_database():
    # 데이터베이스 연결
    conn = sqlite3.connect('your_database.db')
    cursor = conn.cursor()

    # 테이블 생성
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS customers (
            customerNumber INTEGER PRIMARY KEY,
            customerName TEXT,
            contactLastName TEXT,
            contactFirstName TEXT,
            phone TEXT,
            addressLine1 TEXT,
            addressLine2 TEXT,
            city TEXT,
            state TEXT,
            postalCode TEXT,
            country TEXT,
            salesRepEmployeeNumber INTEGER,
            creditLimit REAL
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS products (
            productCode TEXT PRIMARY KEY,
            productName TEXT,
            productLine TEXT,
            productScale TEXT,
            productVendor TEXT,
            productDescription TEXT,
            quantityInStock INTEGER,
            buyPrice REAL,
            MSRP REAL
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS employees (
            employeeNumber INTEGER PRIMARY KEY,
            lastName TEXT,
            firstName TEXT,
            extension TEXT,
            email TEXT,
            officeCode TEXT,
            reportsTo INTEGER,
            jobTitle TEXT
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS offices (
            officeCode TEXT PRIMARY KEY,
            city TEXT,
            phone TEXT,
            addressLine1 TEXT,
            addressLine2 TEXT,
            state TEXT,
            country TEXT,
            postalCode TEXT,
            territory TEXT
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS orders (
            orderNumber INTEGER PRIMARY KEY,
            orderDate TEXT,
            requiredDate TEXT,
            shippedDate TEXT,
            status TEXT,
            comments TEXT,
            customerNumber INTEGER
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS orderdetails (
            orderNumber INTEGER,
            productCode TEXT,
            quantityOrdered INTEGER,
            priceEach REAL,
            orderLineNumber INTEGER,
            PRIMARY KEY (orderNumber, productCode)
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS payments (
            customerNumber INTEGER,
            checkNumber TEXT,
            paymentDate TEXT,
            amount REAL,
            PRIMARY KEY (customerNumber, checkNumber)
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS productlines (
            productLine TEXT PRIMARY KEY,
            textDescription TEXT,
            htmlDescription TEXT,
            image BLOB
        )
    ''')

    # 데이터 삽입
    cursor.execute('''
        INSERT OR IGNORE INTO customers (customerNumber, customerName, contactLastName, contactFirstName, phone, addressLine1, addressLine2, city, state, postalCode, country, salesRepEmployeeNumber, creditLimit)
        VALUES (497, 'New Customer Inc.', 'Smith', 'John', '+1 555-1234', '123 Elm St.', NULL, 'Los Angeles', 'CA', '90001', 'USA', 1370, 50000)
    ''')

    cursor.execute('''
        INSERT OR IGNORE INTO customers (customerNumber, customerName, contactLastName, contactFirstName, phone, addressLine1, addressLine2, city, state, postalCode, country, salesRepEmployeeNumber, creditLimit)
        VALUES (498, 'Eastern Ventures Ltd.', 'Chen', 'Wei', '+86 21-12345678', '456 Bamboo St.', NULL, 'Shanghai', NULL, '200000', 'China', 1621, 75000)
    ''')

    cursor.execute('''
        INSERT OR IGNORE INTO products (productCode, productName, productLine, productScale, productVendor, productDescription, quantityInStock, buyPrice, MSRP)
        VALUES ('S12_1108', 'Super Car', 'Classic Cars', '1:18', 'High-Speed Classics', 'A top-tier supercar model.', 150, 85.75, 120.00)
    ''')

    cursor.execute('''
        INSERT OR IGNORE INTO products (productCode, productName, productLine, productScale, productVendor, productDescription, quantityInStock, buyPrice, MSRP)
        VALUES ('S24_2021', 'Jet Airliner', 'Planes', '1:400', 'Sky Models', 'A detailed model of a commercial jet airliner.', 200, 120.00, 180.00)
    ''')

    cursor.execute('''
        INSERT OR IGNORE INTO employees (employeeNumber, lastName, firstName, extension, email, officeCode, reportsTo, jobTitle)
        VALUES (1703, 'Doe', 'Jane', 'x1234', 'jdoe@classicmodelcars.com', '1', 1143, 'Sales Representative')
    ''')

    cursor.execute('''
        INSERT OR IGNORE INTO offices (officeCode, city, phone, addressLine1, addressLine2, state, country, postalCode, territory)
        VALUES ('8', 'San Francisco', '+1 555-5678', '789 Market St.', NULL, 'CA', 'USA', '94103', 'NA')
    ''')

    cursor.execute('''
        INSERT OR IGNORE INTO orders (orderNumber, orderDate, requiredDate, shippedDate, status, comments, customerNumber)
        VALUES (10426, '2024-08-26', '2024-09-01', NULL, 'In Process', 'Urgent delivery required.', 497)
    ''')

    cursor.execute('''
        INSERT OR IGNORE INTO orderdetails (orderNumber, productCode, quantityOrdered, priceEach, orderLineNumber)
        VALUES (10426, 'S12_1108', 10, 85.75, 1)
    ''')

    cursor.execute('''
        INSERT OR IGNORE INTO payments (customerNumber, checkNumber, paymentDate, amount)
        VALUES (497, 'HQ123456', '2024-08-26', 857.50)
    ''')

    cursor.execute('''
        INSERT OR IGNORE INTO productlines (productLine, textDescription, htmlDescription, image)
        VALUES ('Electric Cars', 'High-performance electric vehicles.', '<p>Explore the future with our electric car models.</p>', NULL)
    ''')

    # 변경사항 커밋
    conn.commit()

    # 데이터를 조회하여 출력
    def print_query_results(query):
        cursor.execute(query)
        rows = cursor.fetchall()
        for row in rows:
            print(row)

    # (1) 모든 고객 정보 조회
    print("Customers:")
    print_query_results("SELECT * FROM customers")

    # (2) 모든 제품 목록 조회
    print("\nProducts:")
    print_query_results("SELECT * FROM products")

    # (3) 모든 직원의 이름과 직급 조회
    print("\nEmployees (Name and Job Title):")
    print_query_results("SELECT firstName, lastName, jobTitle FROM employees")

    # (4) 모든 사무실의 위치 조회
    print("\nOffices (Location):")
    print_query_results("SELECT city, addressLine1, addressLine2, state, postalCode FROM offices")

    # (5) 최근 10개의 주문 조회
    print("\nRecent 10 Orders:")
    print_query_results("SELECT * FROM orders ORDER BY orderDate DESC LIMIT 10")

    # (6) 특정 주문의 모든 상세 정보 조회
    order_number = 10426  # 예시: 특정 주문 번호
    print(f"\nOrder Details for Order Number {order_number}:")
    print_query_results(f"SELECT * FROM orderdetails WHERE orderNumber = {order_number}")

    # (7) 특정 고객의 모든 지불 정보 조회
    customer_number = 497  # 예시: 특정 고객 번호
    print(f"\nPayments for Customer Number {customer_number}:")
    print_query_results(f"SELECT * FROM payments WHERE customerNumber = {customer_number}")

    # (8) 각 제품 라인의 설명 조회
    print("\nProduct Lines:")
    print_query_results("SELECT productLine, textDescription FROM productlines")

    # (9) 특정 지역의 고객 조회
    region = 'CA'  # 예시: 특정 주
    print(f"\nCustomers in {region}:")
    print_query_results(f"SELECT * FROM customers WHERE state = '{region}'")

    # (10) 특정 가격 범위의 제품 조회
    min_price = 80.00
    max_price = 130.00
    print(f"\nProducts priced between {min_price} and {max_price}:")
    print_query_results(f"SELECT * FROM products WHERE buyPrice BETWEEN {min_price} AND {max_price}")

    # 데이터 갱신
    # (1) 특정 고객의 주소 갱신
    cursor.execute('''
        UPDATE customers
        SET addressLine1 = '456 Maple Ave.', city = 'Santa Monica', postalCode = '90401'
        WHERE customerNumber = 497
    ''')

    # (2) 특정 제품의 가격 갱신
    cursor.execute('''
        UPDATE products
        SET MSRP = 125.00
        WHERE productCode = 'S12_1108'
    ''')

    # (3) 특정 직원의 직급 갱신
    cursor.execute('''
        UPDATE employees
        SET jobTitle = 'Senior Sales Representative'
        WHERE employeeNumber = 1703
    ''')

    # (4) 특정 사무실의 전화번호 갱신
    cursor.execute('''
        UPDATE offices
        SET phone = '+1 555-9999'
        WHERE officeCode = '8'
    ''')

    # (5) 특정 주문의 상태 갱신
    cursor.execute('''
        UPDATE orders
        SET status = 'Shipped'
        WHERE orderNumber = 10426
    ''')

    # (6) 특정 주문 상세의 수량 갱신
    cursor.execute('''
        UPDATE orderdetails
        SET quantityOrdered = 15
        WHERE orderNumber = 10426 AND productCode = 'S12_1108'
    ''')

    # (7) 특정 지불의 금액 갱신
    cursor.execute('''
        UPDATE payments
        SET amount = 900.00
        WHERE customerNumber = 497 AND checkNumber = 'HQ123456'
    ''')

    # (8) 특정 제품 라인의 설명 갱신
    cursor.execute('''
        UPDATE productlines
        SET textDescription = 'Cutting-edge electric vehicles with advanced features.'
        WHERE productLine = 'Electric Cars'
    ''')

    # (9) 특정 고객의 이메일 갱신
    cursor.execute('''
        UPDATE customers
        SET contactFirstName = 'Jonathan'
        WHERE customerNumber = 497
    ''')

    # 데이터 삭제
    # (1) 특정 고객 삭제
    cursor.execute('''
        DELETE FROM customers
        WHERE customerNumber = 498
    ''')

    # (2) 특정 제품 삭제
    cursor.execute('''
        DELETE FROM products
        WHERE productCode = 'S24_2021'
    ''')

    # (3) 특정 직원 삭제
    cursor.execute('''
        DELETE FROM employees
        WHERE employeeNumber = 1703
    ''')

    # (4) 특정 사무실 삭제
    cursor.execute('''
        DELETE FROM offices
        WHERE officeCode = '8'
    ''')

    # (5) 특정 주문 삭제
    cursor.execute('''
        DELETE FROM orders
        WHERE orderNumber = 10426
    ''')

    # (6) 특정 주문 상세 삭제
    cursor.execute('''
        DELETE FROM orderdetails
        WHERE orderNumber = 10426 AND productCode = 'S12_1108'
    ''')

    # (7) 특정 지불 내역 삭제
    cursor.execute('''
        DELETE FROM payments
        WHERE customerNumber = 497 AND checkNumber = 'HQ123456'
    ''')

    # (8) 특정 제품 라인 삭제
    cursor.execute('''
        DELETE FROM productlines
        WHERE productLine = 'Electric Cars'
    ''')

    # (9) 특정 지역의 모든 고객 삭제
    cursor.execute('''
        DELETE FROM customers
        WHERE state = 'CA'
    ''')

    # (10) 특정 카테고리의 모든 제품 삭제
    cursor.execute('''
        DELETE FROM products
        WHERE productLine = 'Planes'
    ''')

    # 변경사항 커밋
    conn.commit()

    # 데이터를 조회하여 출력
    def print_query_results(query):
        cursor.execute(query)
        rows = cursor.fetchall()
        for row in rows:
            print(row)

    # 데이터 조회
    print("Customers:")
    print_query_results("SELECT * FROM customers")

    print("\nProducts:")
    print_query_results("SELECT * FROM products")

    print("\nEmployees (Name and Job Title):")
    print_query_results("SELECT firstName, lastName, jobTitle FROM employees")

    print("\nOffices (Location):")
    print_query_results("SELECT city, addressLine1, addressLine2, state, postalCode FROM offices")

    print("\nRecent 10 Orders:")
    print_query_results("SELECT * FROM orders ORDER BY orderDate DESC LIMIT 10")

    print(f"\nOrder Details for Order Number {order_number}:")
    print_query_results(f"SELECT * FROM orderdetails WHERE orderNumber = {order_number}")

    print(f"\nPayments for Customer Number {customer_number}:")
    print_query_results(f"SELECT * FROM payments WHERE customerNumber = {customer_number}")

    print("\nProduct Lines:")
    print_query_results("SELECT productLine, textDescription FROM productlines")

    print(f"\nCustomers in {region}:")
    print_query_results(f"SELECT * FROM customers WHERE state = '{region}'")

    print(f"\nProducts priced between {min_price} and {max_price}:")
    print_query_results(f"SELECT * FROM products WHERE buyPrice BETWEEN {min_price} AND {max_price}")

    # 연결 종료
    conn.close()

if __name__ == '__main__':
    initialize_database()
