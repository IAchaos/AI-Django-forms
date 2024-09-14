from django.shortcuts import render, redirect
from .forms import FeedbackForm




# Feedback handling function 
def feedbackHandler(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        done = False
        if  form.is_valid():
            form.save()
            done = True
            return redirect('feedback:message')
        else:
            print(form.errors)
    else: 
        form = FeedbackForm()
    
    return render(request, 'feedback/form.html', {'form': form})

def messages(request):
    message = "Thank you for your feedback!"
    return render(request, 'feedback/messages.html', {'message': message})
        
