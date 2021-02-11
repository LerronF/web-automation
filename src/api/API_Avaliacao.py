import requests

from src.api.API_Autenticacao import API_Autenticacao

class API_Avaliacoes():
    def Avaliacoes_FindAll(self):

        token = API_Autenticacao.Token(self)
        headers = {'Content-Type': 'application/json', 'X-Auth-Token': '{}'.format(token)}
        resp = requests.get('https://api2.recompra.com.br/avaliacoes', headers=headers)

        if resp.status_code != 200:
            return(resp.status_code)
        elif resp.status_code == 200:
            return(resp.json())

    def Avaliacoes_Veiculo(self):

        token = API_Autenticacao.Token(self)
        headers = {'Content-Type': 'application/json', 'X-Auth-Token': '{}'.format(token)}
        resp = requests.get('https://api2.recompra.com.br/avaliacoes', headers=headers)

        if resp.status_code != 200:
            return(resp.status_code)
        elif resp.status_code == 200:
            return(resp.json())