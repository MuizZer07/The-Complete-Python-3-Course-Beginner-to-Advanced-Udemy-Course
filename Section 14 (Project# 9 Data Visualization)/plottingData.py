import matplotlib.pyplot as plt

years = [1950, 1955, 1960, 1965, 1970, 1975, 1980, 1985, 1990, 1995, 2000,
         2005, 2010, 2015]

pops = [2.5, 2.7, 3.0, 3.3, 3.6, 4.0, 4.4, 4.8, 5.3, 5.7, 6.1,
        6.5, 6.9, 7.3]

deaths = [1.2, 1.7, 1.8, 2.2, 2.5, 2.7, 2.9, 3.0, 3.1, 3.3, 3.5, 3.8, 4.0, 4.3]

# plotting data, Figure 1
plt.plot(years, pops, '--', color=(255/255, 100/255, 100/255))  # rgb coloring, dashed line
plt.plot(years, deaths, color=(.6, .6, 1))  # plotting two different lines in a same graph

plt.title("Figure 1: Population growth")  # adding a title to the graph

plt.ylabel("Population in Billions")  # labeling Y axis
plt.xlabel("Population growth by year")  # labeling X axis

plt.show()  # displaying the graph using show() method

# Figure 2
lines = plt.plot(years, pops, years, deaths)
plt.grid(True)  # grid background

plt.title("Figure 2: Population growth")  # adding a title to the graph

plt.ylabel("Population in Billions")  # labeling Y axis

plt.setp(lines, color=(1, .4, .4), marker=".")  # different markers + . o ..see documentation
plt.show()