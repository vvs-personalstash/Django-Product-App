from django.db import models
from django.conf import settings
User=settings.AUTH_USER_MODEL

class Product(models.Model):
      user=models.ForeignKey(User,on_delete=models.SET_NULL,default=1,null=True)
      title=models.CharField(max_length=120,)
      content=models.TextField(null=True,blank=True)
      price=models.DecimalField(max_digits=15,decimal_places=2,default=99.99)
      @property
      def SalesPrice(self):
            return "%.2f"%(float(self.price)*.8)
      def GetDiscount(self):
            return "122"