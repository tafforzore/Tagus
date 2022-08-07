"""TS URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from gestion.views import Register, Login, index, produit, projet, investir, personnel, getchar,publicite

a = getchar(10)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name = 'index'),

    path('connexion/', Login, name = 'Connexion'),
    path('inscription/', Register, name = 'inscription'),

    path('produit/', produit, name = 'produit'),
    path('projet/', projet, name = 'projet'),
    path('projet/'+a+'/', investir, name = 'investir'),
    path('personnel/', personnel, name = 'personnel'),
    path('publicite/', publicite, name = 'publicite'),
    path('error/', publicite, name = 'error'),
]
