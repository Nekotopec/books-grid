from django.urls import path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from rest_framework.routers import SimpleRouter
from .views import BookModelViewSet

# Swagger.
api_info = openapi.Info(
    title="Books api",
    default_version='v1',
    description="Description",
)

schema_view = get_schema_view(
    api_info,
    public=True,
    permission_classes=(permissions.AllowAny,),
)

# Routers.
router = SimpleRouter()
router.register('books', BookModelViewSet)

urlpatterns = [
    path(r'swagger', schema_view.with_ui('swagger', cache_timeout=0),
         name='schema-swagger-ui'),
    path('api/', include(router.urls))
]
