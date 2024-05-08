from rest_framework.routers import DefaultRouter
from .views import PersonaViewSet

router = DefaultRouter()
router.register(r'personas', PersonaViewSet)

urlpatterns = router.urls
