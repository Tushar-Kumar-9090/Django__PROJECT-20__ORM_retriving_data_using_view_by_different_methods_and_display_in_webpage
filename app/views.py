from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from app.models import *
from django.db.models.functions import *

## Retrieving the data of Topic
def display_topics(request):

    topic=Topic.objects.all()
    topic=Topic.objects.filter(topic_name='wwe')
    ## topic=Topic.objects.get(topic_name='wwe')        it will showing error in HTML page//FE page
    topic=Topic.objects.all()

    d={'topics':topic}
    return render(request,'display_topics.html',d)





## Retrieving the data of Webpage
def display_webpages(request):

    webpage=Webpage.objects.all()
    webpage=Webpage.objects.filter(topic_name='wwe')
    ## webpage=Webpage.objects.get(topic_name='wwe')    it will showing error in HTML page//FE page

    webpage=Webpage.objects.exclude(topic_name='cricket')
    webpage=Webpage.objects.all()[3::]
    webpage=Webpage.objects.all()[::-1]
    webpage=Webpage.objects.all().order_by('name')   ## it will be showing in asci value ordering (assending order)
    webpage=Webpage.objects.all().order_by('-name')  ## it will be showing in revering order (decending order)
    webpage=Webpage.objects.all().order_by(Length('name'))
    webpage=Webpage.objects.all().order_by(Length('name').desc())

    webpage=Webpage.objects.all()

    d={'webpages':webpage}
    return render(request,'display_webpages.html',d)





## Retrieving the data of Access_records
def display_accessrecords(request):

    accessrecord=AccessRecord.objects.all()
    d={'accessrecords':accessrecord}

    return render(request,'display_access_records.html',d)



def display_all(request):

    topic=Topic.objects.all()
    webpage=Webpage.objects.all()
    accessrecord=AccessRecord.objects.all()

    d={'topics':topic, 'webpages':webpage, 'accessrecords':accessrecord}

    return render(request,'display_all.html',d)









