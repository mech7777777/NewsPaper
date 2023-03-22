from django.urls import path
from .views import NewsList, NewDetail,Search

urlpatterns = [
    path('', NewsList.as_view()), # т.к. сам по себе это класс, то нам надо представить этот класс в виде view. Для этого вызываем метод as_view
    path('<int:pk>',NewDetail.as_view()),
    path('search',Search.as_view())
    ]

