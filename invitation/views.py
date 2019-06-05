from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Guest, Dishes, Alcohol, Menu
from .forms import PhotoForm
from django.core.mail import EmailMessage
from django.core import mail
from django.contrib.auth.models import User

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
        if guest.guestsIsVisible:
            guests = Guest.objects.all()
            guests_data = []
            i = 1
            guest_slide =[]
            for g in guests:
                if i == 5:
                    guest_slide.append(g)
                    guests_data.append(guest_slide)
                    guest_slide = []
                    i = 1
                elif g == guests[len(guests)-1]:
                    guest_slide.append(g)
                    guests_data.append(guest_slide)
                else:
                    guest_slide.append(g)
                    i += 1

            data = {'guestName': guestName, 'guest': guest, 'form': form, 'photoUrl': photoUrl, 'guests': guests_data, 'count_slide': len(guests_data)}
        else:
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
        if False:
            try:
                email = EmailMessage('Приглашение на свадьбу Влада и Даши', 'World', to=[email])
                email.send()
            except:
                pass

        return HttpResponse('ok', content_type='text/html')


def menu(request):
    guest = Guest.objects.get(user=request.user)
    salads = Dishes.objects.filter(type=1)
    mainDishes = Dishes.objects.filter(type=2)
    garnish = Dishes.objects.filter(type=3)
    alcohol = Alcohol.objects.all()
    try:
        saladId = guest.menu.salad.id
    except:
        saladId = ''
    try:
        mainDishId = guest.menu.mainDish.id
    except:
        mainDishId = ''
    try:
        garnishId = guest.menu.garnish.id
    except:
        garnishId = ''

    alcoholsGuest = []
    for drink in guest.alcohol.all():
        alcoholsGuest.append(drink.id)


    data = {'salads': salads, 'mainDishes': mainDishes, 'garnish': garnish, 'alcohol': alcohol, 'guest': guest,
            'saladId': saladId, 'mainDishId': mainDishId, 'garnishId': garnishId, 'alcoholsGuest': alcoholsGuest}

    return render(request, 'invitation/menu.html', data)


def save_menu(request):
    if request.method == 'POST':
        guest = Guest.objects.get(user=request.user)
        saladId = int(request.POST.get('salad'))
        mainDishId = int(request.POST.get('mainDish'))
        garnishId = int(request.POST.get('garnish'))
        alcoholIds = request.POST.get('alcohol')

        salad = Dishes.objects.get(id=saladId)
        mainDish = Dishes.objects.get(id=mainDishId)
        if garnishId != -1:
            garnish = Dishes.objects.get(id=garnishId)
        else:
            garnish = None

        try:
            menuGuest = Menu.objects.get(salad = salad, mainDish = mainDish, garnish = garnish)
        except Menu.DoesNotExist:
            menuGuest = Menu()
            menuGuest.salad = salad
            menuGuest.mainDish = mainDish
            menuGuest.garnish = garnish
            menuGuest.save()
        guest.menu = menuGuest

        guest.alcohol.clear()
        id = ''
        for s in alcoholIds:
            if s != ',':
                id += s
            else:
                id = int(id)
                alcohol = Alcohol.objects.get(id=id)
                guest.alcohol.add(alcohol)
                id = ''

        guest.save()
        return HttpResponse('ok', content_type='text/html')


def view_menu(request):
    guest = Guest.objects.get(user=request.user)
    data = {'menu': guest.menu, 'isView': True, 'alcohol': guest.alcohol.all()}
    return render(request,'invitation/menu.html', data)


def new_guest(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        family = request.POST.get('family')
        description = request.POST.get('guest_description')
        guest_middle = request.POST.get('guest_middle')
        type = int(request.POST.get('guest_type'))
        family = family.capitalize()
        family = family.replace(" ","")
        name = name.capitalize()
        name = name.replace(" ", "")
        user_name = name + family
        password = family

        try:
            new_user = User.objects.get(username=user_name)
        except User.DoesNotExist:
            new_user = User.objects.create_user(username=user_name, password=password)

        try:
            guest = Guest.objects.get(user=new_user)
        except Guest.DoesNotExist:
            guest = Guest()

        guest.name = name
        guest.family = family
        guest.middleName = guest_middle
        guest.user = new_user
        guest.description = description
        guest.type = type
        guest.save()
        return HttpResponse('ok', content_type='text/html')

