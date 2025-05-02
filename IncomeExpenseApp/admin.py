from django.contrib import admin
from .models import Income,Expense,UserProfile,User
# Register your models here.
admin.site.register(UserProfile)
admin.site.register(Income)
admin.site.register(Expense)
