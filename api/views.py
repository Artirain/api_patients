from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Patient
from .serializers import PatientSerializer

class PatientListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        # Проверяем роль пользователя
        if request.user.role != 'doctor':
            return Response({"detail": "Access denied. Only doctors are allowed."}, status=403)

        # Получаем список пациентов
        patients = Patient.objects.all()
        serializer = PatientSerializer(patients, many=True)
        return Response(serializer.data)

