# my file-sam
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def analyze(request):
    # get the text
    djtext = request.GET.get('text', 'default')
    # chechkbox values
    removepunc = request.GET.get('removepunc', 'off')
    fullcaps = request.GET.get('fullcaps', 'off')
    newlineremover = request.GET.get('newlineremover', 'off')
    spaceremover = request.GET.get('spaceremover', 'off')
    charcount = request.GET.get('charcount', 'off')
    # check Which checkbox is on
    if removepunc == "on":
        punctuations = '''`~!@#$%^&*()_+{}|"':;><.,?/*-+/[]'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed+char
        params = {'purpose': 'Remove Punctuations', 'analyzed_text': analyzed}
        djtext = analyzed
    if fullcaps == 'on':
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()
        params = {'purpose': 'UPPERCASE', 'analyzed_text': analyzed}
        djtext = analyzed
    if newlineremover == 'on':
        analyzed = ""
        for char in djtext:
            if char != "\n" and char!="\r":
                analyzed = analyzed + char
        params = {'purpose': 'New LineRemover', 'analyzed_text': analyzed}
        djtext = analyzed
    if spaceremover == 'on':
        analyzed = ""
        for i, char in enumerate(djtext):
            if not (djtext[i] == " " and djtext[i+1] == " "):
                analyzed = analyzed+char
        params = {'purpose': 'Space Remover', 'analyzed_text': analyzed}
        djtext = analyzed
    elif charcount == 'on':
        count = 0
        for char in djtext:
            if char != " ":
                count += 1
        params = {'purpose': 'Charcters Counter', 'analyzed_text': count}
    if charcount != 'on' and spaceremover != 'on' and newlineremover != 'on' and fullcaps != 'on' and removepunc != "on":
        return HttpResponse("error")

    return render(request, 'analyze.html', params)


