from .serializers import CustomerSerializer
from .models import Customer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAdminUser
from rest_framework import viewsets
from .permissions import IsOwnerOrReadOnly
from rest_framework.throttling import AnonRateThrottle, UserRateThrottle


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'user': reverse('UserList', request=request, format=format),
        'customerdetail': reverse('CustomerDetail', request=request, format=format),
    })


class UserList(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAdminUser]
    throttle_classes = [UserRateThrottle]


class CustomerDetail(viewsets.ReadOnlyModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsOwnerOrReadOnly]
    throttle_classes = [AnonRateThrottle, UserRateThrottle]

    def get_queryset(self):
        return self.queryset.filter(username=self.request.user)
