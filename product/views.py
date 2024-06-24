from rest_framework import generics, mixins
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import Http404
from .models import Product
from .serializers import ProductSerializer
from django.shortcuts import get_object_or_404
from api.mixins import StaffEditorPermissionMixin,UserQuerySetMixin


class ProductListCreateAPIView(UserQuerySetMixin,StaffEditorPermissionMixin, generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    allow_staff_view = False
    # authentication_classes=[authentication.SessionAuthentication,
    #                         TokenAuthentication]
    # permission_classes=[permissions.IsAdminUser, IsStaffEditorPermission]
     
    def perform_create(self, serializer):
        # print("1")
        # email=serializer.validated_data.pop('email')
        # print(email)
        title = serializer.validated_data.get("title")
        content = serializer.validated_data.get("content") or None
        if content is None:
            content = title
        serializer.save(user=self.request.user, content=content)

    # def get_queryset(self,*args,**kwargs):
    #     qs=super().get_queryset(*args,**kwargs)
    #     request=self.request
    #     user=request.user
    #     if not user.is_authenticated:
    #         return Product.objects.none
    #     return qs.filter(user=user)


product_list_create_view = ProductListCreateAPIView.as_view()


class ProductDetailApiView(UserQuerySetMixin,StaffEditorPermissionMixin, generics.RetrieveAPIView):
    # permission_classes=[permissions.IsAdminUser, IsStaffEditorPermission]
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # lookup_field= pk (primary key)


product_detail_view = ProductDetailApiView.as_view()


class ProductDestroyApiView(UserQuerySetMixin,StaffEditorPermissionMixin, generics.DestroyAPIView):
    # permission_classes=[permissions.IsAdminUser, IsStaffEditorPermission]
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    # lookup_field= pk (primary key)
    def perform_destroy(self, instance):
        super().perform_destroy(instance)


product_destroy_view = ProductDestroyApiView.as_view()


class ProductUpdateApiView(UserQuerySetMixin,StaffEditorPermissionMixin, generics.UpdateAPIView):
    # permission_classes=[permissions.IsAdminUser, IsStaffEditorPermission]
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = "pk"  # (primary key)

    def perform_update(self, serializer):
        instance = serializer.save()
        if not instance.content:
            instance.content = instance.title
            serializer.save()


product_update_view = ProductUpdateApiView.as_view()


# "Not gonna use this method instead just change create api view to list api vieew"
# class ProductListApiView(generics.ListAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer
class ProductMixinView(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    generics.GenericAPIView,
):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = "pk"

    def get(self, request, *args, **kwargs):  # Http->get
        pk = kwargs.get("pk")
        if pk is not None:
            return self.retrieve(request, *args, **kwargs)
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def perform_create(self, serializer):
        title = serializer.validated_data.get("title")
        content = serializer.validated_data.get("content")

        if content is None:
            content = "This is a single view doing cool stuff"
        serializer.save(content=content)


product_mixin_view = ProductMixinView.as_view()


# product_list_view = ProductListApiView.as_view()


# you can do the above 3/2 (as 1 is useless) methods with a single view like this but doing this is not recomended so dont use function based views instead use class based views like above
@api_view(["GET", "POST"])
def product_alt_view(request, pk=None, *args, **kwargs):
    method = request.method
    if method == "GET":
        if pk is not None:
            # queryset=Product.objects.filter(pk=pk)
            #    if not queryset.exists():
            #          raise Http404
            object = get_object_or_404(Product, pk=pk)
            serialzer = ProductSerializer(object, many=False).data
            # this means this will be a detail view
            return Response(serialzer)
        # get request -> detail view
        queryset = Product.objects.all()
        data = ProductSerializer(queryset, many=True).data
        return Response(data)
    if method == "POST":
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            title = serializer.validated_data.get("title")
            content = serializer.validated_data.get("content")
            if content is None:
                content = title
            serializer.save(content=content)
            return Response(serializer.data)
        return Response({"invalid": "Data is not good"}, status=400)
