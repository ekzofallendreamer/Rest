from rest_framework import routers

from .views import BookView, AuthorView

router = routers.DefaultRouter()
router.register(r'books', BookView)
router.register(r'authors', AuthorView)

urlpatterns = router.urls
