from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$',views.list,name='index'),

    url(r'^create/$',views.create,name='create'),
    url(r'^update/(?P<id>\d+)/$',views.update,name='update'),
    url(r'^delete/(?P<id>\d+)/$',views.delete,name='delete'),
]