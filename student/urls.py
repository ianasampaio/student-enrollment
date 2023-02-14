from django.urls import path
from . import views

urlpatterns = [
    path('', views.List_students.as_view(), name='list_students'),
    path('detail/<uuid:pk>/', views.Detail_students.as_view(), name='detail_students'),
    path('create/', views.Create_students.as_view(), name='create_students'),
    path('update/<uuid:pk>/', views.Update_students.as_view(), name='update_students'),
    path('delete/<uuid:pk>/', views.Delete_students.as_view(), name='delete_students'),
]