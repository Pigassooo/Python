import pandas as pd
from datetime import datetime, timedelta
from matplotlib import pyplot as plt
from matplotlib import dates as mpl_dates

data = pd.read_csv('data\data4.csv')

data['Date'] = pd.to_datetime(data['Date'])
data.sort_values('Date', inplace=True)

price_date = data['Date']
price_close = data['Close']

plt.title('Bitcoin Prices')
plt.xlabel('Date')
plt.ylabel('Closing Price')

y = [0, 1, 3, 4, 6, 5, 7]

date_format = mpl_dates.DateFormatter('%b%d %Y')

plt.gca().xaxis.set_major_formatter(date_format)

plt.plot_date(price_date, price_close, linestyle='solid', marker='o')

plt.gcf().autofmt_xdate()

plt.tight_layout()

plt.show()