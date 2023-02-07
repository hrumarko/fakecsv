from django.urls import path
from . import views


urlpatterns = [
    path('login/', views.UserLogin.as_view(), name='login'),
    path('register/', views.UserRegister.as_view(), name='register'),
    path('logout/', views.logout_user, name='logout'),
    path('', views.index, name='home'),
    path('create-schema/', views.create_schema, name='create-schema'),
    path('data-schemas/', views.data_schemas, name='data-schemas'),
    path('edit-schema/<int:pk>/', views.edit_schema, name='edit-schema'),
    path('delete-shema/<int:pk>', views.delete_schema, name='delete-schema'),
    path('data-sets/<int:pk>', views.data_sets, name='data-sets'),
    path('create-file/', views.create_file, name='create-file'),
]
