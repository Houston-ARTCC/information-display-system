import os
import requests

from ..users.models import User


def process_oauth(code):
    resp = requests.post('https://auth.vatsim.net/oauth/token/', data={
        'grant_type': 'authorization_code',
        'client_id': os.getenv('VATSIM_CONNECT_CLIENT_ID'),
        'client_secret': os.getenv('VATSIM_CONNECT_CLIENT_SECRET'),
        'redirect_uri': os.getenv('VATSIM_CONNECT_REDIRECT_URI'),
        'code': code,
    })

    if resp.status_code != 200:
        return

    auth = resp.json()

    data = requests.get('https://auth.vatsim.net/api/user/', headers={
        'Authorization': 'Bearer ' + auth.get('access_token'),
        'Accept': 'application/json',
    }).json().get('data')

    user_query = User.objects.filter(cid=data.get('cid'))
    if not user_query.exists():
        user = User.objects.create_user(
            cid=data.get('cid'),
            email=data.get('personal').get('email'),
            first_name=data.get('personal').get('name_first'),
            last_name=data.get('personal').get('name_last'),
        )
    else:
        user = user_query.first()

    return user
