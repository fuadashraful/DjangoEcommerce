from django.db import models
import sys
from PIL import Image
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile
# Create your models here.
# for image compressing https://github.com/gajeshbhat/django-experiments/blob/master/Upload-compress/Compress/models.py

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
    
    def save(self,*args,**kwargs):
        if not self.id:
            self.categoryImage=self.compressImage(self.categoryImage)
            super(Category,self).save(*args,**kwargs)


    def compressImage(self,categoryImage):
        imageTemproary = Image.open(categoryImage)
        outputIoStream = BytesIO()
        imageTemproaryResized = imageTemproary.resize( (1020,573) )
        imageTemproary.save(outputIoStream , format='JPEG', quality=60)
        outputIoStream.seek(0)
        categoryImage= InMemoryUploadedFile(outputIoStream,'ImageField', "%s.jpg" % categoryImage.name.split('.')[0], 'image/jpeg', sys.getsizeof(outputIoStream), None)
        return categoryImage
    

    def __str__(self):
        return self.name
    
        

