from ast import Is
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from yaml import serialize
from api.serializers.create_and_list import UserCreateAndListSerializer
from api.serializers.show import UserShowSerializer
from api.serializers.invite import UserInviteSerializer
from models.models import User
from api.services.user import UserService
from drf_spectacular.types import OpenApiTypes
from drf_spectacular.utils import OpenApiParameter, extend_schema
from rest_framework.permissions import IsAuthenticated ,AllowAny

class UserCreateAndListView(APIView):
    permission_classes = [AllowAny]
    @extend_schema(
        tags=['User'],
        summary='Create user',
        description='Создание пользователя',
        request=UserCreateAndListSerializer,
        responses={
            201: UserShowSerializer
        }
    )
    def post(self, request):
        serializer = UserCreateAndListSerializer(data=request.data)
        if serializer.is_valid():
            refresh = UserService().create_user(serializer.validated_data['phone_number'],serializer.validated_data['password'])      
            return Response(
            {
                "refresh": refresh[0],
                "access":refresh[1],
            },
            status=status.HTTP_201_CREATED,
        )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST )

    
class UserShowView(APIView):
    permission_classes = [AllowAny]
    @extend_schema(
        tags=['User'],
        summary='Get user by id',
        description='Получение пользователя по id',
        responses={
            200: UserShowSerializer
        }
    )
    def get(self, request, pk):
        try:           
            user = User.objects.get(pk=pk)
            serializer = UserShowSerializer(user)
            return Response(serializer.data)
        except User.DoesNotExist:
            return Response({'detail': 'User not found'},status=status.HTTP_404_NOT_FOUND)
class UserInviteView(APIView):
    permission_classes = [IsAuthenticated]
    @extend_schema(
        tags=['User'],
        summary='Use invite code',
        description='Использование кода приглашения',
        request=UserInviteSerializer,
        responses={
            200: UserShowSerializer
        }
    )
    def put(self, request):

        phone_number = request.data['phone_number']
        invite_code = request.data['invite_code']
        if User.objects.filter(invite_code=invite_code).exists():
            user = User.objects.get(phone_number=phone_number)
            if user.invite_code == invite_code:
                return Response({'detail': 'Это ваш инвайт-код'}, status=status.HTTP_400_BAD_REQUEST)
            if user.used_invite_code != None:
                return Response({'detail': 'Вы уже использовали инвайт-код'}, status=status.HTTP_400_BAD_REQUEST)
            if user == None:
                return Response({'detail': 'Неверный номер'}, status=status.HTTP_400_BAD_REQUEST)
            user.used_invite_code = invite_code
            user.save()
        else:
            return Response({'detail': 'неверный инвайт-код'}, status=status.HTTP_400_BAD_REQUEST)
        serializer = UserShowSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)
        

        