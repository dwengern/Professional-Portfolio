from django.urls import path
from django.contrib import admin
from portfolio import views

urlpatterns = [
    path("admin/", admin.site.urls),

    path("", views.home, name="home"),
    path("about", views.about, name="about"),
    path("photography", views.photography_home, name="photography_home"),
    path("projects", views.projects_home, name="projects_home"),
    path("valet_system", views.valet_system, name="valet_system"),

    path("add_car/<str:model_name>/", views.add_car, name="add_car"),
    path("edit_car/<str:model_name>/<int:pk>/", views.edit_car, name='edit_car'),
    path("delete_car/<str:model_name>/<int:pk>/", views.delete_car, name='delete_car'),
]
