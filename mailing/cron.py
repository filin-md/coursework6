import logging

from django.conf import settings
from django.core.mail import send_mail


# def mailing_cron():
#     send_mail(
#         subject='Hello World!',
#         message=f'CRON успешно настроен и работает',
#         from_email=settings.EMAIL_HOST_USER,
#         recipient_list=['filin.work@ya.ru']
#     )


def mailing_cron():
    # Настройка логгера
    logger = logging.getLogger('mailing_cron')
    logger.setLevel(logging.INFO)  # Установите уровень логирования по вашему выбору

    # Создайте обработчик для записи логов в файл
    file_handler = logging.FileHandler('mailing_cron.log')  # Укажите путь к файлу для логов
    file_handler.setLevel(logging.INFO)  # Установите уровень логирования для этого обработчика

    # Создайте форматтер для логов
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)

    # Добавьте обработчик к логгеру
    logger.addHandler(file_handler)

    try:
        # Ваш код для отправки почты и выполнения задачи cron

        # Пример логирования информации
        logger.info('CRON успешно настроен и работает')
    except Exception as e:
        # В случае ошибки, вы можете залогировать ее с более высоким уровнем логирования
        logger.error(f'Произошла ошибка: {str(e)}')

if __name__ == "__main__":
    mailing_cron()
