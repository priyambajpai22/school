from django.shortcuts import render
from datetime import datetime
from django.views.generic import View,TemplateView,ListView,DetailView,UpdateView,FormView
from .models import StudentForm
from django.http import HttpResponse
from django.http import JsonResponse
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.contrib.auth import authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Student,Fee,Content,ContactForm,Contact,Contact,ContentForm
from django.db.models import Sum
import json
from django.http import JsonResponse
from django.urls import reverse
from .models import Common
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
	

class ContactView(SuccessMessageMixin,FormView):
	template_name='contact.html'
	form_class=ContactForm
	success_message='enquiry submitted successfully'
	def get_success_url(self):
		return self.request.path
	

class Enquiry(LoginRequiredMixin,ListView):
	template_name='enquiry.html'
	model=Contact
	context_object_name = 'object'
	
		

class Index(TemplateView):
	template_name='index.html'

	def get(self,request):
	
		return render(request,self.template_name,{'object':Content.objects.all()})
	


from django.http import JsonResponse
from django.views.generic.edit import CreateView

	

class AdminPannel(LoginRequiredMixin,View):
	template_name='sid.html'

	def get(self,request):
		student_form=StudentForm()
		return render(request,self.template_name,{'form':student_form})

	def post(self,request):
			form=StudentForm(request.POST)
			if form.is_valid():
					form.save()
					messages.success(request, 'Form submission successful')
					return redirect('golu')
			else:
				return redirect("golu")


class Deshboard(LoginRequiredMixin,SuccessMessageMixin,ListView):
	template_name='data.html'
	model=Student
	context_object_name = 'object'
	success_message = "form created successfully"

class FeeDetails(LoginRequiredMixin,SuccessMessageMixin,View):
	template_name='feedata.html'
	def get(self,request,pk):
		#import pdb;pdb.set_trace()
		instance=Student.objects.get(id=pk)
		name=Fee.objects.filter(student=instance)
		if name:
			money=Fee.objects.filter(student=instance).aggregate(Sum('installment'))
			remain=int(instance.fee)-int(money['installment__sum'])
			print(remain)
			print(money)
			return render(request,self.template_name,{'name':name,'money':money})
		else:
			return render(request,self.template_name)
	def post(self,request,pk):
		instance=Student.objects.get(id=pk)
		fee=request.POST.get('add')
		k=Fee(installment=fee,student=instance)
		k.save()
		return redirect('fee',pk=pk)

'''class View(LoginRequiredMixin,View):

	template_name='index.html'
	def get(self,request):


		return render(request,self.template_name)

	def post(self,request,pk):
		new=Student.objects.get(id=pk)
		k=Fee(fee=request.POST.get('add'),instance=new)

		return HttpResponse('ok working')
'''
class ContentView(LoginRequiredMixin,SuccessMessageMixin,UpdateView):
	template_name='addcontent.html'
	model=Content
	fields='__all__'
	success_message = "form created successfully"
	def get_success_url(self):
            return reverse('content', kwargs={'pk': self.object.id})

	





	



	
