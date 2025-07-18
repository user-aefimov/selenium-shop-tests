# test_items.py
# Copyright (c) 2025 Aleksey Efimov
# MIT License

import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_add_to_basket_button_is_present(browser, language):
    # Открываем страницу товара
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)
    
    # Ожидание загрузки страницы
    WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.TAG_NAME, "body"))
    )

    # Для визуальной проверки языка (шаг 2 задания)
    time.sleep(3)  
    
    # Проверка языка интерфейса (дополнительная проверка)
    html_lang = browser.find_element(By.TAG_NAME, "html").get_attribute("lang")
    print(f"\nCurrent interface language: {html_lang}")
    assert html_lang == language, f"Язык интерфейса не совпадает: {html_lang} != {language}"


    # Проверяем наличие кнопки добавления в корзину с явным ожиданием
    add_button = WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "button.btn-add-to-basket"))
    )
    
    # Проверяем, что кнопка есть на странице
    print("Проверка, кнопка есть на странице!")
    assert add_button is not None, "Add to basket button is not found"
    assert add_button.is_displayed(), "Add to basket button is not visible"
    
    # Проверка текста кнопки ожидание/факт
    add_button_text = add_button.text.strip()
    
    expected_text = {
        "ru": "Добавить в корзину",
        "en-gb": "Add to basket",
        "es": "Añadir al carrito",
        "fr": "Ajouter au panier",
        "pt": "Adicionar ao carrinho",
        "it": "Aggiungi al carrello",
    }.get(language, "Unknown")
    print("Проверка текста кнопки ожидание/факт!")
    assert add_button_text == expected_text, f"Текст кнопки не соответствует языку: {add_button_text} != {expected_text}"

    # Дополнительно: выводим текст кнопки для отладки
    print(f"Button text: '{add_button.text}'")