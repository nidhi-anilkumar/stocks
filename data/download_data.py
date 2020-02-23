import subprocess

pot_stock_list = ['CGC', 'CARA']

for ticker in pot_stock_list:
    date = '20190221'
    process = subprocess.Popen(['./stockdownload_yahoo.sh', ticker, date],
                             stdout=subprocess.PIPE,
                             stderr=subprocess.PIPE)
    print(process.communicate())
