import pandas as pd
import matplotlib.pyplot as plt


dingosplit = pd.read_csv('/content/gdrive/My Drive/Rue Cafe Data Analytics/Transactions/Payments_2022v02.csv')


dingosplit['payment_date'] = pd.to_datetime(dingosplit['payment_date'])


start_date = '2022-03-01'
filtered_data = dingosplit[dingosplit['payment_date'] >= start_date]


weekly_avg = filtered_data.resample('W', on='payment_date')['amount'].mean()


plt.figure(figsize=(10, 6))


plt.plot(weekly_avg, marker='o', linestyle='-', color='blue', linewidth=2)

plt.title('Average Transaction Amount per Week', fontsize=16, fontweight='bold')
plt.xlabel('Week', fontsize=12)
plt.ylabel('Average Transaction Amount', fontsize=12)

plt.xticks(rotation=45, fontsize=10)
plt.yticks(fontsize=10)

plt.grid(True, linestyle='--', linewidth=0.5, alpha=0.7)

plt.tight_layout()

plt.show()
