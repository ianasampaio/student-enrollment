from django.views.generic import ListView,DetailView, CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy
from .models import Student

class List_students(ListView):
    model = Student
    template_name = "student_list.html"
    paginate_by = 10

    def get_queryset(self):
        txt_name = self.request.GET.get('name')

        if txt_name:
            registers = Student.objects.filter(name__icontains=txt_name)
        else:
            registers = Student.objects.all()
        return registers

class Detail_students(DetailView):
    model = Student 
    template_name = "student_view.html"

class Create_students(CreateView):
    model = Student
    fields = '__all__'
    template_name = "student_create.html"
    success_url = reverse_lazy('list_students')

class Update_students(UpdateView):
    model = Student
    fields = '__all__'
    template_name = "student_update.html"
    success_url = reverse_lazy('list_students')

class Delete_students(DeleteView):
    model = Student
    template_name = "student_confirm_delete.html"
    context_object_name = 'student'
    success_url = reverse_lazy('list_students')
