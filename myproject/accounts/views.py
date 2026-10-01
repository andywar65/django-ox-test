from django.contrib.auth.models import User
from django.db import transaction
from django.http import HttpResponse
from django.shortcuts import render

from .tasks import send_welcome_email


def register(request):
    if request.method != "POST":
        return render(request, "accounts/register.html")
    with transaction.atomic():
        user = User.objects.create_user(
            username=request.POST["username"],
            email=request.POST["email"],
        )
        send_welcome_email.enqueue(user.pk)
    return HttpResponse(f"Thanks, {user.username}. Your welcome email is on its way.")
