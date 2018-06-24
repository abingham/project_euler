ones = ['',
        'one',
        'two',
        'three',
        'four',
        'five',
        'six',
        'seven',
        'eight',
        'nine']

teens = ['ten',
         'eleven',
         'twelve',
         'thirteen',
         'fourteen',
         'fifteen',
         'sixteen',
         'seventeen',
         'eighteen',
         'nineteen']

tens = ['',
        '',
        'twenty',
        'thirty',
        'forty',
        'fifty',
        'sixty',
        'seventy',
        'eighty',
        'ninety']

def to_text(val):
    if val == 0:
        return 'zero'
    elif val == 1000:
        return 'one thousand'

    (val,o) = divmod(val,10)
    (val,t) = divmod(val, 10)
    (val,h) = divmod(val, 10)

    print (h,t,o)

    rval = ''

    if h > 0:
        rval += '%s %s ' % (ones[h],'hundred')
        if o > 0 or t > 0:
            rval += 'and '

    if t == 1:
        # teens
        rval += '%s ' % teens[o]
    else:
        if t != 0:
            rval += '%s ' % tens[t]
        if o != 0:
            rval += '%s' % ones[o]


    return rval

sum = 0
f = open('numbers.txt', 'w')
for i in range(1, 1001):
    sz = to_text(i)
    f.write('%s\n' % sz)
    sum += len(filter(lambda x: not str.isspace(x), sz))

f.close()
print (sum)
