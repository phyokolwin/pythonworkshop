
grades = ['A', 'B', 'C', 'D', 'E', 'F']
students_count = [20, 30, 10, 5, 8, 2]

import matplotlib.pyplot as plt
plt.bar(grades, students_count, color=['green', 'gray', 'gray', 'gray', 'gray', 'red'])

plt.title('Grades Bar Plot for Biology Class')
plt.xlabel('Grade')
plt.ylabel('Num Students')
plt.bar(grades, students_count, color=['green', 'gray', 'gray', 'gray', 'gray', 'red'])
plt.show()

plt.barh(grades, students_count, color=['green', 'gray', 'gray', 'gray', 'gray', 'red'])

