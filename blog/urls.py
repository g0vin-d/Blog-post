from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.index, name="home" ),
    path('about/', views.about, name="about" ),
    path('createpost/', views.createPost, name="createpost" ),
    path('<int:post_id>/', views.details, name="details" ),
]