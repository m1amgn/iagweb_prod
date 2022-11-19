from django.shortcuts import render
from .models import Video, ProductImages, Services, AboutMe
from orders.models import Order

from orders.forms import OrderForm
from orders.sendmessage import send_telegram


def webpage(request):
    video = Video.objects.all()
    product_images = ProductImages.objects.all()
    services_dreds = Services.objects.get(pk=1)
    services_afro = Services.objects.get(pk=2)
    services_braids = Services.objects.get(pk=3)
    services_learn = Services.objects.get(pk=4)
    about_me = AboutMe.objects.all()
    form = OrderForm()

    context = {
        'video': video,
        'product_images': product_images,
        'services_dreds': services_dreds,
        'services_afro': services_afro,
        'services_braids': services_braids,
        'services_learn': services_learn,
        'about_me': about_me,
        'form': form
    }

    return render(request, 'index.html', context)


def get_order(request):
    name = request.POST['name']
    email = request.POST['email']
    order = Order(name=name, email=email)
    order.save()
    send_telegram(tg_name=name, tg_email=email)
    return render(request, 'order.html', {'name': name})