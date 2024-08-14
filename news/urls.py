from django.urls import path

from .views import (
    HomeView, ContactView, NewsDeatilView, CategoryDeatilView
)


urlpatterns = [
    path('', view=HomeView.as_view(), name='home_page'),
    path('contact/', view=ContactView.as_view(), name='contact_page'),
    path('news-detail/<int:pk>/', view=NewsDeatilView.as_view(), name='news_detail_page'),
    path('category-detail/<int:pk>/', view=CategoryDeatilView.as_view(), name='category_detail_page')
]