# from django.urls import path
# from . import views

# urlpatterns = [
#     path('', views.PostView.as_view(), name='post_list'),
#     path('<slug:slug>/', views.post_detail, name='post_detail'),
# ]

from django.urls import path
from . import views

urlpatterns = [
    path('', views.PostView.as_view(), name='home'),  # Renomear para 'home'
    path('<slug:slug>/', views.post_detail, name='post_detail'),
]
