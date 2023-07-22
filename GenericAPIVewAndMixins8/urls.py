from django.urls import path
from GenericAPIVewAndMixins8 import views



urlpatterns = [
    path('books8/', views.BookListCreateAPIView8.as_view()),
    path('books8/<int:pk>/', views.BookRetrieveUpdateDestroy.as_view()),
]