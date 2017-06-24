# coding: utf-8
from rest_framework import routers

from .views import japan_ver81_VewSet

router = routers.DefaultRouter()
router.register(r'japan_ver81', japan_ver81_VewSet)
