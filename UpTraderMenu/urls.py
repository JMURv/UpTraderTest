from django.contrib import admin
from django.urls import path
from menu import views as menu_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('pc_components/', menu_views.pc_components_view, name="pc_components"),
    path('smartphones/', menu_views.smartphones_view, name="smartphones"),
    path('cameras/', menu_views.cameras_view, name="cameras"),
    path('catalog/', menu_views.catalog_view, name="catalog"),
    path('', menu_views.catalog_view, name="index"),
]
