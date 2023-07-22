from django.urls import path
from GenericAPIVewAndMixins2 import views




urlpatterns = [
    path('books2/', views.BookListCreateAPIView2.as_view()),
    path('books2/<int:pk>/', views.BookRetrieveUpdateDestroyAPIView2.as_view()),
]