import random, sys, math
import numpy as np


def Set_Population(X, count, a , b):
    for _ in range(count):
        X.append((round(random.uniform(a,b),2), round(random.uniform(a,b),2)))


def Set_Velocity(V, count):
    for _ in range(count):
        V.append((round(random.uniform(1,3),2), round(random.uniform(1,3),2)))


def StopCondition(last_min):
    if last_min[-1] == 0:
        return False
    for i in range(len(last_min)-1):
        if last_min[i] != last_min[i+1]:
            return False
    
    return True


def Append_Min(last_min, new_min):
    prev = new_min
    for i in range(len(last_min)):
        new = last_min[i]
        last_min[i] = prev
        prev = new 


def new_X(X, V, a , b):
    for i in range(len(X)):
        X[i] = (round(X[i][0] + V[i][0],2), round(X[i][1] + V[i][1],2))

        if(X[i][0] < a):
            X[i] = (a, X[i][1])
        if(X[i][0] > b):
            X[i] = (b, X[i][1])
        
        if(X[i][1] < a):
            X[i] = (X[i][0], a)
        if(X[i][1] > b):
            X[i] = (X[i][0], b)


def Update_V(X, V, Pbest, Gbest, w, c1, c2):
    for i in range(len(V)):
        v1 = round(w*V[i][0] + c1 * random.uniform(-1,1) * (Pbest[i][0] - X[i][0]) + c2 * random.uniform(-1,1) * (Gbest[1][0] - X[i][0]),2)
        v2 = round(w*V[i][1] + c1 * random.uniform(-1,1) * (Pbest[i][1] - X[i][1]) + c2 * random.uniform(-1,1) * (Gbest[1][1] - X[i][1]),2)
        V[i] = (v1, v2)


def Update_Pbest(X, Pbest, function):
    for i in range(len(X)):
        if function(X[i]) < function(Pbest[i]):
            Pbest[i] = X[i]


def FindMin(count, function, a, b, w, c1, c2, end_point):
    X = []
    V = []
    Gbest = (sys.maxsize, [])
    Pbest = []
    Set_Population(X, count, a, b)
    for i in range(count):
        Pbest.append(X[i])
    Set_Velocity(V, count)
    for i in range(len(X)):
        if function(X[i]) < Gbest[0]:
            Gbest = (function(X[i]), X[i][:])
    
    last_min = []
    for _ in range(end_point):
        last_min.append(0)
    last_min[0] = Gbest[0]
    j = 1
    while(not StopCondition(last_min)):
        new_X(X, V, a, b)
        Update_V(X, V, Pbest, Gbest, w, c1, c2)
        Update_Pbest(X, Pbest, function)
        for i in range(len(X)):
            if function(X[i]) < Gbest[0]:
                Gbest = (function(X[i]), X[i])
        Append_Min(last_min, Gbest[0])
        print(j)
        print(Gbest)
        j += 1

count = 1000
w = 0.5
c1 = 3
c2 = 2
end_point = 100

def function1(x):
    f = (-1)*abs(math.sin(x[0]) * math.cos(x[1]) * np.exp(abs(1-(((x[0]**2+x[1]**2)**(1/2))/math.pi))))
    return round(f,2)


def function2(x):
    a = math.sin(abs(x[0]**2-x[1]**2))
    b = math.cos(a)
    f = 0.5 + (((b**2) - 0.5) / (1+(x[0]**2+x[1]**2)/1000)**2)
    return round(f,2)

FindMin(count, function1, -10, 10, w, c1, c2, end_point)