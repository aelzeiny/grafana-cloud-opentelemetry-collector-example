import requests
import time


def spam():
    while True:
        requests.get('http://app:5000/rolldice')
        time.sleep(5)


if __name__ == '__main__':
    time.sleep(5)
    spam()
