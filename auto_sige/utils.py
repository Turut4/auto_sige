from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from auto_sige.settings import cpf, password
from auto_sige import data


def fill_input_field(driver, by, element, value):
    input_field = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((by, element))
    )
    input_field.clear()
    input_field.send_keys(value)


def click_element(driver, by, element):
    element_to_click = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((by, element))
    )
    element_to_click.click()


def login(driver):
    fill_input_field(driver, By.NAME, 'txtCPF', cpf)
    fill_input_field(driver, By.NAME, 'txtSenha', password)

    click_element(driver, By.ID, 'cmdOK')


def close_modal(driver):
    try:
        click_element(driver, By.CLASS_NAME, 'close-modal')
    except Exception:
        print("Modal não encontrado ou já fechado.")


def navigate_to_documents(driver):
    from selenium.webdriver.common.action_chains import ActionChains
    actions = ActionChains(driver)

    documentos_btn = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, 'documentos'))
    )

    relatiorios_btn = driver.find_element(
        By.XPATH, '//*[@id="smoothmenu1"]/ul/li[4]/ul/li[2]')
    acomp_btn = driver.find_element(
        By.XPATH, '//*[@id="smoothmenu1"]/ul/li[4]/ul/li[2]/ul/li[3]')

    actions.move_to_element(documentos_btn).pause(1).move_to_element(
        relatiorios_btn).pause(1).move_to_element(acomp_btn).click().perform()

    click_element(driver, By.XPATH,
                  '//*[@id="smoothmenu1"]/ul/li[4]/ul/li[2]/ul/li[3]/ul/li[1]')


def select_option(select, option: int):
    options = select.find_elements(By.TAG_NAME, 'option')
    options[option].click()


def select_turma(select, turma):
    options = select.find_elements(By.TAG_NAME, 'option')
    for i in range(len(options)):
        print(options[i].text)
        if (options[i].text in data.turmas_fundamental or options[i].text in data.turmas_medio) and options[i].text == turma:
            options[i].click()


def select_serie(select, turma):
    options = select.find_elements(By.TAG_NAME, 'option')

    if "6" in turma:
        options[5].click()
    if "7" in turma:
        options[6].click()
    if "8" in turma:
        options[7].click()
    if "9" in turma:
        options[8].click()
