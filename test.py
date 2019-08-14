import requests

# IR A LA PAGINA PRINCIPAL DE IBM CLOUD
# BUSCAR EL SERVICIO DE WATSON MACHINE LEARNING
# IR LA PESTAÑA CREDENCIALES Y EN LAS CREDENCIALES DE NUESTRO SERVICIO OBTENER:
# apikey y instance_id y sustituir aqui abajo

apikey = ''
instance_id = ''
scoring_endpoint = ''

# Get an IAM token from IBM Cloud
url     = "https://iam.bluemix.net/oidc/token"
headers = { "Content-Type" : "application/x-www-form-urlencoded" }
data    = "apikey=" + apikey + "&grant_type=urn:ibm:params:oauth:grant-type:apikey"
IBM_cloud_IAM_uid = "bx"
IBM_cloud_IAM_pwd = "bx"
response  = requests.post( url, headers=headers, data=data, auth=( IBM_cloud_IAM_uid, IBM_cloud_IAM_pwd ) )
iam_token = response.json()["access_token"]

import urllib3, requests, json

# NOTE: generate iam_token and retrieve ml_instance_id based on provided documentation
header = {'Content-Type': 'application/json', 'Authorization': 'Bearer ' + iam_token, 'ML-Instance-ID': instance_id}

# NOTE: manually define and pass the array(s) of values to be scored in the next line
payload_scoring = {
  "input_data":
  [
    {
      "fields":
      [
        "1",
        "2",
        "3",
        "4",
        "5",
        "6",
        "7",
        "8",
        "9",
        "10",
        "11",
        "12",
        "13",
        "14",
        "15",
        "16",
        "17",
        "18",
        "19",
        "20",
        "21",
        "22",
        "23",
        "24",
        "25",
        "26"
      ],
      "values":
      [
        [4,5,2,4,4,5,3,5,4,2,2,2,4,3,4,4,5,3,4,5,3,3,4,5,2,5],
        [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,3,1,1,1,1]
      ]
    }
  ]
}


response_scoring = requests.post(scoring_endpoint, json=payload_scoring, headers=header)
print("Resultados: ")
print (json.loads(response_scoring.text))
