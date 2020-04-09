from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from .forms import UploadForm
from .models import Files
from django.conf import settings


def uploadp(request):
    if request.method == 'POST':
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            # return HttpResponse(form.errors.items())
            return redirect('/')
        else:
            return HttpResponse('Invalid form')
    elif request.method == 'GET':
        form = UploadForm()
        return render(request, 'upload.html', {'form': form})
    else:
        return HttpResponse('Invalid request method')


def mainp(request):
    if request.method == 'GET':
        videos = Files.objects.all()
        return render(request, 'main.html', {'videos': videos, 'MEDIA_ROOT': settings.MEDIA_ROOT})
    else:
        return HttpResponse('Invalid request method')
