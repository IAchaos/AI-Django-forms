from django.shortcuts import render, redirect
from .models import Student
from .forms import RegistationForm




def registration(request):
    if request.method == 'POST':
        print("POST data:", request.POST) 
        form = RegistationForm(request.POST)
        if form.is_valid(): # the error starts from this line
            
            form.save()
            return redirect('music-school-registration:registration_form')
    else:
        form = RegistationForm()
    return render(request, 'registration/registration.html', {'form': form})