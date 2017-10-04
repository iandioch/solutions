import csv
import os

def main():
    files = [f for f in os.listdir() if f[0] != '_' and f.split('.')[1] == 'csv']
    problems = {}
    for f in files:
        with open(f) as csvfile:
            reader = csv.reader(csvfile, delimiter=',', quotechar='`')
            for row in reader:
                print(row)
                prob_id, date_str, difficulty, *langs = row
                if prob_id in problems:
                    problems[prob_id]['solvers'][f] = (date_str, langs)
                else:
                    problems[prob_id] = {
                        'solvers': {
                            f: (date_str, langs),
                        },
                        'difficulty': difficulty,
                    }
    with open('_collation.csv', 'w') as csvfile:
        writer = csv.writer(csvfile, delimiter=',', quotechar='`', quoting=csv.QUOTE_MINIMAL)
        title_users = []
        for f in files:
            title_users.append(f)
            title_users.append(None)
        title = ['Problem', 'Difficulty'] + title_users
        writer.writerow(title)
        for prob in sorted(problems, key=lambda x:problems[x]['difficulty']):
            data = problems[prob]
            row = [prob, data['difficulty']]
            for f in files:
                if f in data['solvers']:
                    row += [data['solvers'][f][1][0], data['solvers'][f][0]]
                else:
                    row += [None, None]
            writer.writerow(row)

if __name__ == '__main__':
    main()
