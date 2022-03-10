import random

count = 0
spis = []
for i in range(2019):
	spis.append(random.randint(0, 15_000))
for i in spis:
	if i % 2 == 1 and i % 3 == 0:
		count += 1
for i in range(len(spis)):
	if spis[i] % 2 == 0 and spis[i] % 3 != 0:
		spis[i] = count
print(spis)

