# conftest.py
# Copyright (c) 2025 Aleksey Efimov
# MIT License

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default="chrome",
                     help="Choose browser: chrome or firefox")
    parser.addoption('--language', action='store', default='en-gb', 
                     help="Choose language: ru, en-gb, es, fr, etc.")

@pytest.fixture(scope="session")
def language(request):
    """Фикстура для получения языка из командной строки"""
    return request.config.getoption("language")

@pytest.fixture(scope="function")
def browser(request, language):
    browser_name = request.config.getoption("browser_name")
    user_language = language
    options = None
    browser = None
    
    if browser_name == "chrome":
        print("\nstart chrome browser for test..")
        options = ChromeOptions()
        options.add_argument(f"--lang={user_language}")
        options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
        service = ChromeService(ChromeDriverManager().install())
        browser = webdriver.Chrome(service=service, options=options)
        browser.maximize_window()

    elif browser_name == "firefox":
        print("\nstart firefox browser for test..")
        options = FirefoxOptions()
        options.set_preference("intl.accept_languages", user_language)
        service = FirefoxService(GeckoDriverManager().install())
        browser = webdriver.Firefox(service=service, options=options)
        browser.maximize_window()
        
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    
    yield browser
    print("\nquit browser..")
    browser.quit()