from django.shortcuts import redirect, render
from django.views.generic import ListView
from .models import *
from .forms import ContactUsForm

class HomeView(ListView):
    template_name='index.html'

    def get(self, request):
        headertitle = HeaderTitle.objects.get()
        whatwedo = WhatWeDo.objects.get()
        features_1=Features.objects.all()
        gallery=Gallery.objects.all()
        testimonials=Testimonials.objects.get()
        aboutus=AboutUs.objects.all()
        countactuswithphone=CountactUsWithPhone.objects.get()
        

        context={
            'headertitle': headertitle,
            'whatwedo':whatwedo,
            'features_1':features_1,
            'gallery':gallery,
            'testimonials':testimonials,
            'aboutus':aboutus,
            'countactuswithphone': countactuswithphone,
                }

        return render(request,self.template_name,context)
    
    def post(self,request):
        contactus=ContactUsForm(request.POST)
        if contactus.is_valid():
            contactus.save()
            return redirect('home')
        else:
            return redirect('home')
    

