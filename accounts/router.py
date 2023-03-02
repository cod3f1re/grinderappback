from accounts.api.viewsets import UserViewSets
from rest_framework import routers

router = routers.DefaultRouter()
router.register('', UserViewSets)
