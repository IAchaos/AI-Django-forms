from django.shortcuts import render
from .models import CollegeAdmission
from .forms import CollegeAdmissionForm

def collegeAdmission(request):
    sent = False
    if request.method == 'POST':
        # form was submitted
        form = CollegeAdmissionForm(request.POST)
        if form.is_valid():
            # form fialds passed validation
            form.save()
            sent = True
    else:
        form = CollegeAdmissionForm()
    return render(request, 'collegeAdmission/college_admission.html', {'form': form, 'sent': sent})