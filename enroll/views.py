from django.shortcuts import render,HttpResponseRedirect
from .models import User
from .forms import StudentRegistrationForm
# Create your views here.


def ADD_SHOW(request):
     # Initialize form
    form = StudentRegistrationForm()

    # Fetch all users
    stud = User.objects.all()

    if request.method == 'POST':
        form = StudentRegistrationForm(request.POST)
        if form.is_valid():
            nm = form.cleaned_data['name']
            em = form.cleaned_data['email']
            mo = form.cleaned_data['mobile']
            pw = form.cleaned_data['password']

            # Create or get user
            FO = User.objects.get_or_create(name = nm, email = em, mobile = mo, password = pw)[0]
            FO.save()
            
            # Clear form after submission
            form = StudentRegistrationForm()

        
    return render(request,'addandshow.html',{'form':form, 'stu':stud})

# This Function Will Update/Edit The Data
def UPDATE_DATA(request, id):
    UO = User.objects.get(pk = id)
    form = StudentRegistrationForm(instance=UO)

    if request.method == 'POST':
        UO = User.objects.get(pk = id)
        form = StudentRegistrationForm(request.POST, instance=UO)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/")
    
       
    return render(request,'updatestudent.html',{'form':form})



# This Function will Detele The data
def DELETE_DATA(request, id):
    if request.method == 'POST':
        DO = User.objects.get(pk = id)
        DO.delete()
        return HttpResponseRedirect("/")