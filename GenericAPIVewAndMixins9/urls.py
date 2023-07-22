from  django.urls import path
from GenericAPIVewAndMixins9 import views



urlpatterns = [
    path('books9/', views.BookListCreateAPIView9.as_view()),
    path('books9/<int:pk>/', views.BookRetrieveUpdateDestroy9.as_view()),
]