from django.urls import path

from . import views

urlpatterns = [
    path('save',views.send_email),
    path('delete/<int:ID>/',views.delete),

    path('', views.index, name='index'),
    # path('list',views.view_Email_lists,name='list'),
    # path('delete/<int:ID>', views.delete_email)
    
    # path('add',views.add,name='add')
]