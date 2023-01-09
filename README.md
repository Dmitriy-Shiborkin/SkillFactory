Финальный проект для курса "Тестировщик - автоматизатор на Python"

Тестирование формы авторизации Личного кабинета Ростелеком https://b2c.passport.rt.ru

Ссылка на тест-кейсы, баг-репорты: https://docs.google.com/spreadsheets/d/1Vl7Fryd6VAdqf3odBWpSgeLT8HOlGpMs/edit?usp=sharing&ouid=100197534236808599244&rtpof=true&sd=true

Запуск тестов:

Установить все внешние зависимости командой pip install -r requirements.txt

Скачать версию Selenium WebDriver для Chrome 108 версии

Запустить тесты можно командой: python -m pytest -v --driver Firefox --driver-path <Путь до вебдрайвера>\geckodriver.exe python -m pytest -v --driver Chrome --driver-path <Путь до вебдрайвера>\chromedriver.exe
