from django.urls import path
from . import views

urlpatterns = [
	path('', views.MainView.as_view(), name='home'),
	path('one/', views.SendSingle.as_view(), name='one')

]
