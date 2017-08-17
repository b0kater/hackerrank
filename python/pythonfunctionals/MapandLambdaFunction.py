# author: Boris Harmeyer
# https://www.hackerrank.com/b0kater

cube = lambda x: x**3 # complete the lambda function 

def fibonacci(n):
    # return a list of fibonacci numbers
    init = [0,1]
    for i in range(2,n):
        init.append(init[i-1]+init[i-2])
    
    return init[0:n] # in case n is less than 2

if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))
