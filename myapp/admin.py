from django.contrib import admin
from .models import vets
from .models import products
from .models import userProfile
# Register your models here.

class VetsAdmin(admin.ModelAdmin):
    list_display= ('vName', 'vAddress', 'vPhone', 'vLocation','vLink')
    
admin.site.register(vets, VetsAdmin)

class ProfileAdmin(admin.ModelAdmin):
    list_display= ('name', 'phone', 'address', 'catName','catAge', 'catBreed', 'profilePic', 'catImg')
    
admin.site.register(userProfile, ProfileAdmin)


