from django.contrib import admin

from usuarios.models import Usuario

# Register your models here.
admin.site.register(Usuario)


# # CAMPOS QUE SE PUEDEN MODIFICAR
# class AutorAdmin(admin.ModelAdmin):
#     fields = ["Nombre","Apellido","Nacionalidad"]
#     list_display = ["Nombre","Apellido"]
    
# admin.site.register(AutorDB,AutorAdmin)

# @admin.register(FraseDB)
# class FraseAdmin(admin.ModelAdmin):
#     fields = ["cita","autor_fk"]
#     list_display = ["cita"]