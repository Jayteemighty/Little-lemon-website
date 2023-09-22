# from django.http import HttpResponse
from django.shortcuts import render
from .forms import BookingForm
from .models import *



# Create your views here.
def home(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def book(request):
    form = BookingForm()
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
    context = {'form':form}
    return render(request, 'book.html', context)

# Add your code here to create new views
def menu(request):
    menu_data=Menu.objects.all()
    main_data= { "menu": menu_data}
    return render(request, 'menu.html',{"menu":main_data})


def menu_item_view(request, item_name):
    # You can perform any necessary validation or database lookup here
    # For example, if item_name is a valid item in your database, fetch the corresponding data
    # Assuming you have a model called MenuItem, you can do something like this:
    # menu_item = MenuItem.objects.get(name=item_name)

    # Pass the item_name to the template
    return render(request, 'menu_item.html', {'item_name': item_name})