from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
    path("post/<int:pk>/", views.post_detail, name="post_detail"),
    path("category/<category>/", views.category, name="category"),
    path("create_post/", views.makepost, name="create_post"),
    path("journal/", views.journal, name="journal"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)