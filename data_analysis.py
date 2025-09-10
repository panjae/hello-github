# 버전 1.0: 기본 데이터 읽기
import pandas as pd

def load_data(filename):
    """데이터 파일을 읽는 함수"""
    data = pd.read_csv(filename)
    return data

print("데이터 분석 프로그램 v1.0")
