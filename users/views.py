from rest_framework import generics
from users.models import Users
from users.serializers import UsersSerializer


class UsersCreateListView(generics.ListCreateAPIView):
    queryset = Users.objects.all()
    serializer_class = UsersSerializer


class UsersRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Users.objects.all()
    serializer_class = UsersSerializer
