from django.db import models

# Create your models here.
class japan_ver81(models.Model):
	gid = models.IntegerField(primary_key=True)
	jcode = models.CharField(max_length=5)
	ken = models.CharField(max_length=10)
	sicho = models.CharField(max_length=20)
	gun = models.CharField(max_length=20)
	seirei = models.CharField(max_length=20)
	sikuchoson = models.CharField(max_length=50)
	city_eng = models.CharField(max_length=50)
	p_num = models.IntegerField()
	h_num = models.IntegerField()
	geom = models.BinaryField()

	class Meta:
		db_table = 'japan_ver81'