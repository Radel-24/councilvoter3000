from django.urls  import path, re_path

from . import views

app_name = 'poll_app'

urlpatterns = [
	path('', views.index, name='index'),
	path('validation/', views.validation, name='validation'),
	path('election/<str:voter>/', views.election, name='election'),
	path('result/', views.result, name='result'),
	path('end/<str:message>/', views.end, name='end'),
]
