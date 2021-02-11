import requests

from src.api.API_Autenticacao import API_Autenticacao

class API_Clientes():
    def Cliente_Documento(self, cpf):

        token = API_Autenticacao.Token(self)
        headers = {'Content-Type': 'application/json', 'X-Auth-Token': '{}'.format(token)}
        resp = requests.get('https://api2.recompra.com.br/clientes/documento/' + cpf, headers=headers)

        if resp.status_code != 200:
            return False
        elif resp.status_code == 200:
            return True