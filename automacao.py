from selenium import webdriver  # importing just the webdriver from selenium
from selenium.webdriver.common.keys import Keys # importing Keys to use our press enter

navegador = webdriver.Chrome()  # here we are calling our browser
navegador.get('https://www.linkedin.com/')  # getting the web address
navegador.maximize_window()  # maximazing our browser window


def comecar():  # this function starts our script
    # find which element we want to, in this case email field
    escrever_email = navegador.find_element_by_xpath('//*[@id="session_key"]')
    escrever_email.send_keys('your_email')  # put your email here
    # find which element we want to, in this case password field
    escrever_senha = navegador.find_element_by_xpath(
        '//*[@id="session_password"]')
    escrever_senha.send_keys('your_password')  # put your password here
    # find which element we want to, in this case the button to sign in
    entrar = navegador.find_element_by_xpath(
        '//*[@id="main-content"]/section[1]/div/div/form/button')
    entrar.click()  # it clicks on enter to sign in


def minimizar_chat():  # this function minimize our chat
    minimizar = navegador.find_element_by_xpath(
        '//*[@id="msg-overlay"]/section/header')  # find the right element
    minimizar.click()  # it clicks on the element


def pesquisar_vagas():  # here we will find which jobs we would like to work
    pesquisar = navegador.find_element_by_xpath(
        '//*[@id="global-nav-typeahead"]/input')  # find the field search
    # here you need to write the jobs you're interested
    pesquisar.send_keys('')


def tecla_enter():  # and the last but not least, here we create an enter
    enter = navegador.find_element_by_xpath(
        '//*[@id="global-nav-typeahead"]/input')  # find the search field
    enter.send_keys(Keys.ENTER)  # and now we press enter


comecar()  # calling the function to start
minimizar_chat()  # calling the function to minimize our chat
pesquisar_vagas()  # calling the function to write the job
tecla_enter()  # calling the function to press enter