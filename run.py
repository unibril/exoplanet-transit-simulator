
import requests
import mysql.connector

url = "https://exoplanetarchive.ipac.caltech.edu/TAP/sync?query=SELECT+pl_name,pl_rade,st_rad,pl_orbsmax,pl_orbper+FROM+ps+WHERE+pl_rade+IS+NOT+NULL+AND+st_rad+IS+NOT+NULL+AND+pl_orbsmax+IS+NOT+NULL+AND+pl_orbper+IS+NOT+NULL+AND+rownum<=10&format=json"

response = requests.get(url)

data = response.json()

print(data[0])