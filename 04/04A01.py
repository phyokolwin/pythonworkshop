
import csv

lines = []

with open('titanic_train.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for line in csv_reader:
        lines.append(line)

data = lines[1:]
passengers = []
headers = lines[0]

for d in data:
    p = {}
    for i in range(0,len(headers)):
        key = headers[i]
        value = d[i]
        p[key] = value
    passengers.append(p)

survived = [p['Survived'] for p in passengers]
pclass = [p['Pclass'] for p in passengers]
age = [float(p['Age']) for p in passengers if p['Age'] != '']
gender_survived = [p['Sex'] for p in passengers if int(p['Survived']) == 1]

import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from collections import Counter

plt.title("Survived")
plt.pie(Counter(survived).values(), labels=Counter(survived).keys(), autopct='%1.1f%%',
        colors=['lightblue', 'lightgreen', 'yellow'])
plt.show()

import seaborn as sns
import numpy as np
from collections import Counter

plt.title("Survived")
plt.pie(Counter(survived).values(), labels=Counter(survived).keys(), autopct='%1.1f%%',
        colors=['lightblue', 'lightgreen', 'yellow'])
plt.show()

plt.title("surviving passengers count by gender")
plt.bar(Counter(gender_survived).keys(), Counter(gender_survived).values())
plt.show()

