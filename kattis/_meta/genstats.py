import subprocess
import sys

def get_data_iandioch():
    url = 'http://github.com/iandioch/solutions'

def main(user):
    data = supported_users[user]()
    print(data)

# dict of <username>:<func to load user data>
supported_users = {
    'iandioch': get_data_iandioch,
}

if __name__ == '__main__':
    if len(sys.argv) == 2 and sys.argv[1] in supported_users:
        main(sys.argv[1])
    else:
        print('Must give one of the following usernames:\n{}'.format('\n'.join(supported_users)))
