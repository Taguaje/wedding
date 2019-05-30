from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Guest
from .forms import PhotoForm
from django.core.mail import EmailMessage
from django.core import mail


def index(request):
    return render(request, 'invitation/home.html')


def profile(request):
    if request.user.is_authenticated:
        guest = Guest.objects.get(user=request.user)
        guestName = guest.name + " " + guest.family
        try:
            photoUrl = guest.avatar.url
        except:
            photoUrl = ""
        form = PhotoForm(auto_id = False)
        data = {'guestName': guestName, 'guest': guest, 'form': form, 'photoUrl': photoUrl}
        return render(request, 'invitation/profile.html', data)


def confirm_invite(request):
    if request.method == 'POST':
        guest = Guest.objects.get(user=request.user)
        isComing = request.POST.get('isComing')
        if isComing == 'true':
            guest.isComing = True
        else:
            guest.isComing = False
        guest.confirm = True
        guest.save()
        return HttpResponse('ok', content_type='text/html')


def confirm_transfer(request):
    if request.method == 'POST':
        guest = Guest.objects.get(user=request.user)
        needTransfer = request.POST.get('needTransfer')
        if needTransfer == 'true':
            guest.needTransfer = True
        else:
            guest.needTransfer = False
        guest.transferConfirm = True
        guest.save()
        return HttpResponse('ok', content_type='text/html')


def upload_avatar(request):
    if request.method == 'POST':
        guest = Guest.objects.get(user=request.user)
        form = PhotoForm(request.POST, request.FILES, instance=guest)
        if form.is_valid():
            form.save()
            return redirect('profile')


def set_email(request):
    if request.method == 'POST':
        guest = Guest.objects.get(user=request.user)
        email = request.POST.get('email')
        guest.email = email
        guest.save()
        try:
            email = EmailMessage('Приглашение на свадьбу Влада и Даши', 'World', to=[email])
            email.send()
        except:
            pass

        return HttpResponse('ok', content_type='text/html')
