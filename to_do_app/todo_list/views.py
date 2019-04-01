from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import List
from .forms import ListForm

def home(request):
    if request.method == 'POST':
        form = ListForm(request.POST or None)

        if form.is_valid():
            form.save()
            all_items = List.objects.all
            context = {
                'all_items': all_items
            }
            messages.success(request, ('New item has been added to the list!'))
            return render(request, 'home.html', context)
                
    else:
        all_items = List.objects.all
        context = {
            'all_items': all_items
        }
        return render(request, 'home.html', context)

def about(request):
    my_name = 'Syed'
    context = {
        'name': my_name
    }
    return render(request, 'about.html', context)

def delete(request, list_id):
    item = List.objects.get(pk=list_id)
    item.delete()
    messages.success(request, ('Item has been deleted from the list!'))
    return redirect('home')

def cross_off(request, list_id):
    item = List.objects.get(pk=list_id)
    item.item_completed = True
    item.save()
    return redirect('home')

def uncross(request, list_id):
    item = List.objects.get(pk=list_id)
    item.item_completed = False
    item.save()
    return redirect('home')

def edit(request, list_id):
    if request.method == 'POST':
        item = List.objects.get(pk=list_id)

        form = ListForm(request.POST or None, instance=item)

        if form.is_valid():
            form.save()
            messages.success(request, ('Item has been editied!'))
            return redirect('home')

    else:
        item = List.objects.get(pk=list_id)
        context = {
            'item': item
        }
        return render(request, 'edit.html', context)