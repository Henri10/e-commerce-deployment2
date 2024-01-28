from django.urls import path
from viewer.views import prove, search

urlpatterns = [
    path('', prove, name='index'),
    path("search/", search, name="search")
]