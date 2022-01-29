import requests

ROOT_URL = settings.ROOT_URL
def states_accessor():
    # Go through the doc api examples!
    url = f"{ROOT_URL}/states/all"
    r = requests.get(url)
    if not r.ok:
        raise RuntimeError(r.json())
    print(r.json())

def tracks_accessor():
    url = f"https://opensky-network.org/api/states/all"
    r = requests.get(url)
    if not r.ok:
        raise RuntimeError(r.json())
    print(r.json())