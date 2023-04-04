from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.home),
    path('showproduct/<id>',views.showproduct),
    path('SignUp',views.SignUp),
    path('login',views.login),
    path('viewproduct/<id>',views.viewproduct),
    path('viewbrandproduct/<id>',views.viewbrandproduct),
    path('showbrandproduct/<id>',views.showbrandproduct),
    path("SignOut",views.SignOut),
    path("addToCart",views.addToCart),
    path('viewCart',views.viewCart),
    path('Aboutus',views.Aboutus),
    path('mamearth',views.mamearth),
    path('swissbeauty',views.swissbeauty),
    path('sugarcosmetics',views.sugarcosmetics),
    path('makepayment',views.makepayment),
    #path('career',views.career),
    path('career',views.career,name="career"),
    path('search',views.search),
    path('myorder',views.myorder),
]
