from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    # params = {'name': 'Ankit', 'place': 'USA'}
    return render(request, 'index.html')
    # return HttpResponse(" <h1> Anky With AI ")


def analyze(request):
    djtext = request.POST.get('text', 'default')
    removepunk = request.POST.get('removepunk', 'off')
    fullcap = request.POST.get('fullcap', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')
    charcounter = request.POST.get('charcounter', 'off')

    if removepunk == "on":
        # analyzed = djtext
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose': 'Remove Punctuations', 'analyzed_text': analyzed}
        djtext = analyzed
        # return render(request, 'analyze.html', params)

    if fullcap == "on":
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()
        params = {'purpose': 'Change to Uppercase', 'analyzed_text': analyzed}
        djtext = analyzed
        # return render(request, 'analyze.html', params)

    if extraspaceremover == "on":
        analyzed = ""
        for index, char in enumerate(djtext):
            if not(djtext[index] == " " and djtext[index+1] == " "):
                analyzed = analyzed + char
        params = {'purpose': 'Extra Spaces Remover', 'analyzed_text': analyzed}
        djtext = analyzed
        # return render(request, 'analyze.html', params)
    if newlineremover == "on":
        analyzed = ""
        for char in djtext:
            if char != "\n" and char != "\r":
                analyzed = analyzed + char
        params = {'purpose': 'New Line Remover', 'analyzed_text': analyzed}
        djtext = analyzed
        # return render(request, 'analyze.html', params)

    if charcounter == "on":
        analyzed = ""
        # count = 0
        # for char in djtext:
        #     count += 1
        #     analyzed = analyzed + len("djtext")
        # counter = charcounter.count(djtext)
        # print(counter)
        char = str(len(djtext))
        # analyzed = analyzed + char
        params = {'purpose': 'Character Counter', 'analyzed_text': char}
        # return render(request, 'analyze.html', params)

    if removepunk != "on" and fullcap != "on" and extraspaceremover != "on" and newlineremover != "on" and charcounter != "on":
        return HttpResponse('please select any operation and try again')
    return render(request, 'analyze.html', params)
# def space_remover(request, href=None):
#     return HttpResponse('''<h1>Space Remover</h1><a href ="/"> Back To Home </a>''')
#
#
# def remove_punk(request):
#     return HttpResponse('''<h1>Remove Punk</h1><a href ="/"> Back To Home </a>''')
