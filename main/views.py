from django.http import HttpResponse
from django.core import serializers
from django.shortcuts import render, redirect, get_object_or_404
from main.forms import NewsForm
from main.models import News

#--------

def show_xml(request):
    news_list = News.objects.all()
    xml_data = serializers.serialize("xml", news_list)
    return HttpResponse(xml_data, content_type="application/xml")

#--------

def show_json(request):
    news_list = News.objects.all()
    json_data = serializers.serialize("json", news_list)
    return HttpResponse(json_data, content_type="application/json")

#--------

def show_main(request):
    news_list = News.objects.all()

    context = {
        'npm' : '2402406453594',
        'name': 'Roben Joseph B Tambayong',
        'class': 'KKI',
        'news_list': news_list
    }

    return render(request, "main/main.html", context)

def create_news(request):
    form = NewsForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        return redirect('main:show_main')

    context = {'form': form}
    return render(request, "main/create_news.html", context)

def show_news(request, id):
    news = get_object_or_404(News, pk=id)
    news.increment_views()

    context = {
        'news': news
    }

    return render(request, "main/news_detail.html", context)

# XML by ID
def show_xml_by_id(request, news_id):
    try:
        news_item = News.objects.filter(pk=news_id)  # filter returns a queryset
        xml_data = serializers.serialize("xml", news_item)
        return HttpResponse(xml_data, content_type="application/xml")
    except News.DoesNotExist:
        return HttpResponse(status=404)

# JSON by ID
def show_json_by_id(request, news_id):
    try:
        news_item = News.objects.get(pk=news_id)  # get returns a single object
        json_data = serializers.serialize("json", [news_item])  # wrap in list
        return HttpResponse(json_data, content_type="application/json")
    except News.DoesNotExist:
        return HttpResponse(status=404)