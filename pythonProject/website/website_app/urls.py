from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name = 'home'),
    path('statistic/', views.statistic, name = 'statistic'),
    path('demand/', views.demand, name = 'demand'),
    path('geography/', views.geography, name = 'geography'),
    path('skills/', views.skills, name = 'skills'),
    path('last_vacancies/', views.last_vacancies, name = 'last_vacancies'),
    path('test/', views.test, name = 'test'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)