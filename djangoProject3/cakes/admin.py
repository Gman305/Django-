from django.contrib import admin
from django.db.models import Count

from cakes.models import Cake,Baker
# Register your models here.

class CakeAdmin(admin.ModelAdmin):
    def has_change_permission(self, request, obj=None):
        return obj and obj.baker.user == request.user

    def save_model(self, request, obj, form, change):
        baker=Baker.objects.filter(user=request.user).first()
        baker_cakes=Cake.objects.filter(baker=baker).all()

        if not change and baker_cakes.count()==10:
            return

        sum=0

        for cake in baker_cakes:
            sum+=cake.price

        old_cake=baker_cakes.filter(id=obj.id).first()

        if not change and sum+obj.price>10000:
            return
        if change and sum+obj.price-old_cake.price>10000:
            return
        if Cake.objects.filter(id=obj.id).exists():
            return
        super(CakeAdmin,self).save_model(request, obj, form, change)



class BakerAdmin(admin.ModelAdmin):
    def get_queryset(self, request):
        qs=super(BakerAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs.annotate(cakes=Count('cake')).filter(cakes=5)
        return qs

    def has_add_permission(self, request):
        if request.user.is_superuser:
            return True
        else:
            return False

    def has_delete_permission(self, request, obj=None):
        if request.user.is_superuser:
            return True
        else:
            return False

    def has_change_permission(self, request, obj=None):
        if request.user.is_superuser:
            return True
        else:
            return False

admin.site.register(Cake,CakeAdmin)
admin.site.register(Baker,BakerAdmin)