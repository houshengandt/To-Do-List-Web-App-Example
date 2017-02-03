from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'todolist_project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^', include('todolist.urls')),
    url(r'^admin/', include(admin.site.urls)),
]