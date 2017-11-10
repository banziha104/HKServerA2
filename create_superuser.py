import django
django.setup()

from django.contrib.auth import get_user_model

def main():
    username = "iyengjoon"
    email = 'banziha104@gmail.com'
    password = '!dl38349687'
    User = get_user_model()
    if not User.objects.filter(username=username).exists():
        User.objects.create_superuser(username,email,password)
        print('Create Iyeongjjon')

    if __name__ == '__main__':
        main()