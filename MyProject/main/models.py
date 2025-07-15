from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

class HeaderTitle(models.Model):
    title=models.CharField('title',max_length=100)
    subtitle=models.TextField(verbose_name='Subtitle')

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name='Header Title'
        verbose_name_plural='Header Titles'

class WhatWeDo(models.Model):
    main_text=models.TextField('Main Text')
    link_text=models.CharField('Link Text' , max_length=255)
    link_url=models.URLField('Link Url')

    def __str__(self):
         return self.main_text
        
class Features(models.Model):
    icon=models.CharField('Icon',max_length=50)
    title=models.CharField('Title',max_length=100)
    description=models.TextField('Description')

    def __str__(self):
        return self.title
    
    class Meta:
         verbose_name='Feature'
         verbose_name_plural='Features'

class Gallery(models.Model):
    image=models.ImageField('Image', upload_to='gallery/')
    title=models.CharField('Title',max_length=100)
    image_2=models.ImageField('Image_2',upload_to='gallery/')

    def __str__(self):
        return f'Gallery Image {self.id}'
    
    class Meta:
         verbose_name='Gallery Image'
         verbose_name_plural='Gallery Images'

        

class ContactUs(models.Model):
    name=models.CharField('Name',max_length=100)
    email=models.EmailField('Email')
    message=models.TextField('Message')

    def __str__(self):
        return f"Contact from {self.name}"
    
    class Meta:
         verbose_name='Contact Us'
         verbose_name_plural='Contacts Us'

class Testimonials(models.Model):
    title=models.CharField('Testimonials Text',max_length=255)
    text=models.TextField('Text')

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name='Testimonial'
        verbose_name_plural='Testimonials'

class AboutUs(models.Model):
    img=models.ImageField('Image',upload_to='about/')
    text=models.TextField('Text')
    name=models.CharField('Name',max_length=100)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name='About Us'
        verbose_name_plural='About Us'

class CountactUsWithPhone(models.Model):
    chat=models.CharField('Chat',max_length=100)
    email=models.EmailField('Email')
    location=models.CharField('Location',max_length=255)
    phone=PhoneNumberField('Phone Number')

    def __str__(self):
        return f'Contact Info {self.chat}'
    
    class Meta:
        verbose_name='Countact Us with phone'
        verbose_name_plural='Countacts Us with phone'