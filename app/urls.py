from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.first),
    path('<pk>/',views.second),
    #path('<pk>/',views.RetrieveUpdateDestroy.as_view())
]
