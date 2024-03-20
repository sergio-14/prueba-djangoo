"""
URL configuration for tallerprogra project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from proyectos import views
from django.conf import settings
from django.contrib.staticfiles.urls import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('base/', views.base, name='base'),
    path('poryectos/', views.poryectos, name='poryectos'),
    path('logout/',views.signout, name='logout'),
    path('signin/',views.signin, name='signin'),
    path('programadores',views.programadores,name='programadores'),
    path('programadores/crear',views.crear,name='crear'),
    path('editar',views.editar,name='editar'),
    path('form',views.form,name='form'),
    path('eliminar/<int:id>',views.eliminar,name='eliminar'),
    path('programadores/editar/<int:id>',views.editar, name='editar'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)