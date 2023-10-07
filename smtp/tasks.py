import random
from celery import shared_task
from django.core.mail import send_mail
from lvlind.settings import EMAIL_HOST_USER
from django.contrib.auth import get_user_model
from django.shortcuts import HttpResponse
from accounts.models import MyUser


@shared_task(bind=True)
def smtp_func(self, object):
    """ U (the sender) need to check some account-security steps! """
    """ App passwords: team_esiia3 |-->> get(my_passd) """
    global key 
    key = [random.randint(0, 9) for i in range(1, 6)]
    qs = MyUser.objects.filter(email="ranjalahyandrytahianasylvain@gmail.com")
    mail_sublect = "Hi! Mail Testing from Andry"
    # [print(u) for u in user]
    message = "If you are new to our plateform, please hit that key:" + str(key)
    for u in qs:
        user = u 
    to_email = user.email
    print(to_email)
    send_mail(
        subject=mail_sublect,
        message = message,
        from_email = EMAIL_HOST_USER,
        recipient_list = [to_email],
        fail_silently = True
    )
    return HttpResponse('Done')
