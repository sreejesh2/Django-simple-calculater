
from django.urls import path
from .  import views

urlpatterns = [
    path("",views.home,name='home'),
    path('add',views.AddView.as_view(),name="add"),
    path('sub',views.SubView.as_view(),name="sub"),
    path('mul',views.MulView.as_view(),name="mul"),
    path('div',views.DivView.as_view(),name="div"),
    path('fact',views.FactView.as_view(),name="fact"),
    path('prime',views.PrimeNumberView.as_view(),name="prime"),
    path('amstrong',views.AmstrongNumberView.as_view(),name="am"),
    path('palindrome',views.PalindromeNumberView.as_view(),name="pal"),
]
