from django.conf.urls import url
from .views import index, center, disciplines, courses, teachers, discipline, \
    coursesDisc, course, teacher, courThemes, theme

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^center$', center, name='center'),
    url(r'^disc$', disciplines, name='disc'),
    url(r'^courses$', courses, name='courses'),
    url(r'^teachers$', teachers, name='teachers'),
    url(r'^discipline/(?P<disc_id>\d+)$', discipline, name='discipline'),
    url(r'^coursesDisc/(?P<disc_id>\d+)$', coursesDisc, name='coursesDisc'),
    url(r'^course/(?P<cour_id>\d+)$', course, name='course'),
    url(r'^teacher/(?P<teach_id>\d+)$', teacher, name='teacher'),
    url(r'^courThemes/(?P<cour_id>\d+)$', courThemes, name='courThemes'),
    url(r'^theme/(?P<theme_id>\d+)$', theme, name='theme'),
]
