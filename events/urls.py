from django.urls import path
from events import views

app_name = 'events'

urlpatterns = [
    path('all/', views.get_events_list, name='events_list'),
    path('<int:event_id>/', views.get_event_info, name='event_info'),
]