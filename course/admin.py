from django.contrib import admin
from course.models import Course, Deadline, Group, Update, GroupMember, CourseMember

# Register your models here.
class CourseAdmin(admin.ModelAdmin):
	list_display = ['id', 'name', 'last_date', 'owner', 'modified', 'created']

class DeadlineAdmin(admin.ModelAdmin):
	list_display = ['id', 'name', 'course', 'date_due', 'maker', 'modified', 'created']

class GroupAdmin(admin.ModelAdmin):
	list_display = ['id', 'name', 'description', 'modified', 'created']

class UpdateAdmin(admin.ModelAdmin):
	list_display = ['id', 'text', 'user', 'course', 'group', 'modified', 'created']

class GroupMemberAdmin(admin.ModelAdmin):
	list_display = ['id', 'group', 'user', 'modified', 'created']

class CourseMemberAdmin(admin.ModelAdmin):
	list_display = ['id', 'course', 'user', 'modified', 'created']

admin.site.register(Course, CourseAdmin)
admin.site.register(Deadline, DeadlineAdmin)
admin.site.register(Group, GroupAdmin) 
admin.site.register(Update, UpdateAdmin)
admin.site.register(GroupMember, GroupMemberAdmin)
admin.site.register(CourseMember, CourseMemberAdmin)