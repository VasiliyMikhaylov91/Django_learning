from django.urls import path
from myapp.views import week_items, month_items, year_items, add_image_item, start

urlpatterns = [
    path('', start),
    path('week/<int:pk>/', week_items),
    path('month/<int:pk>/', month_items),
    path('year/<int:pk>/', year_items),
    path('add_image_item/<int:pk>', add_image_item),
]