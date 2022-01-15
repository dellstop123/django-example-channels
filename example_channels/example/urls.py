from django.urls import include,re_path
from example.views import log_in, log_out, sign_up, user_list


urlpatterns = [
    re_path(r'^log_in/$', log_in, name='log_in'),
    re_path(r'^log_out/$', log_out, name='log_out'),
    re_path(r'^sign_up/$', sign_up, name='sign_up'),
    re_path(r'^$', user_list, name='user_list')
]
