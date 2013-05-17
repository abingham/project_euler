import os, zipfile

def read_primes_(filenames):
    '''
    Takes a list of zip filenames, reading them each in order
    as lists of prime numbers. This is a generator where each
    yield produces the next prime read in.
    '''
    for filename in filenames:
        zfile = zipfile.ZipFile(filename, 'r')
        for name in zfile.namelist():
            file = zfile.open(name)
            for line in file:
                for prime in line.split():
                    try:
                        yield int(prime)
                    except ValueError:
                        continue
        zfile.close()

def read_primes(filenames=[]):
    '''generate a sequence of primes read from files

    :param filenames: a list of filenames to read primes from. If
                      empty, a list of all files in the prime_data
                      directory is used (in proper order)
    :return: a generator of primes                    
    '''
    if len(filenames) == 0:
        filenames = [os.path.join('prime_data', 'primes%d.zip' % i) for i in xrange(1, 51)]
    return read_primes_(filenames)
