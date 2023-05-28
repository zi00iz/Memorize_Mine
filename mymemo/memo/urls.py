from django.urls import path

from . import views

urlpatterns = [
    path('', views.memo_list, name = 'memo_list'),
    path('<int:pk>', views.memo_detail, name = 'memo_detail'),
    path('post/', views.memo_post, name='memo_post'),
    path('<int:pk>/edit/', views.memo_edit, name='memo_edit'),
    path('<int:pk>/delete/', views.memo_delete, name='memo_delete'),
]