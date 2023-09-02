from django.urls import path
from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='users'),
    path('create/', views.RegistrationFormView.as_view(), name='register'),
    # path('create/<int:id_pk>/update', views.UserEditFormView.as_view(), name='users_update'),
    # path('create/<int:id_pk>/delete', views.UserDeleteFormView.as_view(), name='users_delete'),
]
