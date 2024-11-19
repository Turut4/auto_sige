from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import pandas as pd
import time

from auto_sige.utils import click_element, select_option, select_serie, select_turma


def mapa_form(driver, turma, index):
    WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.TAG_NAME, 'select'))
    )
    select_option(driver.find_element(By.NAME, 'cmbComposicao'), 1)
    time.sleep(1)
    select_serie(driver.find_element(By.NAME, 'cmbSerie'), turma)
    time.sleep(1)
    select_option(driver.find_element(By.NAME, 'cmbTurno'), 2)
    time.sleep(1)
    select_turma(driver.find_element(By.NAME, 'cmbTurma'), turma.upper())
    time.sleep(10)
    select_option(driver.find_element(By.NAME, 'cmbBimestre'), 3)
    time.sleep(1)
    click_element(driver, By.NAME, 'cmdGerar')


def copy_data(driver, turma, output_csv_path):
    xpath_mappings = {
        '6': ('/html/body/table[6]/tbody/tr[5]', '/html/body/table[6]/tbody/tr[6]'),
        '7': ('/html/body/table[3]/tbody/tr[35]', '/html/body/table[6]/tbody/tr[36]'),
        '8': ('/html/body/table[4]/tbody/tr[20]', '/html/body/table[4]/tbody/tr[21]')
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

    rows = {
        "Qtd. de Notas Maiores ou Iguais a Média 6,0": xpath,
        "Qtd. de Notas Menores que a Média 6,0": xxpath
    }

    data_dict = {key: [] for key in rows.keys()}

    for key, xpath in rows.items():
        try:
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, xpath))
            )
            row = driver.find_element(By.XPATH, xpath)
            for cell in row.find_elements(By.TAG_NAME, 'td'):
                text = cell.text.strip()
                if text and text != key:
                    data_dict[key].append(text)
        except Exception as e:
            print(f"Erro ao processar a linha '{key}': {e}")

    max_length = max(len(v) for v in data_dict.values())
    for key in data_dict:
        data_dict[key].extend([""] * (max_length - len(data_dict[key])))

    data = pd.DataFrame(data_dict)

    if output_csv_path:
        try:
            data.to_csv(output_csv_path, index=False, encoding='utf-8')
            print(f"Dados da turma {turma} salvos em {output_csv_path}")
        except Exception as e:
            print(f"Erro ao salvar CSV para a turma {turma}: {e}")