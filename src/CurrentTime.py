from datetime import datetime, timedelta

def generate_hourly_time():
    # 현재 시간을 가져옵니다.
    current_time = datetime.now()

    # 1시간 전의 시간을 계산합니다.
    new_time = current_time - timedelta(hours=1)

    # 년도, 월, 일, 시간을 나타내는 문자열을 생성합니다.
    formatted_time = new_time.strftime("%Y%m%d%H00")

    return formatted_time

