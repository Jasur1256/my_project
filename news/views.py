from django.shortcuts import render

from  django.views import View
from .models import CategoryModel, NewsModel


class HomeView(View):
    def get(self, request):

        category_list = CategoryModel.objects.all()
        all_news_list = NewsModel.manager.all().order_by('-publish_time')[:9]
        uzb_news_list = NewsModel.manager.all().filter(category__name="O'ZBEKISTON").order_by('-publish_time')[:6]
        world_news_list = NewsModel.manager.all().filter(category__name="JAHON").order_by('-publish_time')[:6]
        economy_news_list = NewsModel.manager.all().filter(category__name="IQTISODIYOT").order_by('-publish_time')[:6]
        fan_news_list = NewsModel.manager.all().filter(category__name="FAN-TEXNIKA").order_by('-publish_time')[:6]
        sport_news_list = NewsModel.manager.all().filter(category__name="SPORT").order_by('-publish_time')[:6]

        context = {
            'category_list': category_list,
            'all_news_list': all_news_list,
            'uzb_news_list': uzb_news_list,
            'world_news_list': world_news_list,
            'economy_news_list': economy_news_list,
            'fan_news_list': fan_news_list,
            'sport_news_list': sport_news_list
        }

        return render(request=request, template_name='news/home.html', context=context)
      


class ContactView(View):
    def get(self, request):


        category_list = CategoryModel.objects.all()

        context = {
            'category_list': category_list,
        }

        return render(request=request, template_name='news/contact.html', context=context)


class NewsDeatilView(View):
    def get(self, request, pk):
        news_detail = NewsModel.objects.get(pk=pk)
        category_list = CategoryModel.objects.all()

        context = {
            'category_list': category_list,
            'news_detail': news_detail
        }
        
        return render(request=request, template_name='news/news_detail.html', context=context)


class CategoryDeatilView(View):
    def get(self, request, pk):
        category_detail = CategoryModel.objects.get(pk=pk)
        news_list = NewsModel.manager.all().filter(category__name=category_detail).order_by('-publish_time')[:6]
        category_list = CategoryModel.objects.all()

        context = {
            'category_list': category_list,
            'category_detail': category_detail,
            'news_list': news_list
        }
        
        return render(request=request, template_name='news/category_detail.html', context=context)