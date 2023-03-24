from django.urls import path

from . import views

urlpatterns = [
    path('<int:pk>/', views.hero_detail_view),
    path('<int:pk>/update/', views.hero_update_view),
    path('<int:pk>/delete/', views.hero_delete_view),
    path('', views.hero_list_create_view)
]