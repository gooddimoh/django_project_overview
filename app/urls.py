from rest_framework import routers
from django.conf.urls import url
from django.contrib.staticfiles.views import serve
from django.views.generic import RedirectView
from .viewsets import ProductViewSet, ProductTypeViewSet, ProductCategoryViewSet, StandardViewSet, StandardCategoryViewSet, StandardRequirementViewSet, KeyWordViewSet
from .views import products, standards

router = routers.SimpleRouter()

router.register('product', StandardViewSet)
router.register('product_type', ProductTypeViewSet)
router.register('product_category', ProductCategoryViewSet)

router.register('standard', StandardViewSet)
router.register('standard_requirement', StandardRequirementViewSet)
router.register('standard_category', StandardCategoryViewSet)

router.register('keyword', KeyWordViewSet)
routes = router.urls

routes.extend([
    url('products_list', products),
    url('standards_list', standards)
])

urlpatterns = routes





