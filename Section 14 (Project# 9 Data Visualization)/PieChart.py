import matplotlib.pyplot as plt

labels = 'Python', 'C++', 'Ruby', 'Java', 'PHP', 'Perl'
sizes = [33, 52, 12, 17, 62, 48]
separated = (1, 0, 0, 0, 0, 0)

# pie chart
plt.pie(sizes, labels=labels, autopct='%1.1f%%', explode=separated)
# showing the percentage also, showing the first argument sperately
plt.axis('equal')
plt.show()

