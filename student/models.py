import uuid
from django.db import models

class Subject(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "Subjects"

    def __str__(self):
        return self.name

class Situation(models.Model):
    choices = (
        ('Undegraduate', 'Undegraduate'),
        ('Leave of absence', 'Leave of absence'),
        ('Graduate', 'Graduate')
    )
    status = models.CharField('Situation',max_length=20, choices=choices, blank=False, null=False)
    
    class Meta:
        verbose_name = "Situation"
        verbose_name_plural = "Situations"

    def __str__(self):
        return self.status

class Student(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name  = models.CharField(max_length=100)
    subject = models.ForeignKey(Subject,on_delete=models.CASCADE)
    status = models.ForeignKey(Situation,verbose_name='Situation',on_delete=models.CASCADE)
    beginSemester =  models.PositiveIntegerField('Admission semester',blank=False, null=False)
    endSemester =  models.PositiveIntegerField('Final semester',blank=True, null=True)

    class Meta:
        verbose_name_plural = "Students"

    def __str__(self):
        return self.name

    # def getSubject(self):

    #     subject = self.student_set.values('subject__name','status__status').all()
    #     # return subject
    #     situationSubject = [value['subject__name'] for value in subject if value['status__status'] == 'Undegraduate' or value['status__status'] == 'Leave of absence']

    #     txtSubjects = [value for value in situationSubject] 
    #     return txtSubjects
        
    # getSubject.short_description = 'subjects'    



# class student(models.Model):
#     subject = models.ForeignKey(Subject,on_delete=models.CASCADE)
#     student = models.ForeignKey(Student,on_delete=models.CASCADE)
#     status = models.ForeignKey(Situation,verbose_name='Situation',on_delete=models.CASCADE)
#     beginSemester =  models.PositiveIntegerField('Admission semester',blank=False, null=False)
#     endSemester =  models.PositiveIntegerField('Final semester',blank=True, null=True)

#     class Meta:
#         verbose_name = "student"
#         verbose_name_plural = "students"
#         ordering = ["-endSemester"]
    
#     def __str__(self):
#         return str(self.student) + ' , ' + str(self.subject)
