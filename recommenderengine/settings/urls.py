from django.conf.urls import patterns, include, url

# Static files for development
from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'settings.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'', include('apps.recommender.urls')),
) \
              # + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)  # Static files for development
