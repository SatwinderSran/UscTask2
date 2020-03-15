from django.contrib import admin
from .models import Assembly,Packing,ShortageReport,Quote


admin.site.register(Assembly)
admin.site.register(Packing)
admin.site.register(ShortageReport)
admin.site.register(Quote)

   