from django.http import HttpResponse
from django.shortcuts import render

def homepage(request):
    return render(request, 'homepage.html')

def home(request):
    return HttpResponse('<h1>Ok</h1>')

def count(request):
    fulltxt = request.GET['Fulltext']
    print(fulltxt)
    wordlist = fulltxt.split()
    print(len(wordlist))
    return render(request, 'count.html',{'fultxt':fulltxt, 'wordno':len(wordlist)})
