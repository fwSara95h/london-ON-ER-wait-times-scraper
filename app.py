import requests
from bs4 import BeautifulSoup
from helper_fns import reqStatus
from file_builders import log_data
from datetime import datetime
import time


def main(data_filename='ER-wait-times.csv',
         dump_filename='scrape-log-ER-wait.csv'):
    time_now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    wait_time_fields = []
    try:
        scrape_url = ''
        reqRet = requests.get(scrape_url)
        rStatus = reqStatus(reqRet)
        soup = BeautifulSoup(reqRet.content, 'html.parser')

        wait_time_fields = soup.select('h1:has(+a[href])')
        if not wait_time_fields:
            log_data([
                time_now, 'Warning', 'No Wait Times Detected', repr(rStatus)
            ], filename=dump_filename)
            return

        if len(wait_time_fields != 2):
            log_data([
                time_now,
                'Warning',
                'Unexpected Number of Wait Times Detected',
                repr(wait_time_fields)
            ], filename=dump_filename)
            return

        wait_times = [(
            float(h.get_text(' ', strip=True).rstrip(' Hours')),
            repr(h).split('<!--Start:', 1)[-1].split('-->', 1)[0]
        ) for h in wait_time_fields]

        hours_1, title_1 = wait_times[0]
        hours_2, title_2 = wait_times[1]
        log_data([time_now, hours_1, hours_2],
                 ['Time', 'UH', 'VH'], data_filename)

        if (title_1, title_2) == ('UHWaitTimeValue', 'VHWaitTimeValue'):
            log_data([
                time_now, 'Success', 'All as expected',
                f'{title_1}: {hours_1} hours; {title_2}: {hours_2} hours'
            ], filename=dump_filename)
        else:
            log_data([
                time_now,
                'Warning',
                'Unexpected Wait Time Titles Detected',
                repr(wait_time_fields)
            ], filename=dump_filename)
    except Exception as e:
        log_data([
            time_now, 'Error', repr(e), repr(wait_time_fields)
        ], filename=dump_filename)


if __name__ == '__main__':
    scrape_interval = 15  # in minutes
    while True:
        main()
        time.sleep(scrape_interval*60)
