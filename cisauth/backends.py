"""
This is the CIS Authentication.
This might need to be changed if a more secure method of auth is available
(e.g. Shibboleth).
"""
from django.contrib.auth.models import User
import requests
import time


class CISBackend(object):
    def authenticate(self,username=None,password=None):
         # see if the user is valid on the durham server
        validator_resp = requests.get('https://www.dur.ac.uk/its/password/validator', auth=(username,password)) 
        college_info = requests.get('https://community.dur.ac.uk/grey.jcr/itsuserdetailsjson.php', params={'username': str(username)})
        print(username)
        print(college_info.json())
        info = None
        # now determine whether the user is at Aidan's
        if(college_info.status_code != 400):
            info = college_info.json()

        if(validator_resp.status_code != 401 and info is not None and info['college']=="St Aidan's College"):
            # The user is authenticated, and part of Aidan's
            try:
                return User.objects.get(username=username)
            except User.DoesNotExist:
                # Create a new Django user, getting information from the info database
                user = User(username=username)
                user.is_staff = False
                user.is_superuser = False
                user.email = info['email']
                user.first_name = info['firstnames']
                user.last_name = info['surname']
                user.save()
                return user
        return None

    def get_user(self,user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
