from counselor.models import Counselor
from rest_framework import viewsets
from .serializers import CounselorSerializer


class CounselorViewSet(viewsets.ModelViewSet):
    queryset = Counselor.objects.all()
    serializer_class = CounselorSerializer
