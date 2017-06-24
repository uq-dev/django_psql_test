# coding: utf-8
from rest_framework import serializers

from .models import japan_ver81

class japan_ver81_Serializer(serializers.ModelSerializer):
	class Meta:
		model = japan_ver81
		fields = ('gid', 'jcode', 'ken', 'sicho', 'gun', 'seirei', 'sikuchoson', 'city_eng', 'p_num', 'h_num', 'geom')