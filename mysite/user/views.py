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
    queryset = UserProfile.objects.all()
    serializer_class = CartSerializer



class CartListView(generics.ListAPIView):
    # queryset = Cart.objects.all()
    serializer_class = CartSerializer

    def get_queryset(self):
        return Cart.objects.filter(user__id=self.request.user.id)



class CartItemCreateAPIView(generics.CreateAPIView):
    serializer_class = CartItemCreateSerializer

    def perform_create(self, serializer):
        cart, created = Cart.objects.get_or_create(user=self.request.user)
        serializer.save(cart=cart)


class CartItemUpdateDeleteAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CartItemCreateSerializer
