from .views import DebitoCreate, DebitoList, DebitosUpdate, DebitosDetail, DebitosDelete
from django.urls import path, include

urlpatterns = [
    path('list', DebitoList.as_view(), name='debitos_list'),
    path('deb_detail/<int:pk>/', DebitosDetail.as_view(), name='debitos_detail'),
    path('debitos_update/<int:pk>/', DebitosUpdate.as_view(), name='debitos_update'),
    path('deb_delete/<int:pk>/', DebitosDelete.as_view(), name='debitos_delete'),
    path('create', DebitoCreate.as_view(), name='debito_create'),
]
