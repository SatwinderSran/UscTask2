from django.urls import path
from usc import views

urlpatterns = [
    path('', views.assemblylist, name='assemblylist'),
    path('create/', views.addassembly, name='addassembly'),
    path('delete/<task_id>', views.delete_task, name='delete_task'),
    path('edit/<task_id>', views.edit_task, name='edit_task'),
    path('detail/<task_id>', views.detail, name='detail'),
    path('packing/', views.packing, name='packings'),
    path('shortage/', views.shortage, name='shortages'),
    path('quote/', views.quote, name='quotes'),
]
