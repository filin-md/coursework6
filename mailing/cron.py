from datetime import datetime

from django.core.mail import send_mail

from django.conf import settings

from mailing.models import MailingLog, Mailing


# def send_email_periodically():
#     print(settings.EMAIL_HOST_USER)
#     mail = send_mail(
#         'theme',
#         'body',
#         settings.EMAIL_HOST_USER,
#         ['filin.work@ya.ru'],
#         fail_silently=False,
#     )
#     print(mail)


def send_email(ms, message_client):
    result = send_mail(
        subject=ms.message.subject,
        message=ms.message.message,
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[message_client.client.email],
        fail_silently=False
    )

    MailingLog.objects.create(
        mailing=ms,
        client=message_client.client_id,
        status=MailingLog.STATUS_OK if result else MailingLog.STATUS_FAILED,
    )


def send_mails():
    now = datetime.now(datetime.timezone.utc)
    for ms in Mailing.objects.filter(status=Mailing.STATUS_STARTED):
        for mc in ms.mail_to_set.all():
            ml = MailingLog.objects.filter(client=mc.client, mailing=ms)
            if ml.exists():
                last_try_date = ml.order_by('-last_try').first().last_try
                if ms.period == Mailing.PERIOD_DAILY:
                    if (now - last_try_date).days >= 1:
                        send_email(ms, mc)

                elif ms.period == Mailing.PERIOD_WEEKLY:
                    if (now - last_try_date).days >= 7:
                        send_email(ms, mc)

                elif ms.period == Mailing.PERIOD_MONTHLY:
                    if (now - last_try_date).days >= 30:
                        send_email(ms, mc)

            else:
                send_email(ms, mc)
