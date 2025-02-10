from rest_framework import generics, status
from .serializers import *



class UserProfileViewC(generics.RetrieveUpdateAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer

    def get_queryset(self):
        return UserProfile.ojects.filter(user__id=self.request.user.id)


class UserProfileListViewC(generics.ListAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer


class CartDetailView(generics.UpdateAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer

    def get_queryset(self):
        return Cart.ojects.filter(user__id=self.request.user.id)

class CartListView(generics.ListAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer

    def get_queryset(self):
        return Cart.ojects.filter(user__id=self.request.user.id)
