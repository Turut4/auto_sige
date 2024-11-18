from selenium import webdriver
from auto_sige import config
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options


def main():
    options = Options()
    options.add_argument(
        "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option("useAutomationExtension", False)

    driver = webdriver.Chrome(options=options)

    try:
        login(driver)

    except Exception as e:
        print("erro: ", e)
    finally:
        input()

        driver.quit()
        print("fechando...")


def login(driver: webdriver.Chrome):
    driver.get("https://sige.educacao.go.gov.br")
    print(driver.page_source)

    WebDriverWait(driver, 10).until(
        EC.frame_to_be_available_and_switch_to_it((By.NAME, "mainFrame"))
    )

    cpf_field = driver.find_element(By.ID, 'txtCPF')
    cpf_field.send_keys(config.username)

    pass_field = driver.find_element(By.ID, 'txtSenha')
    pass_field.send_keys(config.password)

    ok_button = driver.find_element(By.ID, 'cmdOK')
    ok_button.click()


if __name__ == "__main__":
    main()
