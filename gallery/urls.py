from django.urls import path
from gallery import views

app_name = 'gallery'
urlpatterns = [
    path('', views.index, name='index'),
    path('image/', views.image, name='image')
]
