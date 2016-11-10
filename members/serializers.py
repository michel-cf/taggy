from rest_framework import serializers

from members.models import Member


class MemberSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Member
        fields = ('private_key',)
