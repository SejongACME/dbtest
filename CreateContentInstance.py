# import requests, random, string


# # API로 부터 데이터를 얻어옴
# API_KEY = "4a59596f57746b6d373464514e7952"
# # 호출하려는 API의 URL을 설정합니다.
# api_url = f"http://openapi.seoul.go.kr:8088/{API_KEY}/json/TimeAverageCityAir/1/2/201303061100"

# # API 호출 함수
# def call_api(api_url):
#     try:
#         # GET 요청
#         response = requests.get(api_url)

#         # HTTP 상태 코드 확인
#         if response.status_code == 200:
#             # API 응답을 JSON 형식으로 파싱
#             data = response.json()
#             return data
#         else:
#             # 에러 출력
#             print(f"Error: {response.status_code} - {response.text}")
#             return None
#     except Exception as e:
#         print(f"An error occurred: {e}")
#         return None
    
# def request_identifier():
#     n = 10
#     rqi = ""
#     for i in range(n):
#         rqi += str(random.choice(string.ascii_letters + string.digits))
#     return rqi
    
# def make_contentinstance(MSRRGN_CD):
#     url = "http://127.0.0.1:8080/cse-in/Gwangjin-Gu"
#     rqi = request_identifier()
#     header = {
#         "Content-Type" : "application/json; ty=4",
#         "X-M2M-Origin" : "CAdmin",
#         "X-M2M-RI" : rqi,
#         "X-M2M-RVI" : "3"
#     }
#     body = {
#         "m2m:cin": {
#             "cnf": "text/plain:0",
#             "con": MSRRGN_CD,
#             "rn": "testResource"
#         }
#     }
#     return header, body, url



# # API를 호출하고 결과 가져오기
# result = call_api(api_url)
# # 데이터로부터 필요한 값을 추출해냄
# msrrgn_cd = result["TimeAverageCityAir"]["row"][0].get("MSRRGN_CD")

# # 결과를 출력
# if result:
#     print("API 호출 결과:", msrrgn_cd)

# # 해당 값을 con에 넣고 ACME에 리퀘스트를 넣음
# header_cin, body_cin, url_cin = make_contentinstance(msrrgn_cd)
# http_post_request_cin = requests.post(url_cin, headers=header_cin, json=body_cin)


import json
import requests
import random
import string

def request_identifier():
    n = 10
    rqi = ""
    for i in range(n):
        rqi += str(random.choice(string.ascii_letters + string.digits))
    return rqi

def make_container():
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
            "mbs": 10000,
            "mni": 10,
            "rn": "Gwangjin-Gu"
        }
    }
    return header, body, url
    
def make_contentinstance():
    url = "http://127.0.0.1:8080/cse-in/Gwangjin-Gu"
    rqi = request_identifier()
    header = {
        "Content-Type" : "application/json; ty=4",
        "X-M2M-Origin" : "CAdmin",
        "X-M2M-RI" : rqi,
        "X-M2M-RVI" : "3"
    }
    body = {
        "m2m:cin": {
            "cnf": "text/plain:0",
            "con": "1",
            "rn": "weather"
        }
    }
    return header, body, url

header_cnt, body_cnt, url_cnt = make_container()
header_cin, body_cin, url_cin = make_contentinstance()

http_post_request_cnt = requests.post(url_cnt, headers=header_cnt, json=body_cnt)
http_post_request_cin = requests.post(url_cin, headers=header_cin, json=body_cin)