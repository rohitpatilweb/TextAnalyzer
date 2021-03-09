# I have created this file/rohit

from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,'index.html',)

def analyze(request):

    # getting text
    djtext =request.POST.get('text','default')

    # checkbox
    removepunc= request.POST.get('removepunc','off')
    fullcaps= request.POST.get('fullcaps','off')
    newlineremover= request.POST.get('newlineremover','off')
    removespaces= request.POST.get('removespaces','off')

    if removepunc=="on":
        punctuations = '''!()-[]{};:'",<>./?@#$%^&*~'''
        analyzed=""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        djtext = analyzed

    if(fullcaps=="on"):
        analyzed = ""
        for char in djtext:
            analyzed = analyzed+char.upper()
        djtext = analyzed

    if(newlineremover == "on"):
        analyzed = ""
        for char in djtext:
            if char != "\n" and char !=  "\r":
                analyzed = analyzed + char
            else:
                analyzed = analyzed +" "
        djtext = analyzed

    if(removespaces == "on"):
        analyzed = ""
        for index,char in enumerate(djtext):
            if djtext[index]==" " and djtext[index+1]==" ":
                pass
            else:
                analyzed = analyzed + char
        djtext = analyzed


    info = {'purpose': 'Analyzed text', 'analyzed_text': djtext}
    return render(request, 'analyze.html', info)





