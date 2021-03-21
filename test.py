import requests

requests.post('http://localhost:5000/alert',
            json={"firstname":"Sefa", "lastname":"Aydinelli"})