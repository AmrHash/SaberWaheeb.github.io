"""dentist URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path , include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('/', views.home, name = 'home'),
    path('index.html', views.HomeView.as_view(), name = 'home2'),
    path('article/<int:pk>', views.ArticleDetailView.as_view(), name='article-detail'),
    path('contact.html', views.contact, name ='contact'),
    path('bio.html', views.bio, name = 'bio'),
    path('science.html', views.Science, name = 'science'),
    path('science/<int:pk>', views.ScienceDetailView.as_view(), name='science-detail'),
    path('operation.html', views.Operation, name = 'operation'),
    path('operation.html', views.OperationView, name = 'operations'),
    path('operation/<int:pk>', views.OperationDetailView.as_view(), name='operation-detail'),
    
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
