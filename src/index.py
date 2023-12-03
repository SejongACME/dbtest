import requests

from CallWeatherlAPI import call_weather_api
from CreateContainer import make_container
from CurrentTime import generate_hourly_time
from CreateInstance import make_contentinstance

# API KEY
API_KEY = "4a59596f57746b6d373464514e7952"
LATEST_TIME = generate_hourly_time()
# 호출하려는 API의 URL을 설정합니다.
# 방법: 일단 날짜형식(MSRDT)을 202306151300(년도, 월, 일, 시간)을 한시간 단위로 수정해서 api_url의 뒷부분을 수정함
api_url = f"http://openAPI.seoul.go.kr:8088/{API_KEY}/json/TimeAverageAirQuality/1/25/{LATEST_TIME}"

# API 로부터 데이터 받아오기
data = call_weather_api(api_url)
# print(data)

# 컨테이너 생성
# 컨테이너 이름: NO2, O3, CO, SO2, PM10, PM25
surveyList = ["NO2", "O3", "CO", "SO2", "PM10", "PM25"]
for survey in surveyList:
    header_cnt, body_cnt, url_cnt = make_container(survey)
    requests.post(url_cnt, headers=header_cnt, json=body_cnt)

# 인스턴스 생성
# 그리고 반복문으로 각 컨테이너에 데이터를 넣기
# print(data["TimeAverageAirQuality"]["row"])

# 조사 리스트 반복문
for li in surveyList:
    for element in data["TimeAverageAirQuality"]["row"]:
        h, b, u = make_contentinstance(li, element["MSRSTE_NM"], element[li])
        print(element["MSRSTE_NM"])
        requests.post(url=u, headers=h, json=b)
    


