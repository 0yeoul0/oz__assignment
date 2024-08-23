import sqlite3

try:
    # SQLite 데이터베이스에 연결 (파일이 없으면 생성됨)
    conn = sqlite3.connect('example.db')
    cursor = conn.cursor()

    # 1. employees 테이블 생성
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS employees (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        position TEXT,
        salary REAL
    );
    """)

    # 2. 직원 데이터 추가 (executemany 사용)
    employees_data = [
        ('혜린', 'PM', 90000),
        ('은우', 'Frontend', 80000),
        ('가을', 'Backend', 92000),
        ('지수', 'Frontend', 78000),
        ('민혁', 'Frontend', 96000),
        ('하온', 'Backend', 130000)
    ]
    cursor.executemany("INSERT INTO employees (name, position, salary) VALUES (?, ?, ?)", employees_data)
    conn.commit()  # 데이터베이스 변경사항 저장

    # 3. 모든 직원의 이름과 연봉 정보 조회
    cursor.execute("SELECT name, salary FROM employees;")
    print("모든 직원의 이름과 연봉 정보:")
    for row in cursor.fetchall():
        print(f"Name: {row[0]}, Salary: {row[1]:,.2f}")

    # 4. Frontend 직책 중 연봉이 90000 이하인 직원의 이름과 연봉 조회
    cursor.execute("SELECT name, salary FROM employees WHERE position = 'Frontend' AND salary <= 90000;")
    print("\nFrontend (<=90000):")
    for row in cursor.fetchall():
        print(f"Name: {row[0]}, Salary: {row[1]:,.2f}")

    # 5. PM 직책을 가진 직원의 연봉을 10% 인상
    cursor.execute("UPDATE employees SET salary = salary * 1.10 WHERE position = 'PM';")
    conn.commit()

    # 인상된 연봉 확인
    cursor.execute("SELECT * FROM employees WHERE position = 'PM';")
    print("\nPM 직책의 인상된 연봉:")
    for row in cursor.fetchall():
        print(f"ID: {row[0]}, Name: {row[1]}, Position: {row[2]}, Salary: {row[3]:,.2f}")

    # 6. Backend 직책을 가진 직원의 연봉을 5% 인상
    cursor.execute("UPDATE employees SET salary = salary * 1.05 WHERE position = 'Backend';")
    conn.commit()

    # 7. 민혁 사원의 데이터 삭제
    cursor.execute("DELETE FROM employees WHERE name = '민혁';")
    conn.commit()

    # 8. 직책별로 그룹화하여 각 직책의 평균 연봉 계산
    cursor.execute("SELECT position, AVG(salary) AS avg_salary FROM employees GROUP BY position;")
    print("\n직책별 평균 연봉:")
    for row in cursor.fetchall():
        print(f"Position: {row[0]}, Average Salary: {row[1]:,.2f}")

    # 9. employees 테이블 삭제
    cursor.execute("DROP TABLE IF EXISTS employees;")
    conn.commit()

except sqlite3.Error as e:
    print(f"An error occurred: {e}")

finally:
    # 연결 닫기
    if cursor:
        cursor.close()
    if conn:
        conn.close()
