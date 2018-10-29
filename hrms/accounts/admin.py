from django.contrib import admin
from .models import Invoice,Bill, Quote,NDA,Aggriment,Payment
# Register your models here.

admin.site.register(Invoice)
admin.site.register(Bill)
admin.site.register(Quote)
admin.site.register(NDA)
admin.site.register(Aggriment)
admin.site.register(Payment)