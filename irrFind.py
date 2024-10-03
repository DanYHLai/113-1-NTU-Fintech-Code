import numpy as np
from scipy.optimize import brentq

# 定義 NPV 函數
def npv(rate, cashFlowVec, cashFlowPeriod, compoundPeriod):
    total_value = 0
    n = len(cashFlowVec)

    for i in range(n):
        try:
            if cashFlowPeriod == 12:
                if compoundPeriod in [12, 6, 4, 3, 2, 1]:
                    total_value += cashFlowVec[i] / (1 + rate / 12 * compoundPeriod) ** (i * cashFlowPeriod / compoundPeriod)

            elif cashFlowPeriod == 6:
                if compoundPeriod in [6, 3, 2, 1]:
                    total_value += cashFlowVec[i] / (1 + rate / 12 * compoundPeriod) ** (i * cashFlowPeriod / compoundPeriod)

            elif cashFlowPeriod == 4:
                if compoundPeriod in [4, 2, 1]:
                    total_value += cashFlowVec[i] / (1 + rate / 12 * compoundPeriod) ** (i * cashFlowPeriod / compoundPeriod)

            elif cashFlowPeriod == 3:
                if compoundPeriod in [3, 1]:
                    total_value += cashFlowVec[i] / (1 + rate / 12 * compoundPeriod) ** (i * cashFlowPeriod / compoundPeriod)

            elif cashFlowPeriod == 2:
                if compoundPeriod in [2, 1]:
                    total_value += cashFlowVec[i] / (1 + rate / 12 * compoundPeriod) ** (i * cashFlowPeriod / compoundPeriod)

            elif cashFlowPeriod == 1:
                total_value += cashFlowVec[i] / (1 + rate / 12) ** (i * cashFlowPeriod / compoundPeriod)

        except ZeroDivisionError:
            return 0  # 若出現除以零的情況，返回 0

    return total_value

# 自動擴展區間來尋找變號的範圍
def find_sign_change(cashFlowVec, cashFlowPeriod, compoundPeriod, start=-1, end=1, step=0.1):
    while start > -100 and end < 100:
        try:
            if npv(start, cashFlowVec, cashFlowPeriod, compoundPeriod) * npv(end, cashFlowVec, cashFlowPeriod, compoundPeriod) < 0:
                return start, end
        except OverflowError:
            pass
        start -= step
        end += step
    return None

# 使用 Brent's 方法計算 IRR，並在錯誤時跳過計算
def irrFind(cashFlowVec, cashFlowPeriod, compoundPeriod):
    try:
        # 自動尋找變號的區間
        interval = find_sign_change(cashFlowVec, cashFlowPeriod, compoundPeriod)
        if interval:
            start, end = interval
            try:
                irr = brentq(lambda r: npv(r, cashFlowVec, cashFlowPeriod, compoundPeriod), start, end)
                return irr
            except ValueError as e:
                # 捕捉 Brent 方法中的錯誤，返回 0 表示計算失敗
                return 0
        else:
            # 如果找不到變號區間，返回 0
            return 0
    except Exception as e:
        # 捕捉其他潛在錯誤，返回 0 表示跳過該行
        return 0