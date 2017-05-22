"""School URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin

from School import settings

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', 'main.views.index_view', name='index'),
    url(r'^about/', 'main.views.about_view', name='about'),
    url(r'^information/', 'main.views.information_view', name='info'),
    url(r'^contacts/', 'main.views.contacts_view', name='contacts'),
    url(r'^teachers/', 'main.views.teachers_view', name='teachers'),
    url(r'^profile/', 'main.views.profile_view', name='profile'),
    url(r'^teacher/(?P<id>\d+)/$', 'main.views.single_teacher', name='single_teacher'),

]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
