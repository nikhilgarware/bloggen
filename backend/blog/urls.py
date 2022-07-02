from django.urls import path
from blog.api import BlogReleatedApi
urlpatterns = [
    path('home/', BlogReleatedApi.as_view()),

]
