from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import generics
from .serializers import UserSerializer, NoteSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import Note

# Create your views here.
class NoteListCreate(generics.ListCreateAPIView):
    serializer_class = NoteSerializer
    # only allow authenticated users access
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # get the authenticated user
        user = self.request.user
        # get notes specific to user
        return Note.objects.filter(author=user)

    def perform_create(self, serializer):
        if serializer.is_valid():
            serializer.save(author=self.request.user)
        else:
            print(serializer.errors)


class NoteDelete(generics.DestroyAPIView):
    serializer_class = NoteSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # get the authenticated user
        user = self.request.user
        # get notes specific to user
        return Note.objects.filter(author=user)


class CreateUserView(generics.CreateAPIView):
    # list all objs to make sure no duplicate users
    queryset = User.objects.all()
    # tell view what data to accept to make a new user
    serializer_class = UserSerializer
    # allows anyone (even unauthenticated) to create a user
    permission_classes = [AllowAny]
