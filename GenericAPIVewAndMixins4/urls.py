from django.urls import path
from GenericAPIVewAndMixins4 import views



urlpatterns = [
    path('books4/', views.BookListCreateAPIView4.as_view()),
    path('books4/<int:pk>/', views.BookRetrieveUpdateDestroyAPIView4.as_view()),
]