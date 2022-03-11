from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from products.models import Product
from .serializer import ProductSerializer

class ProductAV(APIView):
    
    """
    place all the relevant methods here

    """

    def get(self, request):

        """
        returns a list of all products
        """
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

    def post(self, request):
        
        """
        creates a new product
        """
        serializer = ProductSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else: 
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProductDetailAV(APIView):

    """
    place all the relevant methods here

    """

    def get(self, request, pk):
        
        """
        returns a single product object
        """
        
        try:
            product = Product.objects.get(pk=pk)

        except Product.DoesNotExist:
            return Response({"message": "product does not exist"}, status=status.HTTP_404_NOT_FOUND)

        serializer = ProductSerializer(product)
        return Response(serializer.data)


    def put(Self, request, pk):
        
        """
        returns data after an update
        """
        product = Product.objects.get(pk=pk)

        serializer = ProductSerializer(product, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        
        """
        removes an existing product
        """
        product = Product.objects.get(pk=pk)
        product.delete()
        return Response({"message": "product deleted successfully"}, status=status.HTTP_204_NO_CONTENT)

