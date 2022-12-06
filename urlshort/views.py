from django.shortcuts import render

# Models will request queries from the DB and retrive Objs
from .models import ShortURL
from .forms import CreateNewShortURL

# Get datetime
from datetime import datetime

# Here we have two options UUID(gives more options when scaling) or rangom string 
import random, string

# Create your views here.
def home(request):
    # return render(request, 'home.html')
    form = CreateNewShortURL() # blank form 
    context = {'form': form}
    return render(request, 'home.html', context)

def redirect(request, url):
    current_obj = ShortURL.objects.filter(short_url=url) 
    if len(current_obj) == 0:
        return render(request, 'pagenotfound.html')

    context = { 'obj': current_obj[0] }
    return render(request, 'redirect.html', context)

def reverseURL(request):
    if request.method == 'POST':
        form = CreateNewShortURL(request.POST) # create a instance of form
        if form.is_valid():
            url_shot = form.cleaned_data['original_url']
            url = url_shot.split('/')[-1]
            current_obj = ShortURL.objects.filter(short_url=url)
            if len(current_obj) == 0:
                return render(request, 'pagenotfound.html')
            context = { 'obj': current_obj[0] }
            return render(request, 'reverse.html', context)
    return render(request, 'pagenotfound.html')

def createShortURL(request):

    #POST doen't show in the url. Prefered for usernames, passwords...(Sensitive data)
    if request.method == 'POST':
        form = CreateNewShortURL(request.POST) # create a instance of form
        if form.is_valid():
            original_website = form.cleaned_data['original_url']
            random_chars_list = list(string.ascii_letters)
            random_chars = ''

            # Create ramdom characters seq 
            for i in range(6):
                random_chars += random.choice(random_chars_list)
            while len(ShortURL.objects.filter(short_url=random_chars)) != 0:
                for i in range(6):
                    random_chars += random.choice(random_chars_list)
            d = datetime.now()
            s = ShortURL(original_url=original_website, short_url=random_chars, time_date_created=d)
            s.save()
            # render accepts a third context arg(dict)
            return render(request, 'urlcreated.html', {'chars':random_chars})
    else:
        # when the request method is GET
        form = CreateNewShortURL() # blank form 
        context = {'form': form}
        return render(request, 'create.html', context)