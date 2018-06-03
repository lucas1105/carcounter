import requests
import json
import time


def test_request(url, data):
    """
    Send a test request on the given URL with the given dict data.
    If the request returns HTTP 200 returns the time taken, else return None.

    :param url: URL to send the request
    :type url: str
    :param data: Json data to send inside the request
    :type data: dict
    :return:
    """

    delay = time.time()
    try:
        r = requests.post(url=url, json=data)
        delay = time.time() - delay
        if r.status_code == 200:
            print('Deu bom! Tempo: ' + str(delay) + ' segundos')
        else:
            raise Exception(r.text)
    except Exception as e:
        print(e)
        return None

    return delay

