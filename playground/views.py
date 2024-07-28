from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import FileUploadForm
from .models import UploadedFile

def say_hello(request):
    return render(request,'hello.html')

def upload_file(request):
    if request.method == 'POST':
        form = FileUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('upload_success')
    else:
        form = FileUploadForm()
    return render(request, 'upload.html', {'form': form})

def upload_success(request):
    return render(request, 'upload_success.html')

# Create your views here.
