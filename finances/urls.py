from django.contrib import admin
from django.urls import path, include

from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('admin/', admin.site.urls),

    path('user/', include('django.contrib.auth.urls')),
    path('user/change-password/', auth_views.PasswordChangeView.as_view(template_name='change_pass.html')),


    path('login', LoginView.as_view()),
    path('logout', LogoutView.as_view()),

    path('debitos/', include('apps.debitos.urls'))

]
