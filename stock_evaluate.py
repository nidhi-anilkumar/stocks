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
fig2 = plt.figure(2)#, figsize=[200, 200], dpi=400)
for file in os.listdir('data'):
    if '.csv' in file:
        data = pd.read_csv(os.path.join('data', file))
        plt.figure(1)
        plt.plot(data['Date'], data['High'], label=file[:-4])
        plt.figure(2)
        plt.plot(data['Date'], data['Low'], label=file[:-4])

plt.figure(1)
fig1.legend()
plt.xlabel('Date')
plt.ylabel('High [$]')
plt.title('Date vs High value')
fig1.savefig('high_plot.png')

plt.figure(2)
fig2.legend()
plt.xlabel('Date')
plt.ylabel('Low [$]')
plt.title('Date vs Low value')
fig2.savefig('low_plot.png')
