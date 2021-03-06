from django.db import models
import sys
from PIL import Image
from io import BytesIO
from django.shortcuts import reverse
from django.utils.text import slugify
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.db.models.signals import pre_save

class CurrentOffer(models.Model):

    offerName=models.CharField(max_length=200)
    description=models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    percentage=models.PositiveIntegerField(default=0)
    offerImage=models.ImageField(upload_to='OfferImage/',blank=False,null=True)

    class Meta:
        ordering = ['created_on']
    def save(self,*args,**kwargs):
        if not self.id:
            self.offerImage=self.compressImage(self.offerImage)
            super(CurrentOffer,self).save(*args,**kwargs)
        
    def compressImage(self,offerImage):
        imageTemproary = Image.open(offerImage)
        outputIoStream = BytesIO()
        imageTemproaryResized = imageTemproary.resize( (1020,573) )
        imageTemproary.save(outputIoStream , format='JPEG', quality=60)
        outputIoStream.seek(0)
        offerImage= InMemoryUploadedFile(outputIoStream,'ImageField', "%s.jpg" % offerImage.name.split('.')[0], 'image/jpeg', sys.getsizeof(outputIoStream), None)
        return offerImage
        
    def __str__(self):
        return self.offerName



class Category(models.Model):
    name=models.CharField(max_length=200)
    categoryImage=models.ImageField(upload_to='categoryImage/',blank=False,null=True)
    slug=models.SlugField(default='my-category')
    


    def compressImage(self,categoryImage):
        imageTemproary = Image.open(categoryImage)
        outputIoStream = BytesIO()
        imageTemproaryResized = imageTemproary.resize( (1020,573) )
        imageTemproary.save(outputIoStream , format='JPEG', quality=60)
        outputIoStream.seek(0)
        categoryImage= InMemoryUploadedFile(outputIoStream,'ImageField', "%s.jpg" % categoryImage.name.split('.')[0], 'image/jpeg', sys.getsizeof(outputIoStream), None)
        return categoryImage
    
 
    def save(self,*args,**kwargs):
        self.categoryImage=self.compressImage(self.categoryImage)
        super(Category,self).save(*args,**kwargs)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return (self.slug)
 
class Product(models.Model):

    name=models.CharField(max_length=200)
    uploaded_by=models.IntegerField(null=False,default=0)
    uploaded_from=models.CharField(max_length=200)
    price=models.FloatField()
    discount_price=models.FloatField(blank=True,null=True)
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    description=models.TextField()
    image=models.ImageField(upload_to='product',blank=False)
    slug = models.SlugField(default='my-product',unique=False)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("core:product",kwargs={
            'slug':self.slug
        })
        
    def save(self,*args,**kwargs):
        super(Product,self).save(*args,**kwargs)



class UserProfile(models.Model):
    user=models.CharField(max_length=200)
    city=models.CharField(max_length=200)
    userImage=models.ImageField(upload_to='profile_image',blank=False)

    def __str__(self):
        return self.user
    
class Order(models.Model):
    PAYMENT_CHOICES=(
        ('B','Bkash'),
        ('R','Rocket'),
        ('N','Nogod'),
        ('U','Upay'),
    )
    ordered_by=models.IntegerField(default=0)
    product_id=models.IntegerField(default=0)
    location=models.CharField(max_length=200,null=False)
    contact=models.CharField(max_length=20,null=False,default='+8801')
    payment_method=models.CharField(max_length=1, choices=PAYMENT_CHOICES)
    transection_no=models.CharField(max_length=200)
    price=models.IntegerField(default=0)
    

    def __str__(self):
        return "paid_by "+self.payment_method

    def save(self,*args,**kwargs):
        super(Order,self).save(*args,**kwargs)
