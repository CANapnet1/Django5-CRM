from django.shortcuts import render
# Create your views here.
from rest_framework import viewsets
from .models import Client, ClientDetails
from .serializers import ClientSerializer, ClientDetailsSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from django.db import connection
from psycopg import OperationalError


class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer


class AnimeDetailsViewSet(viewsets.ModelViewSet):
    queryset = ClientDetails.objects.all()
    serializer_class = ClientDetailsSerializer


class JoinedTablesView(APIView):
    def get(self, request):
        try:
            with connection.cursor() as cursor:
                cursor.execute("""
                SELECT * FROM api_client
                INNER JOIN api_clientdetails ON api_client.client_id = api_clientdetails.client_id;
                """)
                columns = [col[0] for col in cursor.description]
                data = [dict(zip(columns, row)) for row in cursor.fetchall()]
                return Response(data)

        except OperationalError as e:
            # Log the exception or handle it appropriately
            return Response({"error": f"Database error: {e}"}, status=500)