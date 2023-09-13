"""
URL configuration for drf_model_generics_all_10_Views_5 project.

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
from testapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/',views.EmployeeListAPIView.as_view()),
    path('api/search/',views.EmployeeSearchAPIView.as_view()),
    path('api/create/',views.EmployeeCreateAPIView.as_view()),
    path('api/retrieve/<int:pk>/',views.EmployeeRetrievePIView.as_view()),
    path('api/update/<int:pk>/',views.EmployeeUpdateAPIView.as_view()),
    path('api/destroy/<int:pk>/',views.EmployeeDestroyAPIView.as_view()),
    path('api/listcreate/',views.EmployeeListCreateAPIView.as_view()),
    path('api/retrieveupdate/<int:pk>/',views.EmployeeRetrieveUpdateAPIView.as_view()),
    path('api/retrievedestory/<int:pk>/',views.EmployeeRetrieveDestoryAPIView.as_view()),
    path('api/retrieveupdatedestory/<int:id>/',views.EmployeeRetrieveUpdateDestoryAPIView.as_view()),


]
