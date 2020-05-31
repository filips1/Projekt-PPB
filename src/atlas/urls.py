from django.contrib import admin  
from django.urls import path  
from grzyby import views  


urlpatterns = [  
    path('admin/', admin.site.urls),  
    path('insert', views.insert),  
    path('show',views.show),  
    path('',views.move),
    path('edit/<int:id>', views.edit),  
    path('update/<int:id>', views.update),  
    path('delete/<int:id>', views.delete),  
]  