
_username = "jun"

_password = "abc123"



username  = input('username:')

pasword =  input('password:')

if _username == username and _password == pasword:
    print('Welcome user {name} login...'.format (name=username))
else:
    print('Invalid username or password!')