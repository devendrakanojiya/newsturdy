from django.shortcuts import render

# Create your views here.
# view

# Create your views here.
from django.shortcuts import render, HttpResponse, redirect
from codebin.models import Codebin
import uuid

def index(request):
    if request.method == 'POST':
        pastetitle = request.POST.get('pastetitle')
        pastecontent = request.POST.get('pastecontent')
        #visibility = request.POST.get('visibility')

        # Generate a unique ID for the paste
        pasteID = str(uuid.uuid4().int & (1 << 31) - 1)

        connect = Codebin(pastetitle=pastetitle, pastecontent=pastecontent, sid=pasteID)  #visibility=visibility
        connect.save()

        # Display a success message
        message = f'Your paste has been created, and your ID is {pasteID}'

        return render(request, 'index.html', {'message': message})

    return render(request, 'index.html')
     #return HttpResponse("working")



def find(request):
    if request.method == 'POST':
        pasteID = request.POST.get('pasteID')
        # visibility = request.POST.get('visibility')

        # Query the database to find the paste with the given ID and visibility
        try:
            paste = Codebin.objects.get(sid=pasteID)  #,visibility=visibility
        except Codebin.DoesNotExist:
            paste = None

        return render(request, 'find.html', {'paste': paste})

    return render(request, 'find.html')


def about(request):
    return render(request,'about.html')




