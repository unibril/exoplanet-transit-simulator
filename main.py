import mysql.connector
from db import database_connection
from animate import animate_planet
from fetch import fetch_planet_data


conn = database_connection()
cursor = conn.cursor(buffered=True)

cursor.execute("USE space_theme")
cursor.execute("SELECT COUNT(*) FROM PLANETS")
count = cursor.fetchone()[0]

if count == 0:
    print("Database empty, fetching planets from NASA...")
    fetch_planet_data()

planet_name = input("Enter the name of the planet: ")
cursor.execute("SELECT * FROM PLANETS WHERE planet_name = %s", (planet_name,))
result = cursor.fetchone()
if result:
    print(f"Planet: {result[1]}")
    print(f"Size of the planet: {result[2]}")
    print(f"Size of the sun: {result[3]}")
    print(f"Semi-major axis: {result[4]}")
    print(f"Time of orbit: {result[5]}")    
    animate_planet(result[1], result[2], result[3], result[4], result[5])
else:
    print("Planet not found in the database.")


