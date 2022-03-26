import requests


logs = []

request = requests.get("http://3.137.141.78/")
data = request.json()

for item in data:
    logs.append(item["name"])

print(logs)
