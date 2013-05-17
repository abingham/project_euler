def solve(target, so_far = 0, max = None):
    if max is None:
        max = target - 1
        
    count = 0

    for i in xrange(1, max + 1):
        sum = so_far + i
        if sum == target:
            count += 1
            break
        elif sum > target:
            break
        else:
            count += solve(target, sum, i)
            
    return count
        
if __name__ == '__main__':
    last = 1
    for i in range(2, 20):
        new = solve(i)
        print new / 2, new
        last = new
