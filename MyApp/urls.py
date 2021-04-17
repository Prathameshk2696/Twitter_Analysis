
from django.urls import path

from . import views

urlpatterns = [
    path('',views.home),
    path('main',views.main),
    path('index',views.index),
    path('city',views.city),
    path('get_root',views.get_root),
    path('get_children',views.get_children),
    path('get_graph_stats',views.get_graph_stats),
    path('get_triangles_data',views.get_triangles_data),
    path('get_page_rank_data',views.get_page_rank_data),
    path('get_shortest_path',views.get_shortest_path)
]