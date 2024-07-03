# This is my File -- MR.Rakib
from django.http import HttpResponse
from django.shortcuts import render
from .utils import *

def index(request):
    return render(request, 'index.html')

def analyze(request):
    # Get the text
    django_text = request.GET.get("text", "Default")
    remove_punctuation_param = request.GET.get("removepunc")
    capitalize_first_param = request.GET.get("capfirst")
    remove_newline_param = request.GET.get("newlineremover")
    remove_space_param = request.GET.get("spaceremover")
    count_characters_param = request.GET.get("charcount")

    # Initialize the analyzed text
    analyzed_text = django_text

    # Analyse the Text
    if remove_punctuation_param == "on":
        analyzed_text = removepunc(analyzed_text)
    
    if capitalize_first_param == "on":
        analyzed_text = capfirst(analyzed_text)

    if remove_newline_param == "on":
        analyzed_text = newlineremover(analyzed_text)
    
    if remove_space_param == "on":
        analyzed_text = spaceremover(analyzed_text)
    
    if count_characters_param == "on":
        char_count = charcount(analyzed_text)
        analyzed_text += f"\nCharacter Count: {char_count}"

    data = {'purpose': 'Text Analysis', "analyzed_Text": analyzed_text}

    return render(request, 'analyze.html', data)

# def about(request):
#     return HttpResponse('''<h1>About MR.RAKIB</h1><br><a href="http://127.0.0.1:8000/">Previous</a> <a href="http://127.0.0.1:8000/first/">Next</a>''')

# def first(request):
#     return HttpResponse('''<h1>This is First Page !!!</h1><br><a href="http://127.0.0.1:8000/about/">Previous</a> <a href="http://127.0.0.1:8000/second">Next</a>''')

# def second(request):
#     return HttpResponse('''<h1>This is Second Page !!!</h1><br><a href="http://127.0.0.1:8000/first">Previous</a> <a href="http://127.0.0.1:8000/third">Next</a>''')

# def third(request):
#     return HttpResponse('''<h1>This is Third Page !!!</h1><br><a href="http://127.0.0.1:8000/second">Previous</a> <a href="http://127.0.0.1:8000/last/">Next</a>''')

# def last(request):
#     return HttpResponse('''<h1>This is Last Page !!!</h1><br><a href="http://127.0.0.1:8000/third">Previous</a>''')

    
