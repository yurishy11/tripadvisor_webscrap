from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep

restaurante = str(input("Informe o nome do restaurante a ser pesquisado: "))
print()

browser = webdriver.Chrome()
browser.get(f"https://www.tripadvisor.com.br/Search?q={restaurante}")

# Sleep é necessário para carregar o DOM
sleep(5)
browser.find_element(By.ID, "onetrust-accept-btn-handler").click()

sleep(3)
browser.find_element(By.XPATH, "/html/body/div[8]/div[1]/div/div[2]/div/div/div/div/div/ul/li[4]/a").click()

# Retorna os nomes dos restaurantes e o endereço e armazena
sleep(4)
restaurants_name = []
restaurants_addr = []
names = browser.find_elements(By.XPATH, "//div[contains(@class, 'result-title')]")
address = browser.find_elements(By.XPATH, "/html/body/div[2]/div/div[2]/div/div/div/div/div[1]/div/div[1]/div/div[3]/div/div[1]/div/div[2]/div/div/div[1]/div/div/div/div[2]/div[1]/div[3]")
for name in names:
    restaurants_name.append(name.text)

for addr in address:
    restaurants_addr.append(addr.text)

restaurants = dict.fromkeys(restaurants_name, restaurants_addr)
print(restaurants)

browser.close()