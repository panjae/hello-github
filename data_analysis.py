# 버전 1.2: 시각화 기능 추가
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def load_data(filename):
    """데이터 파일을 읽는 함수"""
    data = pd.read_csv(filename)
    return data

def basic_stats(data):
    """기본 통계량 계산"""
    return data.describe()

def plot_data(data, column):
    """데이터 시각화"""
    plt.figure(figsize=(10, 6))
    data[column].plot()
    plt.title(f"{column} 데이터 시각화")
    plt.show()

print("데이터 분석 프로그램 v1.2")
