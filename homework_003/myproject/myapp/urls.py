from django.urls import path
from myapp.views import week_items, month_items, year_items

urlpatterns = [
    path('week/<int:pk>/', week_items),
    path('month/<int:pk>/', month_items),
    path('year/<int:pk>/', year_items),
]