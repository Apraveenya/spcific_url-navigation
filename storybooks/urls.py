from django.urls import path
from storybooks.views import *
appname='storybooks'
urlpatterns=[
    path('harry',harry,name='harry'),
    path('moon',moon,name='moon'),
]