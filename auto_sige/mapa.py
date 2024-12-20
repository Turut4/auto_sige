from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import pandas as pd
import time

from auto_sige.utils import click_element, select_option, select_serie, select_turma


def mapa_form(driver, turma: str, grade: int):

    WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located(
            (By.TAG_NAME, 'select'))
    )
    if grade == 1:
        select_option(driver.find_element(By.NAME, 'cmbComposicao'), 1)
    if grade == 2:
        select_option(driver.find_element(By.NAME, 'cmbComposicao'), 2)

    time.sleep(4)
    select_serie(driver.find_element(By.NAME, 'cmbSerie'), turma)
    WebDriverWait(driver, 10).until(
        EC.staleness_of(driver.find_element(By.NAME, 'cmbTurma'))
    )
    time.sleep(4)
    select_option(driver.find_element(By.NAME, 'cmbTurno'), 2)
    WebDriverWait(driver, 10).until(
        EC.staleness_of(driver.find_element(By.NAME, 'cmbTurma'))
    )
    time.sleep(4)
    select_turma(driver.find_element(By.NAME, 'cmbTurma'), turma.upper())
    WebDriverWait(driver, 10).until(
        EC.staleness_of(driver.find_element(By.NAME, 'cmbTurma'))
    )
    time.sleep(2)

    select_option(driver.find_element(By.NAME, 'cmbBimestre'), 3)
    click_element(driver, By.NAME, 'cmdGerar')


def copy_data(driver, turma, output_csv_path=None):
    xpath_mappings = {
        '6': ('/html/body/table[6]/tbody/tr[5]', '/html/body/table[6]/tbody/tr[6]'),
        '7': ('/html/body/table[3]/tbody/tr[35]', '/html/body/table[3]/tbody/tr[36]'),
        '8': ('/html/body/table[6]/tbody/tr[10]', '/html/body/table[6]/tbody/tr[11]'),
        '9A': ('/html/body/table[3]/tbody/tr[34]', '/html/body/table[3]/tbody/tr[35]'),
        '9B': ('/html/body/table[3]/tbody/tr[37]', '/html/body/table[3]/tbody/tr[38]'),
        '1A': ('/html/body/table[3]/tbody/tr[37]', '/html/body/table[3]/tbody/tr[38]'),
        '1B': ('/html/body/table[3]/tbody/tr[36]', '/html/body/table[3]/tbody/tr[37]'),
        '2': ('/html/body/table[3]/tbody/tr[35]', '/html/body/table[3]/tbody/tr[36]'),
        '3A': ('/html/body/table[3]/tbody/tr[26]', '/html/body/table[3]/tbody/tr[27]'),
        '3B': ('/html/body/table[3]/tbody/tr[30]', '/html/body/table[3]/tbody/tr[31]')
    }

    print(f"Processando turma {turma}")

    selected_xpaths = None
    for key in xpath_mappings:
        if key in turma:
            selected_xpaths = xpath_mappings[key]
            break

    if not selected_xpaths:
        print(f"Turma {turma} não suportada ou XPath não definido.")
        return

    xpath, xxpath = selected_xpaths

    try:
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, xpath))
        )
    except Exception as e:
        print(f"Erro ao localizar a tabela para a turma {turma}: {e}")
        return

    # Matérias a serem extraídas
    materias = [
        "LÍNGUA PORTUGUESA", "MATEMÁTICA", "GEOGRAFIA", "HISTÓRIA",
        "EDUCAÇÃO FÍSICA", "ARTE", "ENSINO RELIGIOSO", "LÍNGUA INGLESA", "CIÊNCIAS DA NATUREZA"
    ]

    # Inicializa as listas de notas maiores e menores que 6
    notas_maiores = []
    notas_menores = []

    # Processa as notas >= 6
    try:
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, xpath))
        )
        row = driver.find_element(By.XPATH, xpath)
        notas_maiores = [
            cell.text.strip() for cell in row.find_elements(By.TAG_NAME, 'td')[1:]
        ][:len(materias)]
    except Exception as e:
        print(f"Erro ao processar notas >= 6: {e}")
        notas_maiores = [""] * len(materias)

    # Processa as notas < 6
    try:
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, xxpath))
        )
        row = driver.find_element(By.XPATH, xxpath)
        notas_menores = [
            cell.text.strip() for cell in row.find_elements(By.TAG_NAME, 'td')[1:]
        ][:len(materias)]
    except Exception as e:
        print(f"Erro ao processar notas < 6: {e}")
        notas_menores = [""] * len(materias)

    # Criação do DataFrame
    data = pd.DataFrame({
        "Matérias": materias,
        "Notas >= 6": notas_maiores,
        "Notas < 6": notas_menores
    })

    # Salva o DataFrame no CSV, se o caminho foi fornecido
    if output_csv_path:
        try:
            data.to_csv(output_csv_path, index=False, encoding='utf-8')
            print(f"Dados da turma {turma} salvos em {output_csv_path}")
        except Exception as e:
            print(f"Erro ao salvar CSV para a turma {turma}: {e}")

    return data
