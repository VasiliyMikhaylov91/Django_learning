from django.shortcuts import render
from datetime import datetime, timedelta
from .forms import ImageForm
from django.core.files.storage import FileSystemStorage
from myapp.models import Order, Item, Client


# Create your views here.

def start(request):
    return render(request, 'myapp/start.html')

def week_items(request, pk):
    return period_items(request, pk, 7)


def month_items(request, pk):
    return period_items(request, pk, 30)


def year_items(request, pk):
    return period_items(request, pk, 365)


def period_items(request, pk, period):
    delta = datetime.now() - timedelta(days=period)
    orders = Order.objects.filter(customer_id=pk).filter(
        date_ordered__gt=delta)
    print(delta)
    print(orders)
    item_set = set()
    for order in orders:
        items = order.items.all()
        for item in items:
            item_set.add(item.name)
    context = {'period': f'{period}', 'item_list': item_set}
    return render(request, 'myapp/items.html', context)


def add_image_item(request, pk):
    item = Item.objects.filter(id=pk).first()
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.cleaned_data['image']
            fs = FileSystemStorage()
            fs.save(image.name, image)
            item.image = image.name
            item.save()
    else:
        form = ImageForm()
    item_name = item.name
    context = {'item_name': item_name, 'form': form}
    return render(request, 'myapp/upload_image.html', context)
