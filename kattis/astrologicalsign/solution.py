def convert(day, month):
    starts = [
        ('Mar', 21), # Aries
        ('Apr', 21), # Taurus
        ('May', 21),
        ('Jun', 22),
        ('Jul', 23),
        ('Aug', 23),
        ('Sep', 22),
        ('Oct', 23),
        ('Nov', 23),
        ('Dec', 22),
        ('Jan', 21),
        ('Feb', 20),
    ]
    ends = [
        ('Apr', 20),
        ('May', 20),
        ('Jun', 21),
        ('Jul', 22),
        ('Aug', 22),
        ('Sep', 21),
        ('Oct', 22),
        ('Nov', 22),
        ('Dec', 21),
        ('Jan', 20),
        ('Feb', 19),
        ('Mar', 20),
    ]
    sign = [
        'Aries',
        'Taurus',
        'Gemini',
        'Cancer',
        'Leo',
        'Virgo',
        'Libra',
        'Scorpio',
        'Sagittarius',
        'Capricorn',
        'Aquarius',
        'Pisces'
    ]
    ans = 0
    for i, start in enumerate(starts):
        end = ends[i]
        if month == start[0] and day >= start[1]:
            ans = i
            break
        if month == end[0] and day <= end[1]:
            ans = i
            break
    return sign[ans]

def main():
    n = int(input())
    for _ in range(n):
        day, month = input().split()
        print(convert(int(day), month))

main()

