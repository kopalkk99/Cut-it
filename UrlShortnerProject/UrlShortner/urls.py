from django.urls import path,include
from UrlShortner import views

urlpatterns = [
    path('',views.index,name="index"),
    path('create/',views.createShortUrl,name="create"),
    path('<str:url>',views.redirectView,name="redirect")
]
