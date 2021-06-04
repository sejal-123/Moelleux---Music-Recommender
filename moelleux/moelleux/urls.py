from django.contrib import admin
from django.urls import path
from mrs.views import home, showhistory, feedback, contact
from auapp.views import usignup, ulogin, ulogout, index, fp
urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/',home, name='home'),
    path('fp/',fp, name='fp'),
    path('showhistory/', showhistory, name='showhistory'),
    path('feedback/', feedback, name='feedback'),
    path('contact/', contact, name='contact'),
    path('usignup', usignup, name='usignup'),
    path('ulogin/', ulogin, name='ulogin'),
    path('ulogout/', ulogout, name='ulogout'),
    path('', index, name='index'),
]