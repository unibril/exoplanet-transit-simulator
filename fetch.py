import requests
import mysql.connector
def fetch_planet_data():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password=""
    )
    cursor = conn.cursor()
    cursor.execute("USE space_theme")

    url = "https://exoplanetarchive.ipac.caltech.edu/TAP/sync?query=SELECT+pl_name,pl_rade,st_rad,pl_orbsmax,pl_orbper+FROM+ps+WHERE+pl_rade+IS+NOT+NULL+AND+st_rad+IS+NOT+NULL+AND+pl_orbsmax+IS+NOT+NULL+AND+pl_orbper+IS+NOT+NULL+AND+rownum<=10&format=json"
    response = requests.get(url)
    data = response.json()

    for planet in data:
        name = planet['pl_name']
        size_planet = planet['pl_rade']
        size_sun = planet['st_rad']
        semi_major_axis = planet['pl_orbsmax']
        time_orbit = planet['pl_orbper']
        
        cursor.execute("INSERT INTO PLANETS (size_planet, size_sun, semi_major_axis, planet_name, time_orbit) VALUES (%s, %s, %s, %s, %s)", 
                    (size_planet, size_sun, semi_major_axis, name, time_orbit))
    conn.commit()