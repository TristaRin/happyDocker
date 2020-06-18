from django.urls import path, include
from . import views
from django.conf.urls import url

urlpatterns = [
    path('hello_world',views.hello_world), 
    url('manage', views.manage),
    url('reactionStop', views.reactionStop),
    url('reaction', views.react),
]
