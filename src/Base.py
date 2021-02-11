import datetime

from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager


class base_Inicia_Chrome:
    def __init__(self):
        #self.driver_path = 'C:\\Users\\lerron.jesus\\OneDrive - Instituto Triad de Pesquisa e Desenvolvimento\\QA\\Recompra\\tester-recompracadastro\\src\\references\\driver\\chromedriver'
        #self.chrome = webdriver.Chrome(self.driver_path, options=self.options)

        self.chrome_options = Options()
        self.chrome_options.add_argument("--no-sandbox")
        self.chrome_options.add_argument("--disable-dev-shm-usage")
        self.chrome_options.set_headless()
        self.chrome = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=self.chrome_options)


class base_Usuario_Senha():
    def dados(self):
        usuario = 'consultorseminovos@automation.com'
        senha = 'root'

        return usuario, senha


class base_Abrir_Sessao:

    def Abrir(self):
        web = base_Inicia_Chrome()
        web.chrome.get('https://www2.recompra.com.br/#/pages/login')
        base_Faz_Login.faz_login(web)
        sleep(2)
        return web


class base_Faz_Login:

    def faz_login(self):
        input_login = self.chrome.find_element_by_name('username')
        input_senha = self.chrome.find_element_by_name('password')
        btn_login = self.chrome.find_element_by_css_selector(
            'body > app-root > app-pages > app-login > div > div.login-card > mat-card > form > div > div > button')

        result = base_Usuario_Senha.dados(self)
        input_login.send_keys(result[0])
        input_senha.send_keys(result[1])
        btn_login.click()


class base_Faz_Logout:

    def faz_logout(self):
        btn_config = self.chrome.find_element_by_css_selector(
            'body > app-root > app-navigation > div > mat-sidenav-container > mat-sidenav-content > mat-toolbar > button')
        btn_config.click()
        sleep(2)
        btn_sair = self.chrome.find_element_by_css_selector('#mat-menu-panel-0 > div > button:nth-child(4)')
        btn_sair.click()
        sleep(2)
        btn_sair = self.chrome.find_element_by_css_selector('#check-modal > div.modal-box > div.modal-footer > button')
        btn_sair.click()


