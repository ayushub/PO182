import unittest
from bs4 import BeautifulSoup as BS
from datetime import datetime
import requests

class dPTest(unittest.TestCase):

    def test_result_count(self):
        url = "http://apply.dataprocessors.com.au/"
        print(datetime.now(tz=None))

        start = requests.get(url)
        coos = start.cookies.get_dict()
        coos["pc3o"] = 'd2r22'
        print(coos)

        bsoj = BS(start.text, 'html.parser')
        imgs = bsoj.find_all("img")
        # [src=filled0.gif]
        filled = filter(lambda x: x['src'].startswith('f'), imgs)
        c = len(filled)
        print(c)
        print(datetime.now(tz=None))

        headers = {'Content-type': 'application/x-www-form-urlencoded'}
        resobj = 'title=submit&jobref=PO182&valuee=' + str(c)
        print(resobj)
        x = requests.post(url, data = resobj, cookies= coos, headers= headers)

        print(datetime.now(tz=None))
        print(x.text)


if __name__ == "__main__":
    unittest.main(verbosity=2)