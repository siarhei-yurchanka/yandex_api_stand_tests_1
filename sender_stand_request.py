import data
import configuration
import requests


def grep_token(user_body):
   response = requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
                     json=user_body,
                     headers=data.headers)

   token = response.json()
   value = token.get('authToken')
   return value


def post_new_client_kit(full_kit, token):
    print(full_kit, token)
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_KITS,
                         json=full_kit,
                         headers= {"Content-Type": "application/json", "Authorization": f"Bearer {token}"},
                         params=full_kit
                         )

response = post_new_client_kit(data.kit_body, grep_token(data.user_body))


def post_new_client_kit_name_0(kit_body_0, token):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_KITS,
                         json=kit_body_0,
                         headers= {"Content-Type": "application/json", "Authorization": f"Bearer {token}"})
response = post_new_client_kit(data.kit_body_0, grep_token(data.user_body))