from numpy import mean, absolute 

data = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140]

A = 70 

sum = 0 # initialize sum to 0 

for i in range(len(data)):
    av = absolute(data[i] - A)

    sum = sum + av 

print(sum / len(data))
