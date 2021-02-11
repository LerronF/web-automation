import unittest

from src.Base import *
from src.pages.login.LoginPage import Login
from time import sleep


class test_autenticacao_Invalida(unittest.TestCase):

    def test(self):
        web = base_Inicia_Chrome()
        web.chrome.get('https://www2.recompra.com.br/#/pages/login')

        Login.email(web, 'vendedor4@anne.com')
        Login.senha(web, 'roo')
        Login.click_entrar(web)
        sleep(1)
        texto = Login.texto(web)

        self.assertEqual(texto, 'Usuário ou senha inválidos','Erro na validação da mensagem')

        web.chrome.close()

class test_User_Lojista_Pendente_Aprovacao(unittest.TestCase):

    def test(self):
        web = base_Inicia_Chrome()
        web.chrome.get('https://www2.recompra.com.br/#/pages/login')

        Login.email(web, 'benny@gmail.com')
        Login.senha(web, 'root')
        Login.click_entrar(web)
        sleep(1)
        texto = Login.texto(web)

        self.assertEqual(texto, 'Seu perfil não possui acesso neste módulo.', 'Erro na validação da mensagem')

        web.chrome.close()

class test_User_Lojista(unittest.TestCase):

    def test(self):
        web = base_Inicia_Chrome()
        web.chrome.get('https://www2.recompra.com.br/#/pages/login')

        Login.email(web, 'benny@gmail.com')
        Login.senha(web, 'root')
        Login.click_entrar(web)
        sleep(5)
        texto = Login.texto(web)

        self.assertEqual(texto, 'Seu perfil não possui acesso neste módulo.','Erro na validação da mensagem')

        web.chrome.close()


if __name__ == '__main__':
    unittest.main()
    #unittest.main(test_autenticacao_Invalida())
    #unittest.main(test_User_Lojista_Pendente_Aprovacao())
    #unittest.main(test_User_Lojista())



