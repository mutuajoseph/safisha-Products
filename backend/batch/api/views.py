from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from batch.models import Batch
from .serializer import BatchSerializer

class BatchAV(APIView):

    """
    place all the relevant methods here
    """
    def get(self, request):

        """
        returns a list of all batches
        """
        batches = Batch.objects.all()
        serializer = BatchSerializer(batches, many=True)
        return Response(serializer.data)


    def post(self, request):
        
        """
        creates a new batch
        """

        serializer = BatchSerializer(data=request.data)

        # check if the data is valid
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else: 
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class BatchDetailAV(APIView):


    """
    place all relevant fields here
    """
    def get(self, request, pk):
        try:
            movie = Batch.objects.get(pk=pk)

        except Batch.DoesNotExist:
            return Response({"message": "Batch does not exist"}, status=status.HTTP_404_NOT_FOUND)

        serializer = BatchSerializer(movie)
        return Response(serializer.data)


    def put(self, request, pk):
        movie = Batch.objects.get(pk=pk)

        serializer = BatchSerializer(movie, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        batch = Batch.objects.get(pk=pk)
        batch.delete()
        return Response({"message": "Batch deleted successfully"}, status=status.HTTP_204_NO_CONTENT)