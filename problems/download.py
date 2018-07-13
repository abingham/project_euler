from urllib.request import urlopen


for i in range(25, 621):
    with urlopen('http://projecteuler.net/problem={}'.format(i)) as resource:
        with open('problem{}.txt'.format(i), mode='wb') as handle:
            print(i)
            handle.write(resource.read())
