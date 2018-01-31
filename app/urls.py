from django.conf.urls import url
from django.contrib.auth import views as auth_views

from . import views

app_name = 'app'
urlpatterns = [
    url(r'^$', views.index, name='index'),

    url(r'^login/$', auth_views.login, name='login'),

    url(r'^register/$', auth_views.login, name='register'),

    url(r'^logout/$', auth_views.logout, {'next_page': '/'}, name='logout'),

    url(r'^accounts/profile/$', views.profile, name='profile'),

    url(r'^wallets/$', views.wallets, name='wallets'),

    url(r'^results/(?P<wallet_id>[0-9]+)/$', views.results, name='results'),

    url(r'^createWallet/$', views.createWallet, name='createWallet'),

    url(r'^editWallet/$', views.editWallet, name='editWallet'),

    url(r'^saveWallet/(?P<wallet_id>[0-9]+)/$', views.editWallet, name='editWallet'),


]
