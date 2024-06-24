from rest_framework import viewsets,mixins

from .models import Product
from .serializers import ProductSerializer
#dont use view sets ie. no use
class ProductViewSet(viewsets.ModelViewSet):
    '''get->list->queryset
       get->retrieve an item -> Prodct instance Detail View
       post-> create -> new instance
       put -> update
       patch -> partial update
       delete -> destroy
    
    '''
    queryset =Product.objects.all()
    serializer_class=ProductSerializer
    lookup_field= 'pk' #default

class ProductGenericViewSet(mixins.ListModelMixin,mixins.RetrieveModelMixin,viewsets.GenericViewSet):
    '''get->list->queryset
       get->retrieve an item -> Prodct instance Detail View
    
    '''
    queryset =Product.objects.all()
    serializer_class=ProductSerializer
    lookup_field= 'pk' #default

    # we can write view for this like
    # product_list_view=ProductGenericViewSet.as_view({'get': 'list'})
    # product_detail_view=ProductGenericViewSet.as_view({'get': 'retrieve'})
    # and call them in urls diretly instead of routers like our class based views