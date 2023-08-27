from datetime import datetime
from django.shortcuts import render, redirect, get_object_or_404
from django.http import FileResponse, HttpResponse, HttpResponseRedirect
from microapp.models import *
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from microapp.models import contact_table
from .forms import FileUploadForm
from .models import File


# Create your views here.

def home(request):
    return render(request,'index.html')

def aboutus(request):
    return render(request,'about.html')

def services(request):
    return render(request,'services.html')

def team(request):
    return render(request,'team.html')

def contact(request):
    if request.method == "POST":
        a = request.POST.get('name')
        b = request.POST.get('email')
        c = request.POST.get('phone')
        d = request.POST.get('message')

        enquiry = contact_table(name = a, email = b, phone = c, message = d)
        enquiry.save()

        messages.success(request, 'Form Submitted Successfully...')

    return render(request,'contact.html')

def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        
        user = authenticate(request, username = username, password = password)

        if user is not None:
            # is not None is keyword None 'N' is capital which check above user (username and password) is available in database or not

            login(request, user)
            
            request.session['username_id'] = username    

            # Redirect to a success page.
            return redirect('dashboard')
            # from django.shortcuts import redirect, render - this module we need to import in same file, to access redirect() where only path name should be call
        else:
            # display 'invalid login' error message
            messages.error(request, 'In-correct username or password!..')    
        
    return render(request, 'login.html')

@login_required(login_url='login_user')
def dashboard(request):
    
    info = contact_table.objects.all()
    # contact is table name which we create in models.py
    data = {'information':info}

    print('You are logged in, Hi', request.session.get('username_id'))

    return render(request, 'dashboard/dashboard.html', data)


def contact_info(request):

    info = contact_table.objects.all()
    # contact is table name which we create in models.py
    data = {'information':info}

    
    return render(request, 'dashboard/tables.html', data)



def upload_file(request):
    if request.method == 'POST':
        form = FileUploadForm(request.POST, request.FILES)
        if form.is_valid():
            file = form.save(commit=False)
            file.file_type = file.file.name.split('.')[-1].lower()
            file.uploaded_at = datetime.now()  # Set the uploaded_at field
            file.save()     
            # form.save()      
            return redirect('upload_file')
    else:
        form = FileUploadForm()

        files = File.objects.all()
    return render(request, 'dashboard/upload.html', {'form': form, 'files': files})

def delete_file(request, file_id):
    file = get_object_or_404(File, id=file_id)
    file.delete()
    return redirect('upload_file')

def services(request):
    files = File.objects.all()
    return render(request, 'services.html', {'files': files})

def download_file(request, file_id):
    # file = File.objects.get(id=file_id)
    # return redirect(file.file.url)
    file = get_object_or_404(File, id=file_id)
    file_path = file.file.path
    return FileResponse(open(file_path, 'rb'), as_attachment=True)



