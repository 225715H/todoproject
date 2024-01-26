from django.urls import path, include
from .views import todolist, tododetail, todocreate, tododelete, todoupdate

urlpatterns = [
    path('list/' , todolist.as_view(), name = 'list'),
    path('detail/<int:pk>' , tododetail.as_view(), name = 'detail'),
    path('create/', todocreate.as_view(), name = 'create'),
    path('delete/<int:pk>', tododelete.as_view(), name = 'delete'),
    path('update/<int:pk>', todoupdate.as_view(), name = 'update'),
]