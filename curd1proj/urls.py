from django.contrib import admin
from django.urls import path
from curdapp1 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home),
    path('create.html/',views.Create_view),
    path('fetche.html/', views.Fetche_view),
    path('update.html/',views.Update_view),
    path('delete.html/',views.Delete_view)
]
