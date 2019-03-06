# -*- coding: utf-8 -*-

from django.conf.urls import patterns

urlpatterns = patterns(
    'home_application.views',
    (r'^$', 'home'),
    # (r'^dev-guide/$', 'dev_guide'),
    # (r'^contactus/$', 'contactus'),
    (r'^test/$', 'test_exam'),
    (r'^task/$', 'task'),
    (r'^task_record/$', 'task_record'),
    (r'^get_ip/$', 'get_ip'),
    (r'^get_job/$', 'get_job'),

)
