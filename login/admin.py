from django.contrib import admin
from models import *
from p import *
actions = ['delete_selected']



class AuthorAdmin(admin.ModelAdmin):

    actions = ['delete_selected']	
    def delete_selected(self, request, obj):
    	print 'how r u ?'
    	print '^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^	'		
    	for o in obj.all():
		print '&&&&&&&&&&&&&&&&&&&&&&'
		print o.mac
		
		remove_element(o.mac)
        	o.delete()
	
    pass
admin.site.register(Access, AuthorAdmin)
# Register your models here.

