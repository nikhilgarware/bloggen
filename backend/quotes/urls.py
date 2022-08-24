from django.urls import path
from quotes.api import QuotesReleatedApi
urlpatterns = [
    path('home/', QuotesReleatedApi.as_view()),

]
