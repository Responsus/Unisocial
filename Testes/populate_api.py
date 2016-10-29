import requests


try:
	req = requests.post("http://172.17.0.1/api/faculdade/",
			data={"nome":"Fatec","email":"fatec@fatec.com.br","cnpj":"1235","senha":"senha123"}
			)
	print req.text
except Exception as e:
	print e

try:
	req = requests.post("http://172.17.0.1/api/faculdade/1/unidades/",
			data={"nome":"Vila Mariana","endereco":"1235"}
			)
	print req.text
except Exception as e:
	print e

try:
	req = requests.post("http://172.17.0.1/api/faculdade/1/areas/",
			data={"nome":"Humanas"}
			)
	print req.text
	req = requests.post("http://172.17.0.1/api/faculdade/1/areas/",
			data={"nome":"Exatas"}
			)
	print req.text
	req = requests.post("http://172.17.0.1/api/faculdade/1/areas/",
			data={"nome":"Saude"}
			)
	print req.text
	req = requests.post("http://172.17.0.1/api/faculdade/1/areas/",
			data={"nome":"Direito"}
			)
	print req.text
except Exception as e:
	print e

try:
	req = requests.post("http://172.17.0.1/api/faculdade/1/tipos/",
			data={"nome":"Bacharel"}
			)
	print req.text
	req = requests.post("http://172.17.0.1/api/faculdade/1/tipos/",
			data={"nome":"Licenciatura"}
			)
	print req.text
	req = requests.post("http://172.17.0.1/api/faculdade/1/tipos/",
			data={"nome":"Extensao"}
			)
	print req.text
	req = requests.post("http://172.17.0.1/api/faculdade/1/tipos/",
			data={"nome":"Profissionalizante"}
			)
	print req.text
except Exception as e:
	print e
