from django.urls import path
from .views import faq_list, faq_detail, faq_create, faq_update, faq_delete

app_name = 'faq'

urlpatterns = [
    path('', faq_list, name='faq_list'),
    path('<int:faq_id>/', faq_detail, name='faq_detail'),
    path('create/', faq_create, name='faq_create'),
    path('<int:faq_id>/update/', faq_update, name='faq_update'),
    path('<int:faq_id>/delete/', faq_delete, name='faq_delete'),
]

