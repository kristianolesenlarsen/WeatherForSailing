import requests
from bs4 import BeautifulSoup


resp = requests.get("http://web.econ.ku.dk/polit/studerende/eksamen/opgrv/cms-ku/dansk.asp?del=3%E5r&fag_id=187&fagnavn=Mikro%F8konomi%20III").content
soup = BeautifulSoup(resp, "html5lib")

requests.findall
