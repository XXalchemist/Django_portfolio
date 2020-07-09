from django.urls import path
from portfolio import views

urlpatterns = [
    #path('',views.home_page, name='home'),
    path('',views.project_index, name='project_index'),
    path('<int:pk>/',views.project_detail, name='project_detail'),
]