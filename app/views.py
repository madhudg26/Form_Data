from django.shortcuts import render
from app.models import *
from django.http import HttpResponse
# Create your views here.
def insert_topic(request):
    if request.method=="POST":
        tn=request.POST['topic']
        T=Topic.objects.get_or_create(topic_name=tn)[0]
        T.save()
        return HttpResponse('insert_topic is done')

    return render(request,'Form_Page.html')


def Form_Webpage(request):

    if request.method=="POST":
        tn=request.POST['topic']
        name=request.POST['name']
        url=request.POST['url']
        T=Topic.objects.get_or_create(topic_name=tn)[0]
        T.save()
        W=Webpage.objects.get_or_create(topic_name=T,name=name,url=url)[0]
        W.save()
        return HttpResponse('Inserted Webpage successfull')
    return render(request,'Form_Webpage.html')





def Form_Access(request):
    if request.method=="POST":
        tn=request.POST['topic']
        name=request.POST['name']
        url=request.POST['url']
        date=request.POST['date']
        T=Topic.objects.get_or_create(topic_name=tn)[0]
        T.save()
        W=Webpage.objects.get_or_create(topic_name=T,name=name,url=url)[0]
        W.save()
        A=AccessRecords.objects.get_or_create(name=W,date=date)[0]
        A.save()
        return HttpResponse('Inserted AccessRecords successfully')
    return render(request,'Form_Access.html')
