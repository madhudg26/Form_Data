from django.shortcuts import render
from app.models import *
from django.http import HttpResponse
# Create your views here.
def Form_Topic(request):
    if request.method=="POST":
        tn=request.POST['topic']
        T=Topic.objects.get_or_create(topic_name=tn)[0]
        T.save()
        return HttpResponse('insert_topic is done')

    return render(request,'Form_Topic.html')


def Form_Webpage(request):
    QST=Topic.objects.all()
    d={'topics':QST}
    if request.method=="POST":
        topic=request.POST['topic']
        na=request.POST['na']
        ur=request.POST['ur']
        T=Topic.objects.get_or_create(topic_name=topic)[0]
        T.save()
        W=Webpage.objects.get_or_create(topic_name=T,name=na,url=ur)[0]
        W.save()
        return HttpResponse('Webpage inserted successfully')
    return render(request,'Form_Webpage.html',d)





def Form_Access(request):
    QST=Topic.objects.all()
    d={'topics':QST}
    if request.method=="POST":
        topic=request.POST['topic']
        na=request.POST['na']
        ur=request.POST['ur']
        da=request.POST['da']
        T=Topic.objects.get_or_create(topic_name=topic)[0]
        T.save()
        W=Webpage.objects.get_or_create(topic_name=T,name=na,url=ur)[0]
        W.save()
        A=AccessRecords.objects.get_or_create(name=W,date=da)[0]
        A.save()
        return HttpResponse('Inserted AccessRecord Successfully')
    return render(request,'Form_Access.html',d)

def select_multiple(request):
    QST=Topic.objects.all()
    d={'topics':QST}
    if request.method=="POST":
        tos=request.POST.getlist('topic')
        print(tos)
        QSW=Webpage.objects.none()
        for i in tos:
            QSW=QSW|Webpage.objects.filter(topic_name=i)
        d1={'webpages':QSW}
        return render(request,'display_webpages.html',d1)

    return render(request,'select_multiple.html',d)



def checkbox(request):
    QST=Topic.objects.all()
    d={'topics':QST}
    if request.method=="POST":
        tos=request.POST.getlist('topic')
        print(tos)
        QSW=Webpage.objects.none()
        for i in tos:
            QSW=QSW|Webpage.objects.filter(topic_name=i)
        d1={'webpages':QSW}
        return render(request,'display_webpages.html',d1)
    return render(request,'checkbox.html',d)