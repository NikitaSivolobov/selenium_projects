# selenium_projects_and_api_test
Данный проект содержит: UI автотесты на Python и Selenium Webdriver, тестовый framework pytest, с использованием паттерна Page Object.
Api автотесты на Python с библиотекой requests, pytest, с логгированием и подключенным allure отчётом.

[Переход в проект автотестов на Java](https://gitlab.com/NikitaSivolobov/javadifferenttests)

запуск Api тестов:

                       python -m pytest -s -v test_google_maps_api.py
запуск Api тестов с allure отчётом:

                       python -m pytest --alluredir=test_results/ test_google_maps_api.py
                             allure serve test_results/ 


