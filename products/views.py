from django.shortcuts import render, redirect
from .models import Kond

def kond_list(request):
    konds = Kond.objects.all().order_by('-id')
    return render(request, 'kond_list.html', {'konds':konds})

def kond_detail(request, pk):
    kond = Kond.objects.get(id=pk)
    return render(request, 'kond_detail.html', {'kond':kond})

def create_kond(request):
    if request.method == 'POST':
        brand = request.POST['brand']
        model = request.POST['model']
        image = request.FILES.get('image')
        price = request.POST['price']

        Kond.objects.create(brand=brand, model=model, image=image, price=price)
        return redirect('kond')

    return render(request, 'create_kond.html')

def update_kond(request, pk):
    kond = Kond.objects.get(id=pk)
    if request.method == 'POST':
        kond.brand = request.POST['brand']
        kond.model = request.POST['model']
        kond.price = request.POST['price']
        image = request.FILES.get('image')
        if image:
            kond.image= image
        kond.save()
        return redirect('kond-detail', pk=kond.id)
    return render(request, 'kond_update.html', {"kond":kond} )

def delete_kond(request, pk):
    kond = Kond.objects.get(id=pk)
    if request.method == 'POST':
        kond.delete()
        return redirect('kond')
    return render(request, 'kond_del.html', {'kond':kond}

