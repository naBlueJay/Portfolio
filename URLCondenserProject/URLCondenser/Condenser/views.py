from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.decorators import api_view
from django.core import serializers
from django.contrib import messages
from rest_framework.response import Response
from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from django.db import connection
from django.shortcuts import redirect

from . models import URLData
from . forms import URLDataForm
from . serializers import URLDataSerializers

import sqlite3
import string
import random

# Key Variables
# The uppercase letters don't matter here. URLs shouldn't be case sensitive
BASE_LIST = '0123456789abcdefghijklmnopqrstuvwxyz./:'
BASE_DICT = dict((c, idx) for idx, c in enumerate(BASE_LIST))

# This is the variable you whould change the base URL for your personal URL
service_url='http://localhost:8000'

# This class will convert the ID to the full URL
class FullURLView(viewsets.ModelViewSet):
    queryset = URLData.objects.all()
    serializers_class = URLDataSerializers

# This Function converts your ID to the full URL
def base_encode(integer, alphabet=BASE_LIST):
    if integer == 0:
        return alphabet[0]

    arr = []
    base = len(alphabet)

    while integer:
        integer, rem = divmod(integer, base)
        arr.append(alphabet[rem])

    arr.reverse()

    return ''.join(arr)

# This function converts the full URL to the ID
def base_decode(request, reverse_base = BASE_DICT):
    originURL = request
    length = len(reverse_base)
    ret = 0

    for i, c in enumerate(originURL[::-1]):
        ret += (length ** i) * reverse_base[c]

    return ret

# This function should generate the shortened URL
def shortChars():
    # This creates the random shortiner that goes at the end of the service_url
    SHORT_LIST_CHAR='0123456789'+string.ascii_letters
    return ''.join([random.choice(SHORT_LIST_CHAR) for i in range(10)])

# This function will check to see if there is an already existing ID in the database
# The program will never create a new ID for an already existing url in the database
def checkifIDExists(ID):
    sc = str(shortChars())
    Retrieved_IDs = list(URLData.objects.values_list('URLID', flat = True))

    if str(ID) in Retrieved_IDs:
        surl = URL_ID = URLData.objects.all().filter(URLID = str(ID))[0].ShortURL
        mess = ("This ID already exists. The shortened link is: {}/{}".format(service_url,surl))
    
    else:
        U = URLData(URLID=ID, ShortURL=sc)
        U.save()
        mess = ("Congratulatons! Your shortened URL is {}/{}".format(service_url,sc))

    return mess

# This function grabs the ID and redirects the user the original URL that's stored in the database
def redirect_short_url(request, short_url):
    redirect_url = service_url + '/condense/'

    try:
        URL_ID = URLData.objects.all().filter(ShortURL = short_url)[0].URLID
        redirect_url = base_encode(int(URL_ID))
    except Exception as e:
        print(e)
    
    return redirect(redirect_url)


def appendPrefix(entry):
    match = ['http','https']

    if any(x in entry for x in match):
        return entry

    else:
        return('https://'+str(entry))

# This checks, cleans, and decodes the the form
def get_form(request):
    if request.method == "POST":
        form = URLDataForm(request.POST)

        if form.is_valid():
            fullurl = form.cleaned_data["EnterURL"]
            fullurladj = appendPrefix(fullurl)

            # By using lower() here we won't have to worry about uppercase characters
            ID = base_decode(fullurl.lower())
            messages.success(request, "{}".format(checkifIDExists(ID)))

    form = URLDataForm()

    return render(request, "myform/form.html", {"form":form})
