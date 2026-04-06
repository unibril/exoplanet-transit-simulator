import numpy as np

def light_curve(planet_radius, star_radius, orbital_period, semi_major_axis):
    planet_radius_solar = planet_radius / 109
    times = np.linspace(0, orbital_period, 1000)
    brightness = np.ones_like(times)
    
    transit_duration = (star_radius / (semi_major_axis * 215)) * (orbital_period / np.pi)
    
    transit_start = orbital_period / 2 - transit_duration / 2
    transit_end = orbital_period / 2 + transit_duration / 2
    
    transit_brightness = 1 - (planet_radius_solar**2 / star_radius**2)

    brightness = np.where((times >= transit_start) & (times <= transit_end), transit_brightness, brightness)
    
    return times, brightness
    