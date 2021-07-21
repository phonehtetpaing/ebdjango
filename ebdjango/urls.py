"""ebdjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples: Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from boards import views
from django.conf import settings
from django.views.i18n import JavaScriptCatalog
from apps.core.views.vendor_common import index
from apps.core.views.vendor_common.media import document_view

urlpatterns = [
    #test 
    path('hello/<name>', views.hello),
    path('savetodb/<name>', views.saveToDb),

    #translations
    path('i18n/', include('django.conf.urls.i18n')),
    path('jsi18n/', JavaScriptCatalog.as_view(), name='javascript-catalog'),
    #django
    path('admin/', admin.site.urls),
    path('google/', include(('apps.core.urls.google_api_urls', 'google_api'), namespace='google_api')),
    path('api/', include(('apps.core.urls.api_urls', 'google_api'), namespace='api')),
    path('smartsec/', include(('apps.core.urls.smart_sec_urls', 'smart_sec'), namespace='smart_sec')),
    path('magicbot/', include(('apps.core.urls.smart_sec_urls', 'magicbot'), namespace='magicbot')),
    # connect
    path('connect/', include(('apps.core.urls.connect_urls', 'connect'), namespace='connect')),
    # ContactChat
    path('contactchat/', include(('apps.core.urls.contactchat_urls', 'contactchat'), namespace='contactchat')),
    path('', index.index),
    path('health/', include('health_check.urls')),
    path('css/<access_url>/', document_view, name='media'),
]

handler500 = 'apps.core.views.vendor_common.error.view_500'
handler404 = 'apps.core.views.vendor_common.error.view_404'
handler403 = 'apps.core.views.vendor_common.error.view_403'

if settings.DEBUG:
    urlpatterns.append(path('sample/', include(('apps.core.urls.sample_urls', 'sample'), namespace='sample')))
    urlpatterns.append(path('recome/', include(('apps.core.urls.recome_urls', 'recome'), namespace='recome')))

    import debug_toolbar
    urlpatterns.append(path('__debug__/', include(debug_toolbar.urls)))
