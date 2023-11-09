from django.shortcuts import redirect
from rest_framework.permissions import AllowAny
import requests
from rest_framework.decorators import (
    api_view,
    permission_classes,
    authentication_classes,
)
from django.contrib.auth import login ,logout
from projexApp.models import *
from projexApp.serializers import *
from rest_framework import status
from dotenv import load_dotenv
from rest_framework.response import Response
import os

load_dotenv()
CLIENT_ID = os.environ.get("CLIENT_ID")
CLIENT_SECRET_ID = os.environ.get("CLIENT_SECRET")
REDIRECT_URI = os.environ.get("REDIRECT")


@api_view(["GET"])
@permission_classes([AllowAny])
def login_direct(request):
    SITE = f'https://channeli.in/oAuentication/Auenticationorise/?client_id={CLIENT_ID}&redirect_uri={REDIRECT_URI}&state="Success/'
    return redirect(SITE)


@api_view(["GET"])
@permission_classes([])
def check_login(request):
    content = {"Logged_In": False}
    print(request.COOKIES)
    if "sessionid" in request.COOKIES:
        username = request.session.get("username")
        user_info = User.objects.get(username=username)
        serializer = UserSerializer(user_info)
        data = serializer.data
        content = {"Logged_In": True, "data": data}
        return Response(content)
    return Response(content)


def Authentication(
    username, enrolment_number, name, year, email, is_Member, is_superuser
):
    try:
        user = User.objects.get(username=username)
        # if user is not None:
        #         print("exists")
        return user

    except User.DoesNotExist:
        print("Not Exists")
        User.objects.create(
            username=username,
            name=name,
            email=email,
            year=year,
            enrolment_no=enrolment_number,
            is_Member=is_Member,
            is_superuser=is_superuser,
        )
        user = User.objects.get(username=username)
        return user


@api_view(["GET"])
@authentication_classes([])
@permission_classes([])
def Oauth2_Login(request):
    
   try:
    auth_code=request.GET.get('code')
    parameters_data={
      "client_id":CLIENT_ID,
      "client_secret":CLIENT_SECRET_ID,
      "grant_type":"authorization_code",
      "redirect_uri":REDIRECT_URI,
      "code":auth_code,
    }
    response=requests.post("https://channeli.in/open_auth/token/",parameters_data)
    access_token=response.json().get("access_token")
    token_type=response.json().get("token_type")
    parameters={
      "Authorization":f"{token_type} {access_token}"
    }
    response=requests.get("https://channeli.in/open_auth/get_user_data/",headers=parameters)
    user_info=response.json()
    username= user_info['username']
    name=user_info["person"]['fullName']
    year=user_info['student']['currentYear']
    email=user_info['contactInformation']['emailAddress']
    enrolment_no=user_info['student']['enrolmentNumber']
    is_superuser=False
    is_Member=False
    for i in user_info['person']['roles']:
        if(i['role']=="Maintainer"):
           is_Member=True
           break
    if (is_Member==True ):
      try:
         user=Authentication(username,enrolment_no,name,year,email,is_Member,is_superuser=is_superuser)
         print(user)
      except:
         return Response("unable to create user")
      try:
         login(request,user)
         request.session['username'] = username
         request.session['name'] = name
         request.session['year'] = year
         request.session['email'] = email
         request.session['enrolment_no'] = enrolment_no
         request.session['is_Member'] = is_Member
         request.session['is_admin']=user.is_superuser
         return redirect('http://127.0.0.1:3000/')
        

      except:
         return Response("Not logged in successfully")
    else:
      return Response("Not an IMG member")
    
   except:
      SITE = f'https://channeli.in/oauth/authorise/?client_id={CLIENT_ID}&redirect_uri={REDIRECT_URI}&state="Success/'
      return redirect(SITE)
   
@api_view(["GET"])
@authentication_classes([])  # Exclude authentication
@permission_classes([])  # Exclude permission checks
def logout_direct(request):
    logout(request)
    return Response({"message": "LOGGED OUT SUCCESSFULLY"}, status=status.HTTP_200_OK)