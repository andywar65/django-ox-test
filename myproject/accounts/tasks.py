from django.contrib.auth.models import User
from django.core.mail import send_mail

# Django 6.0+. On Django 5.2: from django_tasks import task
from django.tasks import task


@task
def send_welcome_email(user_id):
    user = User.objects.get(pk=user_id)
    send_mail(
        subject="Welcome",
        message=f"Hi {user.username}, thanks for signing up.",
        from_email=None,
        recipient_list=[user.email],
    )