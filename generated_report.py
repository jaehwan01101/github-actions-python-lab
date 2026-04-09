from datetime import datetime

with open("report.txt", "w" ,encoding="utf-8") as f:
    f.write("github actions report\n")
    f.write(f"generated at: {datetime.now()}\n")

print("report.txt 생성 완료")