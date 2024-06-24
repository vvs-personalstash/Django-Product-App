from rest_framework import serializers
from rest_framework.reverse import reverse

from .models import Product
from .validators import hello_not_allowed , unique_product_title

class ProductSerializer(serializers.ModelSerializer):
    MY_discount=serializers.SerializerMethodField(read_only=True)
    edit_url=serializers.SerializerMethodField(read_only=True) #works anywhere
    url=serializers.HyperlinkedIdentityField(view_name='products-detail',
                                             lookup_field='pk')#works in model serializer
#     email=serializers.EmailField(write_only=True)
    title=serializers.CharField(validators=[hello_not_allowed,unique_product_title])#validate_title])  //EmailField to check if its a valid email form or not
#    name=serializers.CharField(source='title')
    class Meta:
        model=Product
        fields=[
            'pk',
            'edit_url',
           # 'email',
           # 'user',
            'url',
           # 'name',
            'title',
            'content',
            'price',
            'SalesPrice',
            'MY_discount'
        ]
#     def validate_title(self,value):
#          request=self.context.request   #if in view we need to do this simply do self.request
#          user=request.user
#          qs= Product.objects.filter(user=user,title__exact=value)
#          if qs.exists():
#             raise serializers.ValidationError(f"{value} already exists")
#          return value
#     def create(self,validated_data):
#          #return Product(**validated_data)
#          #email=validated_data.pop('email')
#          obj= super().create(validated_data)
#         # print(email,obj)
#          return obj
#     def update(self,instance,validated_data):
#          email=validated_data.pop('email')
#          return super().update(instance,validated_data)
#          #instance.title=validated_data.get('title')
#          return instance
    def get_edit_url(self,obj):
         # returnf"/api/v2/products/{obj.pk}/"
         request = self.context.get("request") # self.request
         if request is None:
              return None
         return reverse("products-edit",kwargs={"pk": obj.pk},request=request)
    def get_MY_discount(self,obj):
           if not hasattr(obj,'id'):
                return None
           if not isinstance(obj,Product):
                return None
           return obj.GetDiscount()
