# import os
# import sys
# sys.path.append(os.path.join(os.getcwd(), 'data'))
# from data.download_data import download_data
# download_data()

import numpy as np
import pandas as pd
import os
import matplotlib.pyplot as plt

fig1 = plt.figure(1)#, figsize=[200, 200], dpi=400)
for file in os.listdir('data'):
    if '.csv' in file:
        data = pd.read_csv(os.path.join('data', file))
        plt.plot(data['Date'], data['High'], label=file[:-4])

plt.legend()
plt.xlabel('Date')
plt.ylabel('High [$]')
plt.grid()
plt.savefig('stocks_plot.png')
