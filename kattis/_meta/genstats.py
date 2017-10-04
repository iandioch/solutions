import csv
import datetime
import os
import requests
import shutil
import subprocess
import sys
from bs4 import BeautifulSoup
from collections import defaultdict


# Add more entries if you get lots of Unknown solutions.
EXT_TO_LANG = defaultdict(lambda: 'Unknown')
EXT_TO_LANG['py'] = 'Python'
EXT_TO_LANG['c'] = 'C'
EXT_TO_LANG['java'] = 'Java'


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


def get_data_flat(repo_url):
    orig_path = download_git_repo(repo_url)
    files = os.listdir(orig_path)
    problems = {}
    for f in files :
        parts = f.split('.')
        prob = parts[0]
        if prob == 'README':
            continue
        if len(prob) == 0:
            continue
        if prob in problems:
            problems[prob]['lang'].append(EXT_TO_LANG[parts[-1]])
            continue
        problems[prob] = {}
        date_result = subprocess.run(args=['git', 'log', '--pretty=format:%ad', '--date=short', f], stdout=subprocess.PIPE, cwd=orig_path)
        date_obj = datetime.datetime.today()
        try:
            date = date_result.stdout.decode('utf-8').split('\n')[0]
            date_obj = datetime.datetime.strptime(date, '%Y-%m-%d')
        except Exception as e:
            print(e)
        problems[prob]['date'] = date_obj
        problems[prob]['lang'] = []
        problems[prob]['lang'].append(EXT_TO_LANG[parts[-1]])
    shutil.rmtree(orig_path)
    return problems


def get_problem_difficulty(problem):
    try:
        url = 'https://open.kattis.com/problems/{}'.format(problem)
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        raw_difficulty = soup.find('div', 'problem-sidebar').find_all('div', 'sidebar-info')[1].find_all('p')[3].text
        score = float(raw_difficulty.split(':')[1].strip())
        return score
    except Exception as e:
        print(e)
        return 0.0


def main(user):
    data = supported_users[user]()
    for prob in data:
        score = get_problem_difficulty(prob)
        data[prob]['difficulty'] = score
        print('Problem {} difficulty: {}'.format(prob, score))
    sorted_probs = sorted(data, key=lambda x:data[x]['date'])
    with open(user + '.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=',', quotechar='`', quoting=csv.QUOTE_MINIMAL)
        for prob_id in sorted_probs:
            problem = data[prob_id]
            row = [prob_id, problem['date'].strftime('%Y-%m-%d'), problem['difficulty']] + problem['lang']
            print(row)
            writer.writerow(row)


# dict of <username>:<func to load user data>
# This func should return a dict like: {
#   'problem_id': {
#       'date': datetime.datetime(year, month, day) # completion date
#       'lang': ['python'] # completion language (if more than one, list all)
#   }
# }
supported_users = {
    'iandioch': get_data_iandioch,
    'cianlr': lambda: get_data_flat('https://github.com/cianlr/kattis-solutions.git'),
}


if __name__ == '__main__':
    if len(sys.argv) == 2 and sys.argv[1] in supported_users:
        main(sys.argv[1])
    else:
        print('Must give one of the following usernames:\n{}'.format('\n'.join(supported_users)))
