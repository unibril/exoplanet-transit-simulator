import matplotlib.pyplot as plt
import numpy as np
from physics import light_curve
import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",    
)

cursor = conn.cursor()
cursor.execute("USE space_theme")
cursor.execute("SELECT planet_name, size_planet, size_sun, semi_major_axis, time_orbit FROM PLANETS")
planets = cursor.fetchone()
planet_name, size_planet, size_sun, semi_major_axis, time_orbit = planets
print(f"Planet: {planet_name}, Size of Planet: {size_planet}, Size of Sun: {size_sun}, Semi-Major Axis: {semi_major_axis}, Time of Orbit: {time_orbit}")

times, brightness = light_curve(size_planet, size_sun, time_orbit, semi_major_axis)

plt.plot(times, brightness)
plt.xlabel("Time (days)")
plt.ylabel("Brightness")
plt.title(f"Transit Light Curve - {planet_name}")
plt.show()