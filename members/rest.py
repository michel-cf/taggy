from rest_framework import viewsets

from rest_framework.response import Response

from members.models import Member
from members.serializers import MemberSerializer


class MemberViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint to get the member information
    """
    queryset = Member.objects.all()
    serializer_class = MemberSerializer
