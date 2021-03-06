from django.urls import path
from .views import Home,Contact,SkillListView,Project

urlpatterns = [
    path('',Home.as_view(),name='name'),
    path('contact',Contact.as_view(),name='contact'),
    path('about',SkillListView.as_view(),name='about'),
    path('project<slug:all>',Project.as_view(),name='project')
]
