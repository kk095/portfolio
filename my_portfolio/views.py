from django.shortcuts import render,HttpResponse
from django.views.generic.edit import CreateView
from django .views.generic import TemplateView,ListView
from .forms import Contact_form
from .models import Skill,Image,About,Education,Social,Welcome,MyProject,Document


# Create your views here.
class Home(TemplateView):
    template_name='home.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["text"] = Welcome.objects.all()[0]
        return context
    

class Contact(CreateView):
    form_class=Contact_form
    template_name='contact.html'
    success_url='/'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["social"] = Social.objects.all()
        return context
    

class SkillListView(ListView):
    model = Skill
    template_name = "about.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["about"] =  About.objects.all()
        context['image'] = Image.objects.all()[0]
        context['edu'] = Education.objects.all()
        context['resume'] = Document.objects.all()[0]

        return context
    



class Project(ListView):
    template_name='project.html'
    def get_queryset(self):
        lang=self.kwargs['all']
        if lang!='all':
            queryset=MyProject.objects.filter(lang=lang)
        else:
            queryset=MyProject.objects.all()
        return queryset
    
    
    
    
    