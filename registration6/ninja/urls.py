from django .urls import path
from . import views
urlpatterns=[path('k/',views.create,name="create"),
             path('',views.login,name="login"),
             path('t/',views.home,name="home"),
             path('tt/',views.logout,name="logout"),
             ]