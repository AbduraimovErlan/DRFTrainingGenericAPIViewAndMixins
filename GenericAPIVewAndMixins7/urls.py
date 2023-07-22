from django.urls import path
from GenericAPIVewAndMixins7 import views


urlpatterns = [
    path('books7/', views.BookListCreateAPIView7.as_view()),
    path('books7/<int:pk>/', views.BookRetrieveUpdateDestroy7.as_view()),
]