def print_num(n):
    if n==0:
        return 

    print_num(n-1)
    print(n)

print_num(5)


def fact(n):
  if n==2:
    return 2 

  return n*fact(n-1)

print(fact(5))