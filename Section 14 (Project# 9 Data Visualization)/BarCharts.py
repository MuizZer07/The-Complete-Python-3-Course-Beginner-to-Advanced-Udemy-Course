import matplotlib.pyplot as plt
import numpy as np

col_count = 3
bar_width = .2

korea_scores = (554, 536, 538)
canada_scores = (518, 523, 525)
china_scores = (613, 570, 580)
france_scores = (495, 505, 499)

index = np.arange(col_count)

k1 = plt.bar(index, korea_scores, bar_width, alpha=0.4, label="Korea")
c1 = plt.bar(index + 0.2, canada_scores, bar_width, alpha=0.4, label="Canada")
ch1 = plt.bar(index + 0.4, china_scores, bar_width, alpha=0.4, label="China")
f1 = plt.bar(index + 0.6, france_scores, bar_width, alpha=0.4, label="France")


def CreateLabel(data):
    for item in data:
        height = item.get_height()
        plt.text(item.get_x() + item.get_width()/2., height*1.05, '%d' % int(height),ha='center', va='bottom')

CreateLabel(k1)
CreateLabel(c1)
CreateLabel(ch1)
CreateLabel(f1)

plt.ylabel("Mean score in PISA 2012")
plt.xlabel("Subjects")
plt.title("Test scores by country")

plt.xticks(index + .3 /2, ("Mathematics", "Reading", "Science"))
plt.legend(frameon=False, bbox_to_anchor=(1,1), loc=2)
plt.grid(True)

plt.show()

