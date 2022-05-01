import json
import logging
import grequests
import time
import urllib

start_time = time.time()
success = 0


def exception_handler(request, exception):
    print("Exception Details ::  ", exception)


requestCount = 500

urls = ['your Api Url here'] * requestCount
headers = {'content-type': 'application/vnd.api+json',
           'Authorization': 'your auth here'}

# proxie = {'http': 'http://93.185.123.154:3128', 'https': 'https://93.185.123.154:3128'}
# proxies = proxie, timeout=0.05


try:
    rs = (grequests.get(u, headers=headers) for u in urls)
    # print(str(rs.text))
    requests = grequests.map(rs, exception_handler=exception_handler)
    for r in requests:
        print(str(r))
        if r.status_code == 200:
            parsed_body = str(r.text)
            c = json.loads(parsed_body)
            # print(str(c))
            message = str(c['message'])
            if message == 'Questions List':
                success = success + 1
            # print(message)
            else:
                print("\n\n***** failed with message :", message)
                if 'exception' in c:
                    exception = c['exception']
                    print("failed with exception :", exception)
        else:
            print("info:: " + str(r.content))


except Exception as e:
    print("Exception :: " + str(e))

print("\nTotal request:  ", requestCount)
print("Success:  ", success)
print("Failed:  ", requestCount - success)
end = time.time() - start_time
print("\nTime elapsed  %ss" % round(end, 2))
