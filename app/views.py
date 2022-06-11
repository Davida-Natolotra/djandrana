from django.shortcuts import render
from .models import User
# Create your views here.
def index(request):
    return render(request, 'app/index.html')

def rearrange():
    all = User.objects.all()
    for i in range(len(all)):
        all[i].idUser = i+1
        all[i].save(update_fields=['idUser'])