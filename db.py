import mysql.connector
def database_connection():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",    
    )   
    cursor = conn.cursor()
    cursor.execute("CREATE DATABASE IF NOT EXISTS space_theme")
    cursor.execute("USE space_theme")
    cursor.execute("""CREATE TABLE IF NOT EXISTS PLANETS(
                id INT AUTO_INCREMENT PRIMARY KEY,
                planet_name VARCHAR(255),
                size_planet float,
                size_sun float,
                semi_major_axis float,
                time_orbit float
    )""")
    return conn

