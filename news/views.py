from django.shortcuts import render, redirect

# Create your views here.
import requests
from bs4 import BeautifulSoup as BSoup
from news.models import HeadLine

def scrape(request):
    session = requests.Session()
    session.headers = {"User-Agent": "Googlebot/2.1 (+http://www.google.com/bot.html)"}
    url = "https://www.theonion.com/"

    content = session.get(url, verify=False).content
    soup = BSoup(content, "html.parser")
    News = soup.find_all('div', {"class": "curation-module__item"})
    return redirect("../")