class Login:

    def email(self, email):
        input_login = self.chrome.find_element_by_name('username')
        input_login.send_keys(email)

    def senha(self, senha):
        input_senha = self.chrome.find_element_by_name('password')
        input_senha.send_keys(senha)

    def click_entrar(self):
        btn_login = self.chrome.find_element_by_css_selector('body > app-root > app-pages > app-login > div > '
                                                             'div.login-card > mat-card > form > div > div > button')
        btn_login.click()

    def texto(self):
        return self.chrome.find_element_by_class_name('alert').text
