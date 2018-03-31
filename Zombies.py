import matplotlib.pyplot as plt

rateFristi = 5.0/(25.0*7.0)
rate = 8.0/(pow(10, 7)*5)
rateDorst = 1/(7.0)


S = [pow(10,7)]
Z = [10]
R = [0]

timeEnd = 20
for t in range(1,timeEnd*24):
    S.append(S[t-1] + (- rate*S[t-1]*Z[t-1] - rateFristi*S[t-1] + rateDorst*R[t-1])*(1/24.0))
    Z.append(Z[t-1] + (rate*S[t-1]*Z[t-1])*(1/24.0))
    R.append(R[t-1] + (rateFristi*S[t-1]-rateDorst*R[t-1])*(1/24.0))

plt.plot(range(timeEnd*24), S, label="Normaal")
plt.plot(range(timeEnd*24), Z, label="Zombie")
plt.plot(range(timeEnd*24), R, label="Fristidrinker")

plt.xlabel('time (h)')
plt.ylabel('Number of people')

plt.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc=3,
           ncol=2, mode="expand", borderaxespad=0.)



plt.show()
