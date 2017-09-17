# Local Django.
from counselor.models import Counselor
from rest_framework import serializers


class CounselorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Counselor
        fields = ('id', 'url', 'cpf', 'email', 'phone', 'first_name')
