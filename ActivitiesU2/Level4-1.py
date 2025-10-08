import matplotlib.pyplot as plt

labels = "WhatsApp", "Instagram", "TikTok", "Twitter", "Facebook"
sizes = [20, 29, 15, 6,30]
explode = (0, 0, 0, 0, 0)
fig, (ax) = plt.subplots()
plt.figure(figsize=(12, 6))
plt.bar(labels,sizes,color=['green','orange','black','cyan','blue'])
ax.pie(sizes, explode=explode, labels=labels, 
autopct='%1.1f%%',shadow=True, startangle=90)
plt.show()