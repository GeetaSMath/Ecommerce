from django.urls import path

from . import views

urlpatterns = {
    path('user_registration', views.Registration.as_view(), name="registration_user"),
    path('user_login', views.Login.as_view(), name="user_login"),
    path('user_logout', views.Logout.as_view(), name="user_logout")

}
