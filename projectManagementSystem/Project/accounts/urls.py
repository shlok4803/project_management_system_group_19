from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from django.contrib.auth import views as auth_views
from .views import landing_view, login_view, register_view, register_view_owner, register_view_manager, register_view_employee, home_view
from .forms import PasswordResetConfirmForm
from dashboard.views import dashboard

urlpatterns = [
    path('', landing_view, name="landing"),
    path('login/', login_view, name="login"),
    path('register/', register_view, name="register"),
    path('register/as_owner', register_view_owner, name="reg_owner"),
    path('register/as_manager', register_view_manager, name="reg_manager"),
    path('register/as_employee', register_view_employee, name="reg_employee"),
    path('verification/', include('verify_email.urls')),	
    path('dashboard/',dashboard, name="dashboard"),

    # reset password with email auth
    path('reset_password/', auth_views.PasswordResetView.as_view(template_name='forgot_password.html'), name='reset_password'),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name='forgot_password_sent.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='forgot_password_confirm.html', form_class=PasswordResetConfirmForm), name='password_reset_confirm'),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name='reset_password_complete.html'), name='password_reset_complete')
]


# if settings.DEBUG:
#     urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)