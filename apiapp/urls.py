from django.urls import path
from . import views

urlpatterns = [
    path('', views.FirstView.as_view(), name = 'first'),
    path('second-endpoint/', views.SecondView.as_view(), name = 'second'),
    path('third-endpoint/', views.ThirdView.as_view(), name = 'third'),
    path('fourth-endpoint/', views.FourthView.as_view(), name = 'fourth'),
    
]        