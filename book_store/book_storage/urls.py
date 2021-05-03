from django.urls import path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.routers import SimpleRouter

from .views import BookModelViewSet


class OptionalSlashRouter(SimpleRouter):

    def __init__(self):
        super().__init__()
        self.trailing_slash = '/?'


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
router = OptionalSlashRouter()
router.register('books', BookModelViewSet)

urlpatterns = [
    path(r'swagger', schema_view.with_ui('swagger', cache_timeout=0),
         name='schema-swagger-ui'),
    path('', include(router.urls)),
    path('token-auth/', obtain_auth_token, name='token_auth'),
]
