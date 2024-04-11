def fib_recursive(n, counts):
    """
    Return the nth Fibonacci number. 
    counts is a list of n+1 elements, where counts[i] is incremented
    each time fib_recursive(i, counts) is called.
    """    
    counts[n] += 1
    ###TODO
    pass
    if n == 0:
      return n
    elif n==1:
      return 1
    return fib_recursive(n-1, counts) + fib_recursive(n-2, counts)
  

    

    
def fib_top_down(n, fibs):
    ###TODO
    if fibs[n] !=  -1:
      return fibs[n]
    elif n == 0:
      return n 
    elif n == 1:
      return 1
    return fib_top_down(n-1, fibs) + fib_top_down(n-2, fibs)
  


def fib_bottom_up(n):
    ###TODO
    fibs = [0] * (n+1)
    fibs[0]=0
    fibs[1]=1
    for i in range(2, n+1):
      fibs[i] = fibs[i-1] + fibs[i-2]
    return fibs[n]
 




def fib_bottom_up_better(n):
    ###TODO
    pass
