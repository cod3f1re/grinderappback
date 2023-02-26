from users.viewsets import UserViewSets
from rest_framework import routers

router = routers.DefaultRouter()
router.register('users', UserViewSets)
