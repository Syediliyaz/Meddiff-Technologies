from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', 'student_data.views.index', name='index'),
]