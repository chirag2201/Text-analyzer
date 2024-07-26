#I've created this custom file
from django.http import HttpResponse
from django.shortcuts import render
def index(request):
   return render(request,"index.html")

# def about(request):
#     return HttpResponse("about Helo world")

#Generating a pipeline

# def index(request):
#     return HttpResponse("Home")

def analyze(request):
    #get the text
    djtext = request.POST.get('text', 'default')
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    spaceremover = request.POST.get('spaceremover', 'off')
    if removepunc == "on":
        # analyzed = djtext
        punctuations = '''. , ? ! : ; ' " ( ) [ ] { } ... - – / \ & * @ # % ^ _ |'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose':'Removed Punctuations', 'analyzed_text':analyzed}
        #analyze the text
        return render(request, 'analyze.html', params)
    elif(fullcaps=="on"):
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()
            params = {'purpose':'Changed to Uppercase', 'analyzed_text':analyzed}
        #analyze the text
        return render(request, 'analyze.html', params)
    elif(newlineremover=="on"):
        analyzed = ""
        for char in djtext:
            if char != "\n" and char !="\r":
                analyzed = analyzed + char
        params = {'purpose':'New Lines Removed', 'analyzed_text':analyzed}
            #analyze the text
        return render(request, 'analyze.html', params)
    
    elif(spaceremover=="on"):
        analyzed = ""
        for index, char in enumerate(djtext):
            if not (djtext[index]== " " and djtext[index+1]==" "):
                analyzed = analyzed + char
        params = {'purpose':'Extra space is Removed', 'analyzed_text':analyzed}
            #analyze the text
        return render(request, 'analyze.html', params)
                                
    else:
        return HttpResponse("Error")
# def capfirst(request):
#     return HttpResponse("Capitalize first")

# def newlineremove(request):
#     return HttpResponse("Your new line has been removed")
#     # return HttpResponse("New line is removed")

# def spaceremove(request):
#     return HttpResponse("Space removed")

# def charcount(request):
#     return HttpResponse("Character count")

