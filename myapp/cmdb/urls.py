from django.conf.urls import url

from . import views
urlpatterns = [
    url(r'^$',views.login.as_view(),name='login'),
    url(r'^login/',views.login.as_view(),name='login'),
    url(r'^index/',views.index.as_view(),name='index'),
    url(r'^logout/',views.logout.as_view(),name='logout'),
]
