from django.urls import path

from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.index, name='index'),

    path('index.html', views.index, name='index'),
    path('archive.html', views.archives, name='archives'),
    path('techtips.html', views.techtips, name='tips'),
    path('about.html', views.about, name='about'),
    path('<int:blog_id>/', views.entry, name='entry'),
    path('<int:blog_id>/comment/', views.comment, name='comment'),
]