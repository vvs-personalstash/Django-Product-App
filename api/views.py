#from django.http import JsonResponse,HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
#import json
from product.models import Product
from product.serializers import ProductSerializer
from django.forms.models import model_to_dict


@api_view(["POST"])
def api_home(request,*arg,**karg):
    """
    Django Restful framework
    """
    serializer=ProductSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        #instance=serializer.save() #helps create an instance that reads our serializer   forms=instance.save()    
        print(serializer.data)
        data=serializer.data  #this doesnt create an instance
        return Response(data)
    return Response({'invalid': 'Data is not good'},status=400)
    # instance=Product.objects.all().order_by("?").first()
    # data={}
    # if instance:
    #   #data=model_to_dict(instance,fields=['id','title','price','SalesPrice'])
    #   #data_to_json=json.dumps(data)
    #     data=ProductSerializer(instance).data
 #request is an instance of httprequest class->django
    



# Create your views here.
# print(request.GET)   #Gives us url query params
#     print(request.POST) 
#     body=request.body  #this is a byte string of json i.e this will be in string like this  -> '{"query":"Hello World"}' i.e. content of string will be in json
#     data={}
#     try:
#       data=json.loads(body)
#     except:
#       pass
#     print(data.keys())
#     data['headers']=dict(request.headers) 
#     data['content_type']=request.content_type
#     data['params']=dict(request.GET)
#     print(body)
#     return JsonResponse(data)###
    