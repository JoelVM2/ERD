import matplotlib.pyplot as plt

labels = "WhatsApp", "Instagram", "TikTok", "Twitter", "Facebook"
sizes = [20, 29, 15, 6,30]
explode = (0, 0, 0, 0, 0)
plt.rcParams['text.color'] = '#333333'
plt.rcParams['lines.linewidth'] = 2
plt.figure(figsize=(14, 8))
plt.pie(sizes, explode=explode, labels=labels, 
autopct='%1.1f%%',shadow=True,  startangle=90,wedgeprops={ 'linewidth' : 2, 'edgecolor' : 'black' }, colors = ['#4E79A7', '#F28E2B', '#E15759', '#76B7B2', '#59A14F'])
leg = plt.legend(loc="upper right")
plt.title('Use of social networks')
plt.suptitle('2025')
plt.savefig("graf.png")
plt.show()