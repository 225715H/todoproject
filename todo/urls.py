from django.urls import path, include
from .views import todolist, tododetail

urlpatterns = [
    path('list/' , todolist.as_view()),
    path('detail/<int:pk>' , tododetail.as_view())
]