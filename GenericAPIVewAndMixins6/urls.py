from django.urls import path
from GenericAPIVewAndMixins6 import views


urlpatterns = [
    path('books6/', views.BookListCreateAPIView6.as_view()),
    path('books6/<int:pk>/', views.BookRetrieveUpdateDestroy6.as_view()),
]