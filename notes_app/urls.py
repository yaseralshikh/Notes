from django.conf.urls import url
from . import views

app_name = 'note_app'
urlpatterns = [
    url(r'^$', views.all_notes, name='all_notes'),
    # url(r'^(?P<id>\d+)$', views.detail, name='note_detail'),
    url(r'^(?P<slug>[-\w]+)/$', views.detail, name='note_detail'),
    url(r'^add$', views.note_add, name='note_add'),
    url(r'^(?P<slug>[-\w]+)/edit$', views.note_edit, name='note_edit'),
    url(r'^(?P<slug>[-\w]+)/delete$', views.note_delete, name='note_delete'),
]
