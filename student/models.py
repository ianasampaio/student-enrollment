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
