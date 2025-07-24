import time
import requests

def main():
    request_count = 10
    url = "https://www.google.com/"
    session = requests.Session()
    # import pdb
    # pdb.set_trace()

    for i in range(request_count):
        print(f"Making {i} request call")
        resp = session.get(url)
        if resp.status_code == 200:
            pass

start = time.time()
main()
end = time.time()
print("Time elapsed: ",(end - start))

