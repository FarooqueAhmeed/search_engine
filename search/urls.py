from django.urls import path
from . import views



urlpatterns = [
    path('', views.index, name='index'),
    path('search', views.search, name='search'),
    path('google_images_search/<str:query>', views.google_images_search, name='google_images_search'),
    path('news/<str:query>', views.news, name='news'),
    path('videos/<str:query>', views.videos, name='videos'),

]