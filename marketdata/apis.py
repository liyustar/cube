from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action, api_view

class TuShareViewSet(viewsets.ViewSet):
    """
    TuShare API set
    """

    @action(detail=False)
    def get_h_data(self, request, *args, **kwargs):
        return Response({"symbol": "symbol"})



@api_view(['GET'])
def get_h_data(request, symbol:str, *args, **kwargs):
    return Response({"symbol": symbol})