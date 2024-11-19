from selenium import webdriver
from auto_sige.settings import set_chrome_options, config
from auto_sige.utils import login, close_modal, navigate_to_documents
from auto_sige.data import data
from auto_sige.mapa import mapa_form, copy_data
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time


def main():
    options = set_chrome_options()
    driver = webdriver.Chrome(options=options)

    try:
        driver.get("https://sige.educacao.go.gov.br")
        print("Página carregada")

        WebDriverWait(driver, 10).until(
            EC.frame_to_be_available_and_switch_to_it((By.NAME, "mainFrame"))
        )

        login(driver)
        close_modal(driver)
        navigate_to_documents(driver)

        for index, turma in enumerate(data.turmas_fundamental, 0):
            try:
                print(f"Processando turma {turma} (índice {index})...")
                mapa_form(driver, turma, index)
                csv_path = f'./{turma}.csv'
                copy_data(driver, turma, csv_path)
                print(f"Dados da turma {turma} salvos em {csv_path}")
                driver.back()
                WebDriverWait(driver, 10).until(
                    EC.frame_to_be_available_and_switch_to_it(
                        (By.NAME, "mainFrame"))
                )
                driver.find_element(By.NAME, 'cmdLimpar').click()
                time.sleep(5)

            except Exception as e:
                print(f"Erro ao processar a turma {turma}: {str(e)}")

    except Exception as e:
        print(f"Erro: {e}")
    finally:
        input()
        driver.quit()
        print("Fechando o navegador...")


if __name__ == "__main__":
    main()
