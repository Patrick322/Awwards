from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^search/$', views.search_project, name='search_project'),
    url(r'^profile/$', views.profile_info, name='profile_info'),
    url(r'^projects/$', views.new_projects, name='new_projects'),
    url(r'^project/(\d+)$', views.single_project, name='project'),
    url(r'^rating/(\d+)$', views.review_rating, name="review")


    

]
   
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)