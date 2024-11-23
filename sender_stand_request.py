import data
import configuration
import requests
#from sender_stand_request import *

def grep_token(user_body):
   response = requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
                     json=user_body,
                     headers=data.headers)

   token = response.json()
   value = token.get('authToken')
   return value

#token_x = grep_token(data.user_body)



def post_new_client_kit(full_kit, token):
    print(full_kit, token)
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_KITS,
                         json=full_kit,
                         headers= {"Content-Type": "application/json", "Authorization": f"Bearer {token}"},
                         params=full_kit
                         )

response = post_new_client_kit(data.kit_body, grep_token(data.user_body))
#print(response.status_code)
#print(response.json())

#"auth_token": token_x