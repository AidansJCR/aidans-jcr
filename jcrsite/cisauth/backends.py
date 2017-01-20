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
        college_info = requests.get('https://community.dur.ac.uk/grey.jcr/itsuserdetailsjson.php', data={'username': username})
        college = "";
        # now determine whether the user is at Aidan's
        if(college_info.status_code != 400):
            college = college_info.json()['college']

        if(validator_resp.status_code != 401):
            # THE USER IS SUCCESS
            try:
                return User.objects.get(username=username)
            except User.DoesNotExist:
                user = User(username=username)
                user.is_staff = False
                user.is_superuser = False
                user.save()
                return user
        return None

    def get_user(self,user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
