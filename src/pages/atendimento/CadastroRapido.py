from time import sleep


class Cadastro:

    def preencherCPF(self, cpf):
        input_cpf = self.chrome.find_element_by_id('cpfToInput')
        input_cpf.send_keys(cpf)

    def selecionarCPF(self):
        input_cpf = self.chrome.find_element_by_css_selector('#mat-option-148 > span')
        input_cpf.click()

    def notificacaoCPFError(self):
        return self.chrome.find_element_by_class_name('cpf-error').text

    def preencherNome(self, nome):
        input_nome = self.chrome.find_element_by_name('nome')
        input_nome.send_keys(nome)

    def preencherTelefone(self, telefone):
        input_telefone = self.chrome.find_element_by_name('telefone')
        input_telefone.send_keys(telefone)

    def preencherEmail(self, email):
        input_email = self.chrome.find_element_by_name('email')
        input_email.send_keys(email)

    def preencherVeiculoInteresse(self):
        list_veic = self.chrome.find_element_by_name("interesseToFind")
        list_veic.click()
        sleep(1)
        option = self.chrome.find_element_by_css_selector('#mat-option-46 > span')
        option.click()

    def preencherPlaca(self, placa):
        input_placa = self.chrome.find_element_by_id('plateToInput')
        input_placa.send_keys(placa)

    def preencherMarca(self):
        list_marca = self.chrome.find_element_by_name('marcaToFind')
        list_marca.click()
        sleep(150)
        option = self.chrome.find_element_by_css_selector('#mat-option-148 > span')
        option.click()

    def preencherModelo(self):
        list = self.chrome.find_element_by_name("modeloToFind")
        list.click()
        option = self.chrome.find_element_by_css_selector('#mat-option-239 > span')
        option.click()

    def preencherAnoFabricacao(self):
        list = self.chrome.find_element_by_name("ano_fabricacao")
        list.click()
        sleep(1)
        option = self.chrome.find_element_by_css_selector('#mat-option-242 > span')
        option.click()

    def preencherAnoModelo(self):
        list = self.chrome.find_element_by_name("ano_modelo")
        list.click()
        option = self.chrome.find_element_by_css_selector('#mat-option-245 > span')
        option.click()

    def preencherCor(self):
        list = self.chrome.find_element_by_name("cor")
        list.click()
        option = self.chrome.find_element_by_css_selector('#mat-option-10 > span')
        option.click()

    def preencherCombustivel(self):
        list = self.chrome.find_element_by_name("combustivel")
        list.click()
        option = self.chrome.find_element_by_css_selector('#mat-option-20 > span')
        option.click()

    def preencherCambio(self):
        list = self.chrome.find_element_by_name("cambio")
        list.click()
        option = self.chrome.find_element_by_css_selector('#mat-option-27 > span')
        option.click()

    def preencherPortas(self):
        list = self.chrome.find_element_by_name("portas")
        list.click()
        option = self.chrome.find_element_by_css_selector('#mat-option-30 > span')
        option.click()

    def preencherQuilometragem(self, quilometragem):
        input_quilometragem = self.chrome.find_element_by_name('quilometragem')
        input_quilometragem.send_keys(quilometragem)

    def preencherTipo(self):
        list = self.chrome.find_element_by_name("tipo")
        list.click()
        option = self.chrome.find_element_by_css_selector('#mat-option-33 > span')
        option.click()

    def preencherOrigem(self):
        list = self.chrome.find_element_by_name("origem")
        list.click()
        option = self.chrome.find_element_by_css_selector('#mat-option-42 > span')
        option.click()

    def preencherCategoria(self):
        list = self.chrome.find_element_by_name("categoria")
        list.click()
        option = self.chrome.find_element_by_css_selector('#mat-option-44 > span')
        option.click()

    def preencherChassi(self, chassi):
        input_chassi = self.chrome.find_element_by_name('chassi')
        input_chassi.send_keys(chassi)

    def preencherRenavam(self, renavam):
        input_renavam = self.chrome.find_element_by_name('renavam')
        input_renavam.send_keys(renavam)

    def clicarSalvarAvaliar(self):
        btn_salvar_avaliar = self.chrome.find_element_by_xpath(
            '/html/body/app-root/app-navigation/div/mat-sidenav-container/mat-sidenav-content/app-cadastro-rapido/form/div/div[1]/button[1]')
        btn_salvar_avaliar.click()

    def clicarSalvarAgendar(self):
        btn_salvar_agendar = self.chrome.find_element_by_xpath('/html/body/app-root/app-navigation/div/mat-sidenav-container/mat-sidenav-content/app-cadastro-rapido/form/div/div[1]/button[2]')
        btn_salvar_agendar.click()

    def clicarSalvar(self):
        btn_salvar = self.chrome.find_element_by_xpath('/html/body/app-root/app-navigation/div/mat-sidenav-container/mat-sidenav-content/app-cadastro-rapido/form/div/div[2]/button[1]')
        btn_salvar.click()