from django.urls import path
from . import views

urlpatterns = [
	path('', views.MainView.as_view(), name='home'),
	path('one/', views.SendMail.as_view(), name='one'),
	path('signin/', views.SignIn.as_view(), name='signin'),
	path('signup/', views.SignUp.as_view(), name='signup'),

]
