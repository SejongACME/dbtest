from RequestIdentifier import request_identifier

def make_container(resourceName: str):
    url = "http://127.0.0.1:8080/id-in"
    rqi = request_identifier()
    header = {
        "Content-Type" : "application/json; ty=3",
        "X-M2M-Origin" : "CAdmin",
        "X-M2M-RI" : rqi,
        "X-M2M-RVI" : "3"
    }
    body = {
        "m2m:cnt": {
            "mbs": 10000, # maxByteSize
            "mni": 10, # maxNrOfInstances (컨테이너 안에 넣을 수 있는 최대 데이터 개수인듯)
            "rn": resourceName
        }
    }
    return header, body, url