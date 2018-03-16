import requests,json
a =  555
api = f'https://api-center.000webhostapp.com/api/apistore_binchecker.php?bin={a}'

k = requests.get(api)
print(json.loads(k.text))
