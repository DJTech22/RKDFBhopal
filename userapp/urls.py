from django.urls import path
from.import views
urlpatterns = [
    path("",views.firstpage,name='firstpage'),    
    
    path('studentregistration/', views.studentregistration,name='studentregistration'),
    path('response/', views.response, name='response'),
    path('Student_data/', views.Student_data, name='Student_data'),
    path('initiate_payment/', views.initiate_payment, name='initiate_payment'),
]