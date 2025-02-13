from django.contrib.auth.hashers import make_password, check_password
from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import User, Patient, HeartRate
from .serializers import UserSerializer, PatientSerializer, HeartRateSerializer


# Create your views here.

class UserRegistrationView(APIView):
    def post(self, request):
        data = request.data
        data['password'] = make_password(data['password'])
        serializer = UserSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data , status= status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    

# class UserListView(generics.ListAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer

class UserLoginView(APIView):
    def post(self, request):
        email = request.data.get("email")
        password = request.data.get("password")
        try:
            user= User.objects.get(email=email)
            if check_password(password,user.password):
                 return Response({"message": "Login successful"}, status=status.HTTP_200_OK)
            return Response({"error": "Invalid credentials"}, status=status.HTTP_400_BAD_REQUEST)
        except User.DoesNotExist:
            return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)



# class PatientListCreateView(generics.ListCreateAPIView):
#     queryset = Patient.objects.all()
#     serializer_class = PatientSerializer

class PatientListCreateView(generics.ListCreateAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer

    def list(self, request, *args, **kwargs):
        if request.path == "/api/patients_list/":  
            return super().list(request, *args, **kwargs) 
        return Response({"error": "Method not allowed"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def create(self, request, *args, **kwargs):
        if request.path == "/api/patients_create/":  
            return super().create(request, *args, **kwargs)
        return Response({"error": "Method not allowed"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)



class HeartRateListCreateView(generics.ListCreateAPIView):
    queryset = HeartRate.objects.all()
    serializer_class = HeartRateSerializer

    def list(self, request, *args, **kwargs):
        if request.path == "/api/heart_rate_list/":  
            return super().list(request, *args, **kwargs)
        return Response({"error": "Method not allowed"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def create(self, request, *args, **kwargs):
        if request.path == "/api/heart_rate_create/":  
            return super().create(request, *args, **kwargs)
        return Response({"error": "Method not allowed"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
