from physics import light_curve
import matplotlib.pyplot as plt
def animate_planet(planet_name, size_planet, size_sun, semi_major_axis, time_orbit):
    times, brightness = light_curve(size_planet, size_sun, time_orbit, semi_major_axis)
    plt.plot(times, brightness)
    plt.xlabel("Time (days)")
    plt.ylabel("Brightness")
    plt.title(f"Transit Light Curve - {planet_name}")
    plt.show()