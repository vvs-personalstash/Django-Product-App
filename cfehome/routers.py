from rest_framework.routers import DefaultRouter

from product.viewsets import ProductViewSet,ProductGenericViewSet

router=DefaultRouter()
router.register('products-abc',ProductViewSet,basename='products')
print(router.urls)
urlpatterns=router.urls