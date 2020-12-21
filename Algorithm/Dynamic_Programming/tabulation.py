F = [0]*50 #array to store fibonacci terms

def fibonacci_bottom_up(n):
  F[n] = 0
  F[1] = 1

  for i in range(2, n+1):
    print(F)
    F[i] = F[i-1] + F[i-2]
  return F[n]

if __name__ == '__main__':
  print(fibonacci_bottom_up(46))    
