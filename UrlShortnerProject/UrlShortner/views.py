from django.shortcuts import render,redirect
from UrlShortner.models import ShortUrl
from UrlShortner.forms import ShortUrlForm
from datetime import datetime
import random, string
# Create your views here.
def index(req):
    return render(req,'index.html')

def createShortUrl(req):
    if req.method == 'POST':
        form = ShortUrlForm(req.POST)
        if form.is_valid():
            original_website = form.cleaned_data['original_url']
            random_list = list(string.ascii_letters)
            random_chars = ''
            for i in range(6):
                random_chars += random.choice(random_list)
            while len(ShortUrl.objects.filter(short_url=random_chars)) != 0:
                for i in range(6):
                    random_chars += random.choice(random_list)
            d = datetime.now()
            shortUrlObj = ShortUrl(original_url = original_website,
            short_url = random_chars, created_on = d)
            shortUrlObj.save()
            return render(req,'urlcreated.html',{'chars':random_chars})
    else:
        form = ShortUrlForm()
        context = {'form':form}
        return render(req,'create.html',context)

def redirectView(req,url):

    currUrl = ShortUrl.objects.filter(short_url=url)
    if len(currUrl) == 0:
        return render(req,'pagenotfound.html')
    context = {'obj':currUrl[0]}
    # return render(req,'redirect.html',context)

    return redirect(currUrl[0].original_url)
