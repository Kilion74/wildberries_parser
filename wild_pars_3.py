import csv
import time

import bs4
import pyautogui
from selenium import webdriver  # pip install selenium
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager  # pip install webdriver-manager

chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument(
#     'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36')
chrome_options.add_argument("--disable-blink-features=AutomationControlled")

count = 1
while count <= 15:
    with webdriver.Chrome(service=Service(ChromeDriverManager().install()),
                          options=chrome_options) as driver:  # Открываем хром
        driver.get(
            f"https://www.wildberries.ru/catalog/dom/spalnya/mebel?sort=popular&page={count}"
            "")  # Открываем страницу)  # Открываем страницу
        pyautogui.moveTo(300, 230, duration=0.25)
        pyautogui.middleClick()
        pyautogui.move(0, 200, duration=0.25)
        # time.sleep(7)
        time.sleep(3)  # Время на прогрузку страницы
        soup = bs4.BeautifulSoup(driver.page_source, 'html.parser')
        heads = soup.find_all('div', class_='product-card__wrapper')
        time.sleep(3)
        print(len(heads))
        for i in heads:
            w = i.find_next('a').get('href')
            print(w)
            with webdriver.Chrome(service=Service(ChromeDriverManager().install()),
                                  options=chrome_options) as driver:  # Открываем хром
                driver.get(w)  # Открываем страницу
                time.sleep(5)  # Время на прогрузку страницы
                loom = bs4.BeautifulSoup(driver.page_source, 'html.parser')
                head = loom.find('div', class_='product-page__header')
                print(head.text.strip())
                name = (head.text.strip())
                try:
                    cena = loom.find('div', class_='price-block__price-group').find('span',
                                                                                    class_='price-block__price').find(
                        'span')
                    print(cena.text.strip())
                    price = (cena.text.strip())
                except:
                    print('None')
                    price = 'None'
                try:
                    old_cena = loom.find('div', class_='price-block__price-group').find('span',
                                                                                        class_='price-block__price').find(
                        'ins', class_='price-block__final-price wallet')
                    print(old_cena.text.strip())
                    old_price = (old_cena.text.strip())
                except:
                    print('None')
                    old_price = 'None'
                pixx = loom.find('div', class_='zoom-image-container').find('img').get('src')
                print(pixx)
                params = loom.find('table', class_='product-params__table').find_all('tr')
                param_key_1 = (params[0].find_next('th').text.strip())
                param_value_1 = (params[0].find_next('td').text.strip())
                print(param_key_1 + ': ' + param_value_1)
                charact_1 = (param_key_1 + ': ' + param_value_1)
                try:
                    param_key_2 = (params[1].find_next('th').text.strip())
                    param_value_2 = (params[1].find_next('td').text.strip())
                    print(param_key_2 + ': ' + param_value_2)
                    charact_2 = (param_key_2 + ': ' + param_value_2)
                except:
                    charact_2 = 'None'
                    print('None')
                try:
                    param_key_3 = (params[2].find_next('th').text.strip())
                    param_value_3 = (params[2].find_next('td').text.strip())
                    print(param_key_3 + ': ' + param_value_3)
                    charact_3 = (param_key_3 + ': ' + param_value_3)
                except:
                    charact_3 = 'None'
                    print('None')
                try:
                    param_key_4 = (params[3].find_next('th').text.strip())
                    param_value_4 = (params[3].find_next('td').text.strip())
                    print(param_key_4 + ': ' + param_value_4)
                    charact_4 = (param_key_4 + ': ' + param_value_4)

                except:
                    charact_4 = 'None'
                    print('None')
                try:
                    param_key_5 = (params[4].find_next('th').text.strip())
                    param_value_5 = (params[4].find_next('td').text.strip())
                    print(param_key_5 + ': ' + param_value_5)
                    charact_5 = (param_key_5 + ': ' + param_value_5)

                except:
                    charact_5 = 'None'
                    print('None')
                try:
                    param_key_6 = (params[5].find_next('th').text.strip())
                    param_value_6 = (params[5].find_next('td').text.strip())
                    print(param_key_6 + ': ' + param_value_6)
                    charact_6 = (param_key_6 + ': ' + param_value_6)

                except:
                    charact_6 = 'None'
                    print('None')
                print('\n')
                storage = {'name': name, 'cena': price, 'old_cena': old_price, 'param_1': charact_1,
                           'param_2': charact_2,
                           'param_3': charact_3, 'param_4': charact_4, 'param_5': charact_5, 'param_6': charact_6,
                           'pix': pixx, 'url': w}
                fields = ['Name', 'price', 'old_price', 'Param_1', 'Param_2', 'Param_3', 'Param_4', 'Param_5',
                          'Param_6', 'Photo',
                          'Url']
                with open('spalnya.csv', 'a+', encoding='utf-16') as file:
                    pisar = csv.writer(file, delimiter='$', lineterminator="\r")
                    # Проверяем, находится ли файл в начале и пуст ли
                    file.seek(0)
                    if len(file.read()) == 0:
                        pisar.writerow(fields)  # Записываем заголовки, только если файл пуст

                    pisar.writerow(
                        [storage['name'], storage['cena'], storage['old_cena'], storage['param_1'], storage['param_2'],
                         storage['param_3'], storage['param_4'], storage['param_5'], storage['param_6'], storage['pix'],
                         storage['url']])
    count += 1
    print(count)
