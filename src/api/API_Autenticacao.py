import requests

from src.Base import *

class API_Autenticacao:

    def Token(self):
        url = "https://api2.recompra.com.br/security/authentication/login"
        result = base_Usuario_Senha.dados(self)
        usuario = result[0]
        senha = result[1]

        payload = "{\r\n  \"senha\": \""+senha+"\",\r\n  \"usuario\": \""+usuario+"\"\r\n}"
        headers = {'Content-Type': 'application/json'}

        response = requests.request("POST", url, headers=headers, data=payload)
        data = response.headers

        return('{}'.format(data['X-Auth-Token']))
