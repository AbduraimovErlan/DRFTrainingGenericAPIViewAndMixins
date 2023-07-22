from GenericAPIVewAndMixins1 import views
from django.urls import path

urlpatterns = [
    path('books1/', views.BookListCreateView1.as_view()),
    path('books1/<int:pk>/', views.BookRetrieveUpdateDestroyView1.as_view())
]