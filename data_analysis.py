# 버전 1.1: 기본 통계 추가
import pandas as pd
import numpy as np

def load_data(filename):
    """데이터 파일을 읽는 함수"""
    data = pd.read_csv(filename)
    return data

def basic_stats(data):
    """기본 통계량 계산"""
    return data.describe()

print("데이터 분석 프로그램 v1.1")
