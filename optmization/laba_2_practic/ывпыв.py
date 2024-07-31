x_lsit = [1,2,-2,8,-18]
x_0 = [2,5]
epsilon = 0.1
ct = 0
while True:
    ct +=1
    e = [0,0] #
    print(f"f(x) =  {x_lsit[0]*x_0[0]*x_0[0] + x_lsit[1]*x_0[1]*x_0[1]+x_lsit[2]*x_0[0]*x_0[1]+x_lsit[3]*x_0[0]+ x_lsit[4]*x_0[1]} ")
    print(f"Точки: {x_0[0]}, {x_0[1]}")
    # step 1
    d_x_on_d_x1 = round(x_lsit[0]*2*x_0[0] + x_lsit[2]*x_0[1] + x_lsit[3],2) # df(x)/dx1
    d_x_on_d_x2 = round(x_lsit[1]*2*x_0[1] + x_lsit[2]*x_0[0] + x_lsit[4],2) # df(x)/dx2
    print(f"Градиент: {d_x_on_d_x1}, {d_x_on_d_x2}")
    gradient = [d_x_on_d_x1,d_x_on_d_x2]
    if (abs(gradient[0]< epsilon ) and abs(gradient[1]) < epsilon):
        break
     # step 2
    index = 1 if abs(gradient[1])>abs(gradient[0]) else 0
    print(f"Индекс: {index}")
     # step 3
    e[index] = 1 * (1 if gradient[index] < 0  else -1)
    s = e
    print(f"S : {s[0]}, {s[1]}")
     # step 4
    l = 0
    if index == 1:
        l = abs((2*x_0[0]+18)/4)
    else:
        l = abs((2*x_0[1]-8)/4)
    l = round(l,2)
    print(f"Лямбда: {l}")
     # step 5
    x_0[0] = l*s[0]+x_0[0]
    x_0[1] =l*s[1]+x_0[1]
    print()
    if l < epsilon or ct ==200  :
        break
print(f"f(x) =  {x_lsit[0]*x_0[0]*x_0[0] + x_lsit[1]*x_0[1]*x_0[1]+x_lsit[2]*x_0[0]*x_0[1]+x_lsit[3]*x_0[0]+ x_lsit[4]*x_0[1]}")
print(f"Точки: {x_0[0]}, {x_0[1]}")
print("Количество итераций",ct)
