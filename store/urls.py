from rest_framework.routers import DefaultRouter

from store.apps import StoreConfig
from store.views import RetailViewSet, ProductViewSet, ContactViewSet

app_name = StoreConfig.name

retail_router = DefaultRouter()
retail_router.register(r"retails", RetailViewSet, basename="retails")

product_router = DefaultRouter()
product_router.register(r"products", ProductViewSet, basename="products")

contact_router = DefaultRouter()
contact_router.register(r"contacts", ContactViewSet, basename="contacts")

urlpatterns = [] + retail_router.urls + product_router.urls + contact_router.urls
