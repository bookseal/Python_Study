from time import sleep
from tqdm import tqdm

def slow_generator():
    for i in range(10):
        sleep(0.2)  # 시간이 걸리는 작업
        yield i  # 하나씩 결과를 생성

# tqdm이 yield를 감싸면서 상태 표시 가능!
for item in tqdm(slow_generator(), desc="Processing"):
    print(f"Processed item: {item}")