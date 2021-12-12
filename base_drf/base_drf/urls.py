from django.contrib import admin

#from django.urls import path

from django.conf.urls import url, include

from django.conf import settings

from django.conf.urls.static import static, serve

from rest_framework.schemas import get_schema_view

from rest_framework_swagger.renderers import SwaggerUIRenderer, OpenAPIRenderer

schema_view = get_schema_view(title='Users API', renderer_classes=[OpenAPIRenderer, SwaggerUIRenderer])


urlpatterns = [

    url(r'^admin/', admin.site.urls),

    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    url(r'^rest-auth/', include('rest_auth.urls')),

    url(r'^rest-auth/registration/', include('rest_auth.registration.urls')),

    url(r'^docs/', schema_view, name="docs"),

    url(r'api/', include("base_drf.api.urls"), name='api'),

]



if settings.DEBUG:

   urlpatterns += [

       url(r'^media/(?P<path>.*)$', serve, {

           'document_root': settings.MEDIA_ROOT,

       }),

       url(r'^static/(?P<path>.*)$', serve, {

           'document_root': settings.STATIC_ROOT

       })

   ]





