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
        return reverse('core:category',kwargs={
            'slug':self.slug
        })
    
 
class Product(models.Model):
    name=models.CharField(max_length=200)
    price=models.FloatField()
    discount_price=models.FloatField(blank=True,null=True)
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    description=models.TextField()
    image=models.ImageField(upload_to='product/',blank=False)
    slug = models.SlugField(default='my-product',unique=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("core:product",kwargs={
            'slug':self.slug
        })

    def save(self,*args,**kwargs):
        print("Save is called")
        super(Product,self).save(*args,**kwargs)


 
def unique_slug_generator(instance):
    constant_slug=slugify(instance.name)
    slug=constant_slug
    instanceClass=instance.__class__
    num=0
    while instanceClass.objects.filter(slug=slug).exists():
        num+=1
        slug=("{slug}-{num}".format(slug=constant_slug, num=num))
    return slug
    
def pre_save_reciever(sender,instance,*args,**kwargs):
    if not instance.slug:
        instance.slug=unique_slug_generator(instance)

pre_save.connect(pre_save_reciever,sender=Category)
pre_save.connect(pre_save_reciever,sender=Product)
 