import datetime
import os
import shutil
import subprocess
import sys
from collections import defaultdict

EXT_TO_LANG = defaultdict(lambda: 'Unknown')
EXT_TO_LANG['py'] = 'Python'
EXT_TO_LANG['c'] = 'C'

'''Download the repo at the given URL and return the dir it is saved in.'''
def download_git_repo(url):
    path = '/tmp/iandioch_kattis'
    result = subprocess.run(args=['git', 'clone', url, path])
    print(result)
    return path

def get_data_iandioch():
    url = 'https://github.com/iandioch/solutions.git'
    orig_path = download_git_repo(url)
    kattis_path = os.path.join(orig_path, 'kattis')
    dirs = os.listdir(kattis_path)
    problems = {f:{} for f in dirs if f[0] != '_' and os.path.isdir(os.path.join(kattis_path, f))}
    for prob in problems:
        date_result = subprocess.run(args=['git', 'log', '--pretty=format:%ad', '--date=short', prob], stdout=subprocess.PIPE, cwd=kattis_path)
        date = date_result.stdout.decode('utf-8').split('\n')[0]
        date_obj = datetime.datetime.strptime(date, '%Y-%m-%d')
        problems[prob]['date'] = date_obj
        problems[prob]['lang'] = []
        files = os.listdir(os.path.join(kattis_path, prob))
        for f in files:
            ext = f.split('.')[-1]
            problems[prob]['lang'].append(EXT_TO_LANG[ext])
    shutil.rmtree(orig_path)
    return problems

def main(user):
    data = supported_users[user]()
    print(data)

# dict of <username>:<func to load user data>
# This func should return a dict like: {
#   'problem_id': {
#       'date': datetime.datetime(year, month, day) # completion date
#       'lang': ['python'] # completion language (if more than one, list all)
#   }
# }
supported_users = {
    'iandioch': get_data_iandioch,
}

if __name__ == '__main__':
    if len(sys.argv) == 2 and sys.argv[1] in supported_users:
        main(sys.argv[1])
    else:
        print('Must give one of the following usernames:\n{}'.format('\n'.join(supported_users)))
