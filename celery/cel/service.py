from django.core.mail import send_mail


def send(user_email):
    send_mail('You follow for our',
              'fjdknfkdfng',
              'albertto28@mail.ru',
              [user_email],
              fail_silently=False,
    )
