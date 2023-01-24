from selenium import webdriver #selenium-4.8.0
from selenium.webdriver.common.by import By
from time import sleep


class Sharepoint_Bot:
    def __init__(self, user, password):
        self.driver = webdriver.Firefox()
        self.driver.get('https://valeccontrucoes.sharepoint.com/:x:/r/sites/TM-SUROD/')
        sleep(2)
        self.driver.find_element(By.ID, 'i0116').send_keys(user)
        sleep(2)
        self.driver.find_element(By.ID, 'idSIButton9').click()
        sleep(2)
        self.driver.find_element(By.ID, 'i0118').send_keys(password)
        sleep(2)
        self.driver.find_element(By.ID, 'idSIButton9').click()
        sleep(2)
        self.driver.find_element(By.ID, 'idSIButton9').click()
        sleep(2)
        self.driver.get('https://valeccontrucoes.sharepoint.com/sites/TM-SUROD/Documentos%20Compartilhados/Forms/AllItems.aspx?id=%2Fsites%2FTM%2DSUROD%2FDocumentos%20Compartilhados%2F06%2E%20Cronogramas%20consultorias&viewid=cac02269%2D6e4e%2D475d%2Da7d3%2De301992b458e')
        sleep(2)
        self.driver.find_element(By.NAME, 'Editar no modo de exibição de grade').click()
        sleep(2)
        self.driver.find_element(By.XPATH, '/html/body/div[1]/div/div[2]/div[1]/div[2]/div[3]/div/div[2]/div[2]/div[2]/div[2]/div[1]/div/div/div/div/div/div[3]/div/div/table/tbody/tr/td/div[2]/div[3]/div[1]/div[1]/table[2]/tbody/tr[5]/td[1]/div[1]').click()
        sleep(2)
        self.driver.find_element(By.XPATH, '/html/body/div[1]/div/div[2]/div[1]/div[2]/div[3]/div/div[2]/div[2]/div[2]/div[1]/div/div/div/div/div/div/div[1]/div[5]/button').click()
        sleep(2)
        self.driver.find_element(By.NAME, 'Baixar').click()
        print('Rodou')
        sleep(20)
        self.driver.quit()

f = open('_.txt', 'r', encoding='UTF-8')
_ = 0
for i in f:
    if _==0:
        user = i
    elif _==1:
        password = i
    _+=1

Sharepoint_Bot(user, password)
