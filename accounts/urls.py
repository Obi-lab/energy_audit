from django.urls import path
from . import views



from rest_framework_simplejwt.views import (
    TokenRefreshView,
)

urlpatterns = [
    #Authentication
    path('token/', views.MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', views.RegisterView.as_view(), name='auth_register'),
    
    path('profileUpdate/', views.profile_update, name='profile_update'),
    path('profile/', views.profile_get, name='get_profile'),
    
]
