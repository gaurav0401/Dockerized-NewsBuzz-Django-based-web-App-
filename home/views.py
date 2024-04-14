from django.shortcuts import render , redirect
from django.http import HttpResponse
import requests
from bs4 import BeautifulSoup as BSoup
from home.models import Headline
# Create your views here.

dict={'name':""}
def scrape(request, name):
    Headline.objects.all().delete()
    session = requests.Session()
    session.headers = {"User-Agent": "Googlebot/2.1 (+http://www.google.com/bot.html)"}
    url = f"https://www.theonion.com/{name}"
    content = session.get(url).content
    soup = BSoup(content, "html.parser")
    dict['name']=name
    News = soup.find_all("div", {"class": "sc-cw4lnv-13 hHSpAQ"})

    for article in News:
        main = article.find_all("a", href=True)

        linkx = article.find("a", {"class": "sc-1out364-0 dPMosf js_link"})
        link = linkx["href"]
        

    
    
        titlex = article.find("h2", {"class": "sc-759qgu-0 cvZkKd sc-cw4lnv-6 TLSoz"})
        title = titlex.text

        descx=article.find("p" , {"class":"sc-77igqf-0 fnnahv"})
        desc=descx
        print(desc)

        imgx = article.find("img")["data-src"]

        new_headline = Headline()
        new_headline.title = title
        # if description_element != None:
        #     new_headline.description = description_element
        # print(new_headline.description)
        new_headline.url = link
        new_headline.category=name
    
        new_headline.image = imgx
        new_headline.save()
    return redirect("../")






def index(request):
    headlines = Headline.objects.all()[::-1]
    category=dict['name']
    category=category.title()
    print(category)
    context = {
        "object_list": headlines,
        "category": category
    }
    return render(request, "home.html", context)
