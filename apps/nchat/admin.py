from django.contrib import admin

# Register your models here.
# most models should be administered through the service directly and not the admin
from apps.nchat.models.business import Business
admin.site.register(Business)
from apps.nchat.models.vendor_user import VendorUser
admin.site.register(VendorUser)
