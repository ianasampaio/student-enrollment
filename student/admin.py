from django.contrib import admin

from .models import Student,Subject,Situation

class SubjectAdmin(admin.ModelAdmin):
    fields = ['name']

admin.site.register(Subject,SubjectAdmin)

class SituationAdmin(admin.ModelAdmin):
    fields = ['status']

admin.site.register(Situation,SituationAdmin)

# class studentInline(admin.TabularInline):
#     model = student
#     extra = 2

#     # list_display = ('name','Subject','status','beginSemester','endSemester')

class StudentAdmin(admin.ModelAdmin):
    model = Student

    # list_display = ('name','getSubject')
    # inlines = [studentInline]
admin.site.register(Student, StudentAdmin)
