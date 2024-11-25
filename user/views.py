import random
from django.core.mail import send_mail
from rest_framework.response import Response
from rest_framework import viewsets, status
from django.contrib.auth import get_user_model
from rest_framework.exceptions import ValidationError
from django.contrib.auth import login as auth_login
from .serializers import RegisterSerializer, VerifyEmailSerializer, LoginSerializer, VerifyLoginSerializer

User = get_user_model()


class AuthViewSet(viewsets.ViewSet):
    def register(self, request):
        serializer = RegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        email = serializer.validated_data['email']
        verification_code = random.randint(100000, 999999)

        # Save verification code in the session or cache
        request.session['verification_code'] = str(verification_code)
        request.session['email'] = email

        # Send verification email
        send_mail(
            'Your Verification Code',
            f'Your code is {verification_code}',
            'your-email@gmail.com',
            [email],
            fail_silently=False,
        )
        return Response({'message': 'Verification code sent to email'}, status=status.HTTP_200_OK)

    def verify_email(self, request):
        serializer = VerifyEmailSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        email = serializer.validated_data['email']
        code = serializer.validated_data['code']

        saved_code = request.session.get('verification_code')
        saved_email = request.session.get('email')

        if not (saved_code and saved_email):
            raise ValidationError('No verification process found.')

        if saved_email != email or saved_code != code:
            raise ValidationError('Invalid verification code.')

        # Create the user
        User.objects.create_user(email=email)
        del request.session['verification_code']
        del request.session['email']

        return Response({'message': 'Email verified and user registered successfully'}, status=status.HTTP_201_CREATED)

    def login(self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        email = serializer.validated_data['email']

        verification_code = random.randint(100000, 999999)

        # Save verification code in the session or cache
        request.session['verification_code'] = str(verification_code)
        request.session['email'] = email

        # Send login code
        send_mail(
            'Your Login Code',
            f'Your code is {verification_code}',
            'your-email@gmail.com',
            [email],
            fail_silently=False,
        )
        return Response({'message': 'Login code sent to email'}, status=status.HTTP_200_OK)

    def verify_login(self, request):
        serializer = VerifyLoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        email = serializer.validated_data['email']
        code = serializer.validated_data['code']

        saved_code = request.session.get('verification_code')
        saved_email = request.session.get('email')

        if not (saved_code and saved_email):
            raise ValidationError('No login process found.')

        if saved_email != email or saved_code != code:
            raise ValidationError('Invalid login code.')

        # Authenticate user
        user = User.objects.filter(email=email).first()
        if not user:
            raise ValidationError('User not found.')

        auth_login(request, user)
        del request.session['verification_code']
        del request.session['email']

        return Response({'message': 'User logged in successfully'}, status=status.HTTP_200_OK)
