from django.urls import path, include

from users_api import views



urlpatterns = [
    path("", views.user_list, name="all_users"),
    path("<int:pk>/", views.user_detail, name="user_detail")
]