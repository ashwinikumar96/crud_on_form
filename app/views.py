from django.shortcuts import render
from app.models import *
# Create your views here.

def insertschool(request):
    if request.method == 'POST':
        scn = request.POST['scn']
        sp = request.POST['sp']
        sl = request.POST['sl']
        QSSO = School.objects.get_or_create(scname = scn,scprincipal = sp, sclocation = sl)[0]
        QSSO.save()
        QLSO = School.objects.all()
        return render(request,'display_school.html',{'QLSO':QLSO})
    return render(request, 'insert_school.html')