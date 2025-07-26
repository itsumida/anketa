from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('mother/', views.create_mother, name='create_mother'),
    path('child/<int:mother_id>/', views.create_child, name='create_child'),
    path('anketa/<int:child_id>/', views.create_anketa_response, name='create_anketa_response'),
    path('result/<int:anketa_id>/', views.anketa_result_view, name='anketa_result'),
]
