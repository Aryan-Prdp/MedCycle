from django.contrib import admin
from .models import NGO, Medicine, Donation

# ------------------------------
# Register Models in Admin Panel
# ------------------------------

@admin.register(NGO)
class NGOAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'latitude', 'longitude')


@admin.register(Medicine)
class MedicineAdmin(admin.ModelAdmin):
    list_display = ('name', 'user', 'quantity', 'expiry_date', 'donated')
    list_filter = ('donated', 'expiry_date')


@admin.register(Donation)
class DonationAdmin(admin.ModelAdmin):
    list_display = ('medicine', 'ngo', 'user', 'status', 'created_at')
    list_filter = ('status', 'created_at')



