import requests

class Usage:
    op = {
        "gas": "/getGas",
        "water": "/getWtspl",
        "elec": "/getElec"
    }

    def __init__(self, endpoint, de_key):
        self.endpoint = endpoint
        self.de_key = de_key

    def get(self, type_, params):
        if type_ not in self.op:
            print("업승ㅁ")
            return None

        res = requests.get(self.endpoint + self.op[type_], params=params)

        print(res.status_code)
        res.raise_for_status()
        result = res.json()

        items = result["body"]["items"]
        return [
            {"지자체명": i["lclgvNm"],
             "해당년": i["rlvtYr"],
             "사용량": i["avgUseQnt"]
             } for i in items
        ]


if __name__ == "__main__":
    t = Usage(
        endpoint="http://apis.data.go.kr/B552584/kecoapi/cpointEnrgUsqntStatsService",
        de_key="vnSjVe2jiyA+4VcC6vhG0RDz7pEvR5sOck9RDQ+88KnUU/ElRYHDy8LNfGGVc70zZ11ktt8hQvFATO++Bv/7qQ=="
    )

    params = {
        "serviceKey": "vnSjVe2jiyA+4VcC6vhG0RDz7pEvR5sOck9RDQ+88KnUU/ElRYHDy8LNfGGVc70zZ11ktt8hQvFATO++Bv/7qQ==",  # required
        "pageNo": 1,  # required
        "numOfRows": 10,  # required
        "rlvtYr": 2021,  # ~2022
        "lclgvNm": "대전",
        "returnType": "JSON"  # required
    }

    print(t.get("gas", params=params))
    print(t.get("water", params=params))
    print(t.get("elec", params=params))