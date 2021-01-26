from django.shortcuts import render
from django.views.generic import ListView , DetailView
from .models import Property 
from .forms import PropertyBookForm
from django.shortcuts import redirect
from .filter import ProertyFilter
# Create your views here.
from django.views.generic.edit import FormMixin
from django_filters.views import FilterView




class PropertyList(FilterView):
    model = Property
    paginate_by = 1
    filterset_class = ProertyFilter
    template_name = 'property/property_list.html'

class PropertyDetail(FormMixin,DetailView):
    model = Property
    form_class = PropertyBookForm

    def get_context_data(self, **kwargs):
        context = super(PropertyDetail, self).get_context_data(**kwargs)
        context['related'] = Property.objects.filter(category=self.get_object().category)[:2]
        return context

    def post(self,request,*args,**kwargs):
        form = self.get_form()
        if form.is_valid():
            myform = form.save(commit=False)
            myform.property = self.get_object()
            myform.author = request.user
            myform.save()
        return redirect('/')