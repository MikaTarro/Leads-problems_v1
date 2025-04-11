import requests
import logging
from datetime import datetime

"""
Все сообщения уровня INFO и выше будут записываться в файл service_check.log
"""
logging.basicConfig(filename='service_check.log', level=logging.INFO)

services = {
    "Formit": "https://formit.fake",
    "LeadSync": "https://leadsync.fake",
    "MailPipe": "https://mailpipe.fake",
    "BitDashboard": "https://bitdashboard.fake"
}
"""
Сортим апи по доступности через респонс= 200 или падает
"""
def check_service(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print(f"{url} работает.")
        else:
            log_error(url, response.status_code)
    except requests.exceptions.RequestException as e:
        log_error(url, str(e))
"""
Записываем ошибки
"""
def log_error(url, error):
    log_entry = f"{datetime.now()} - {url} - Ошибка: {error}"
    logging.error(log_entry)
    print(f"Отправить уведомление: {log_entry}")

# Проверка всех сервисов
for service, url in services.items():
    check_service(url)