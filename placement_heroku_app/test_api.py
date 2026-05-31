import requests

url = "https://placement-ml-api-nynm.onrender.com/predict"
data = {"cgpa": 8.5, "iq": 120}

response = requests.post(url, json=data)
print(response.json())
