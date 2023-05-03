from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep

restaurante = str(input("Informe o nome do restaurante a ser pesquisado: "))

browser = webdriver.Chrome()
browser.get(f"https://www.tripadvisor.com.br/Search?q={restaurante}")

# Sleep é necessário para carregar o DOM
sleep(5)
browser.find_element(By.ID, "onetrust-accept-btn-handler").click()

sleep(3)
browser.find_element(By.XPATH, "/html/body/div[8]/div[1]/div/div[2]/div/div/div/div/div/ul/li[4]/a").click()

# Retorna os nomes dos restaurantes
sleep(4)
names = browser.find_elements(By.XPATH, "//div[contains(@class, 'result-title')]")
for name in names:
    print(name.text)

browser.close()