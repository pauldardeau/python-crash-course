import requests

# online docs: https://requests.readthedocs.io/en/latest/

# to install: pip install requests

# NOTE: this module is NOT a built-in module. You must install it separately.


# sending get request and saving the response as response object
r = requests.get("http://www.journaldev.com/")

if r.status_code == 200:
    print("response text length = %d" % len(r.text))
else:
    print("http request failed, status code = %d" % r.status_code)

