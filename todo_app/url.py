from todo_app import views
from django.conf.urls import url

app_name = 'todo_app'

urlpatterns = [
    url(r'^$',views.TodoListView.as_view(),name='list'),
    url(r'^create/$', views.TodoCreateView.as_view(), name='create'),
    url(r'^update/(?P<pk>\d+)/$',views.TodoUpdateView.as_view(), name='update'),
    url(r'^(?P<pk>\d+)/$',views.TodoDetailView.as_view(), name='details'),
    url(r'^delete/(?P<pk>\d+)/$',views.TodoDeleteView.as_view(),name='delete')
]