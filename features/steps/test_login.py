import unittest

from src.Base import *
from src.pages.login.LoginPage import Login
from time import sleep
#from pytest_bdd import scenario, given, when, then
from behave import given, when, then


class test_cenarios_validacao_login(unittest.TestCase):
    @given("que entrei na pagina do Recompra")
    def test_Abrir_Pagina(self):
        web = base_Inicia_Chrome()
        web.chrome.get('https://www2.recompra.com.br/#/pages/login')
        web.chrome.close()


    @when("adicionar os dados de usuario")
    def test_add_dados_usuario(self):
        web = base_Inicia_Chrome()
        web.chrome.get('https://www2.recompra.com.br/#/pages/login')
        Login.email(web,'vendedor4@anne.com')
        Login.senha(web,'roo')
        web.chrome.close()


    @then("realiza o login e entra na pagina")
    def test_login_entra_pagina(self):
        web = base_Inicia_Chrome()
        web.chrome.get('https://www2.recompra.com.br/#/pages/login')
        Login.email(web, 'vendedor4@anne.com')
        Login.senha(web, 'root')
        Login.click_entrar(web)
        web.chrome.close()

    @then("realiza o login e a senha é inválida")
    def test_login_senha_invalida(self):
        web = base_Inicia_Chrome()
        web.chrome.get('https://www2.recompra.com.br/#/pages/login')
        Login.email(web, 'vendedor4@anne.com')
        Login.senha(web, 'roo')
        Login.click_entrar(web)
        sleep(2)
        texto = Login.texto(web)
        assert texto == 'Usuário ou senha inválidos'
        web.chrome.close()

    @then("realiza o login e o perfil do usuario nao tem acesso")
    def test_perfil_sem_permissao(self):
        web = base_Inicia_Chrome()
        web.chrome.get('https://www2.recompra.com.br/#/pages/login')
        Login.email(web, 'benny@gmail.com')
        Login.senha(web, 'root')
        Login.click_entrar(web)
        sleep(2)
        texto = Login.texto(web)
        assert texto == 'Seu perfil não possui acesso neste módulo.'
        web.chrome.close()



if __name__ == '__main__':
    unittest.main()
    #unittest.main(test_autenticacao_Invalida())
    #unittest.main(test_User_Lojista_Pendente_Aprovacao())
    #unittest.main(test_User_Lojista())
