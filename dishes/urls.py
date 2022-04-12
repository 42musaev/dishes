from dishes.views import FoodView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'foods', FoodView, basename='food')
urlpatterns = router.urls
