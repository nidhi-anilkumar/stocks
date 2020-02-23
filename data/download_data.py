import subprocess
import yaml

with open("stock_list.yaml", 'r') as stream:
    try:
        data = yaml.safe_load(stream)
    except yaml.YAMLError as exc:
        print(exc)

stock_list = data['stocks']
date = data['date']


def download_data(stock_list=stock_list, date=date):

    for ticker in stock_list:
        process = subprocess.Popen(['./stockdownload_yahoo.sh', ticker, date],
                                 stdout=subprocess.PIPE,
                                 stderr=subprocess.PIPE)
        process_run = process.communicate()
        if 'saved' in process_run[-1]:
            print('downloaded : ', ticker)


if __name__ == '__main__':
    download_data()
