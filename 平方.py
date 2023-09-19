def get_y(n):
    for x in range(1,n+1):
        y=(n+x**2)**0.5
        if isinstance(y,int):
            return x
    return -1
print(get_y(3))