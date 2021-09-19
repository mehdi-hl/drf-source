from django.urls import path,include
from .views import UseViewSet,AticleViewSet
from rest_framework import routers

app_name = "api"

router = routers.SimpleRouter()
router.register('articles', AticleViewSet, basename="articles")
router.register('users', UseViewSet, basename="users")
# urlpatterns = router.urls

urlpatterns = [
    # path("", ArticleList.as_view(),name="list"),
    # path("<int:pk>", ArticleDetail.as_view(),name="detail"),
    # path("users/", UserList.as_view(),name="user-list"),
    # path("users/<int:pk>", UserDetail.as_view(),name="user-detail"),
    path("",include(router.urls)),


]
