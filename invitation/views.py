from django.shortcuts import render
from django.http import HttpResponse
from .models import Guest


def index(request):
    return render(request, 'invitation/home.html')


def profile(request):
    if request.user.is_authenticated:
        guest = Guest.objects.get(user=request.user)
        guestName = guest.name + " " + guest.family
        data = {'guestName': guestName, 'guest': guest}
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
