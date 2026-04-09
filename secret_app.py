import os

secret_value = os.getenv("SECRET_MESSAGE")
secret_value2 = os.environ.get("SECRET_MESSAGE2")

if secret_value:
    print("SECRET_MESSAGE 값 읽기 성공")
else:
    print("SECRET_MESSAGE 값 없음")

if secret_value2:
    print("SECRET_MESSAGE2 값 읽기 성공")
else:
    print("SECRET_MESSAGE2 값 없음")