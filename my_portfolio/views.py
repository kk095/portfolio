from django.shortcuts import render,HttpResponse
from django.views.generic.edit import CreateView
from django .views.generic import TemplateView,ListView
from .forms import Contact_form
from .models import Skill,Image,About,Education,Social,Welcome,MyProject,Document
from portfolio.settings import EMAIL_HOST_USER
from django.core.mail import send_mail


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
    def form_valid(self, form):
        message=form.data.get('message')
        name=form.data.get('name')
        mail=form.data.get('email')
        msg=f"email of user is {mail}.\n message is \n\n '{message}'"
        send_mail(name,msg,EMAIL_HOST_USER,[EMAIL_HOST_USER],fail_silently=False)
        return super().form_valid(form)
    

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
    
    
    
    
    