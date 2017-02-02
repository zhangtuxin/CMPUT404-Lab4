from django.conf.urls import url
from . import views
# $ means end of the string
urlpatterns = [
    url(r'^$',views.index, name = 'index'),
    url(r'^(?P<question_id>[0-9]+)/$',views.detail, name = 'detail'),
    url(r'^(?P<question_id>[0-9]+)/vote/$',views.vote, name = 'vote'),
    url(r'^(?P<question_id>[0-9]+)/results/$',views.results, name = 'results'),
    ]