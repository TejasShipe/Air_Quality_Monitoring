# src/insert_to_db.py

import mysql.connector

def insert_data(data):
    try:
        conn = mysql.connector.connect(
            host='localhost',
            user='root',        # 🔁 change this
            password='Sqlrunner_00',    # 🔁 change this
            database='smart_airquality_db'    # Make sure this DB exists
        )

        cur = conn.cursor()

        cur.execute('''
            CREATE TABLE IF NOT EXISTS air_quality (
                id INT AUTO_INCREMENT PRIMARY KEY,
                location VARCHAR(100),
                date DATE,
                pm25 FLOAT,
                pm10 FLOAT,
                co2 FLOAT,
                no2 FLOAT
            )
        ''')

        insert_query = '''
            INSERT INTO air_quality (location, date, pm25, pm10, co2, no2)
            VALUES (%s, %s, %s, %s, %s, %s)
        '''
        values = (
            data['location'], data['date'], data['pm25'],
            data['pm10'], data['co2'], data['no2']
        )

        cur.execute(insert_query, values)
        conn.commit()
        print("✅ Data inserted into MySQL database successfully.")

    except mysql.connector.Error as err:
        print("❌ Error:", err)

    finally:
        if conn.is_connected():
            cur.close()
            conn.close()
