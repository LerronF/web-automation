from src.api.API_Autenticacao import API_Autenticacao
import requests

class API_Veiculos:

    def Consulta_Placa(self, placa):

        token = API_Autenticacao.Token(self)
        headers = {'Content-Type': 'application/json', 'X-Auth-Token': '{}'.format(token)}
        resp = requests.get('https://api2.recompra.com.br/veiculos/placa/' + placa, headers=headers)

        if resp.status_code != 200:
            return (False, 'sem dados')
        elif resp.status_code == 200:
            return (True, resp.json())
