from django.contrib import admin
from .models import CustomUser, Patient  # Импортируйте все модели

@admin.register(CustomUser)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'email', 'role', 'is_staff')
    list_filter = ('role', 'is_staff', 'is_active')
    search_fields = ('username', 'email', 'role')

@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ('id', 'date_of_birth', 'created_at')
    list_filter = ('date_of_birth', 'created_at')
    search_fields = ('id',)