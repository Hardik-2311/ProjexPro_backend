from django.shortcuts import redirect
from rest_framework.permissions import AllowAny, IsAuthenticated
import requests
from rest_framework.decorators import (
    api_view,
    permission_classes,
    authentication_classes,
)
from django.http import JsonResponse
from django.contrib.auth import login, logout
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
    SITE = f'https://channeli.in/oauth/authorise/?client_id={CLIENT_ID}&redirect_uri={REDIRECT_URI}&state="Success/'
    return redirect(SITE)


@api_view(["GET"])
@permission_classes([])
def check_login(request):
    # print(request.COOKIES)
    if "sessionid" in request.COOKIES:
        username = request.session.get("username")
        # print(username)
        user_info = User.objects.get(username=username)
        serializer = UserSerializer(user_info)
        data = serializer.data
        # print("logged in")
        return Response({"login": "true", "data": data})
    else:
        # print("yuuuuuu")
        return Response({"login": "false"})


def Authentication(
    username, enrolment_number, name, year, email, is_Member, profile_pic, is_superuser
):
    # print("here")
    try:
        user = User.objects.get(username=username)
        return user

    except User.DoesNotExist:
        # print("Not Exists")
        User.objects.create(
            username=username,
            name=name,
            email=email,
            year=year,
            enrolment_no=enrolment_number,
            is_Member=is_Member,
            profile_pic=profile_pic,
            is_superuser=is_superuser,
        )
        user = User.objects.get(username=username)
        return user


@api_view(["GET"])
@permission_classes([AllowAny])
def Oauth2_Login(request):
    try:
        auth_code = request.GET.get("code")
        params_post = {
            "client_id": CLIENT_ID,
            "client_secret": CLIENT_SECRET_ID,
            "grant_type": "authorization_code",
            "redirect_uri": REDIRECT_URI,
            "code": auth_code,
        }
        response = requests.post("https://channeli.in/open_auth/token/", params_post)
        access_token = response.json().get("access_token")
        token_type = response.json().get("token_type")
        params_get = {"Authorization": f"{token_type} {access_token}"}
        response = requests.get(
            "https://channeli.in/open_auth/get_user_data/", headers=params_get
        )
        user_info = response.json()
        username = user_info["username"]
        name = user_info["person"]["fullName"]
        year = user_info["student"]["currentYear"]
        email = user_info["contactInformation"]["emailAddress"]
        enrolment_no = user_info["student"]["enrolmentNumber"]
        profile_pic = (
            "https://channeli.in/" + str(user_info["person"]["displayPicture"] or ""),
        )
        is_superuser = False

        is_Member = False
        for i in user_info["person"]["roles"]:
            if i["role"] == "Maintainer":
                is_Member = True
                break
        if is_Member == True:
            try:
                user = Authentication(
                    username,
                    enrolment_no,
                    name,
                    year,
                    email,
                    is_Member,
                    profile_pic,
                    is_superuser=is_superuser,
                )
                print(user)
            except:
                return Response("user cant be created")
            try:
                login(request, user)
                request.session["username"] = username
                request.session["name"] = name
                request.session["year"] = year
                request.session["email"] = email
                request.session["enrolment_no"] = enrolment_no
                request.session["is_Member"] = is_Member
                request.session["profile_pic="] = profile_pic
                request.session["is_admin"] = user.is_superuser
                return redirect("http://127.0.0.1:3000/projects/")
            except:
                return Response("login nhi hua brother")
        else:
            return Response("who are you boyyyyy??")

    except:
        SITE = f'https://channeli.in/oauth/authorise/?client_id={CLIENT_ID}&redirect_uri={REDIRECT_URI}&state="Success/'
        return redirect(SITE)


@api_view(["GET"])
@authentication_classes([])  # Exclude authentication
@permission_classes([AllowAny])  # Exclude permission checks
def logout_direct(request):
    logout(request)
    return Response({"message": "LOGGED OUT SUCCESSFULLY"}, status=status.HTTP_200_OK)
