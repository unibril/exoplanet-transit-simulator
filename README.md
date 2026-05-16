# 🪐 Exoplanet Transit Simulator

A Python simulation that fetches real exoplanet data from NASA's archive and generates a transit light curve — the same technique astronomers use to detect planets outside our solar system.

---

## What It Does

- Fetches real exoplanet data from the **NASA Exoplanet Archive**
- Stores it in **MySQL** for offline use
- Takes a planet name as input and simulates its **transit light curve** — the dip in starlight as the planet passes in front of its star
- Plots brightness vs time using **matplotlib**

---

## The Science

When an exoplanet transits (passes in front of) its star from our perspective, it blocks a fraction of the star's light. This causes a measurable dip in brightness:
Brightness drop = (planet radius)² / (star radius)²

The simulator calculates:
- **Transit duration** from orbital period and semi-major axis
- **Brightness during transit** using the radius ratio
- **Light curve** — brightness over a full orbital period

This is exactly how missions like Kepler and TESS discovered thousands of exoplanets.

---

## Project Structure
exoplanet-transit-simulator/
├── main.py      # Entry point, user input, database lookup
├── fetch.py     # Pulls exoplanet data from NASA API into MySQL
├── animate.py   # Calls physics and plots the light curve
├── physics.py   # Light curve math using numpy
└── db.py        # MySQL connection

---

## Usage

```bash
python main.py
```

On first run, fetches 10 exoplanets from NASA automatically. Then:
Enter the name of the planet: Kepler-22 b

Outputs planet details and renders the transit light curve plot.

---

## Setup

### Prerequisites

- Python 3.8+
- MySQL running locally

### Install dependencies

```bash
pip install requests numpy matplotlib mysql-connector-python
```

### Database setup

Create the database and table in MySQL:

```sql
CREATE DATABASE space_theme;
USE space_theme;
CREATE TABLE PLANETS (
    id INT AUTO_INCREMENT PRIMARY KEY,
    planet_name VARCHAR(100),
    size_planet FLOAT,
    size_sun FLOAT,
    semi_major_axis FLOAT,
    time_orbit FLOAT
);
```

Update credentials in `db.py` and `fetch.py` if your MySQL password is set.

---

## Data Source

[NASA Exoplanet Archive TAP Service](https://exoplanetarchive.ipac.caltech.edu/)

Fetches: planet radius, star radius, orbital period, semi-major axis.

---

## Requirements
requests
numpy
matplotlib
mysql-connector-python

---

## About

Built as part of a Python and astronomy portfolio. Uses real NASA data and simplified transit photometry physics to simulate one of the most important planet-detection methods in modern astronomy.
