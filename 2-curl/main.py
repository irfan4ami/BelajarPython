import requests
import json
 
url = "https://irfan.iproute.my.id/asu.php" #req 200
url = "https://gitburn.my.id/asjsh"         #req != 200
response = requests.get(url)

if response.status_code == 200:
   data = response.json()
   firstname = data["firstname"]
   print(f"firstname: {firstname}")
if response.status_code != 200:
   print(f"GAGAL REQUEST : {response.status_code}")





#print(response.text)
