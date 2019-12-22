
from django.urls import path
from.import views

urlpatterns = [
    path('',views.homepage),
    path('homepage/',views.homepage),
    path('count/',views.count, name='cnt'),



]
