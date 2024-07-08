import matplotlib.pyplot as plt

languages = ['Hindi', 'English', 'Tamil', 'Bengali', 'Marathi']
students = [40, 12, 7, 4, 9]

plt.figure(figsize=(6, 6)) # width:6, height:6
plt.pie(students, labels=languages, autopct='%1.1f%%', startangle=140)
plt.title('Number of Students Speaking Different Languages')


plt.axis('equal') # Equal aspect ratio ensures that pie is drawn as a circle.
plt.show()