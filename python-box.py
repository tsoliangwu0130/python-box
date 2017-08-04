from boxsdk import Client, OAuth2

oauth = OAuth2(
    client_id='',
    client_secret='',
    access_token=''
)

client = Client(oauth)
me = client.user(user_id='me').get()
print('user_login: ' + me['login'])
