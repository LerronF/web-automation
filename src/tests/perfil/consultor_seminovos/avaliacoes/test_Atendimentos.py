import unittest

from src.Base import *
from src.pages.atendimento.CadastroRapido import Cadastro
from src.api.API_Autenticacao import API_Autenticacao
from src.api import API_Cliente
from src.api import API_Veiculo
from time import sleep


class test_Cadastro_Todos_Campos_Sucesso(unittest.TestCase):
    def test(self):
        web = base_Inicia_Chrome()
        web = base_Abrir_Sessao.Abrir(web)
        token = API_Autenticacao.Token(web)
        web.chrome.get('https://www2.recompra.com.br/#/dashboard/cadastro_rapido?token= {}'.format(token))
        sleep(1)

        Cadastro.preencherCPF(web, '85554871291')
        #Consulta API para verificar se o proprietario ja existe
        cliente = API_Cliente.Cliente_Documento(self, '85554871291')

        if not cliente:
            Cadastro.preencherNome(web,'LErron Felipe')
            Cadastro.preencherTelefone(web,'92982672065')
            Cadastro.preencherEmail(web,'lerron@lerron.com')
        elif cliente:
            Cadastro.selecionarCPF(web)

        Cadastro.preencherVeiculoInteresse(web)





        Cadastro.preencherPlaca(web, 'AAA-8765')
        sleep(2)
        Cadastro.preencherMarca(web)
        Cadastro.preencherModelo(web)
        Cadastro.preencherAnoFabricacao(web)
        Cadastro.preencherAnoModelo(web)
        Cadastro.preencherCor(web)
        Cadastro.preencherCombustivel(web)
        Cadastro.preencherCambio(web)
        Cadastro.preencherPortas(web)
        Cadastro.preencherQuilometragem(web,'500')
        Cadastro.preencherTipo(web)
        Cadastro.preencherOrigem(web)
        Cadastro.preencherCategoria(web)
        Cadastro.preencherChassi(web,'ABCDEFGHIJKLMNOPQ')
        Cadastro.preencherRenavam(web,'01234567890')
        Cadastro.clicarSalvar(web)

        texto = Cadastro.texto(web)
        self.assertEqual(texto,'Item salvo !','Erro no Cadastro rápido')

        sleep(2)
        web.chrome.close()


class test_Cadastro_Apenas_Campos_Obrigatorios(unittest.TestCase):
    def test(self):
        pass

class test_Dados_Repetidos(unittest.TestCase):
    def test(self):
        result = API_Veiculo.Consulta_Placa(self, 'AAA-8765')
        print(result)


if __name__ == '__main__':
    #unittest.main(test_Cadastro_Todos_Campos_Sucesso())
    unittest.main(test_Cadastro_Apenas_Campos_Obrigatorios())
    #unittest.main(test_Dados_Repetidos())
