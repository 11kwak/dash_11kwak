from ast import While
from tqdm import tqdm
import time

color_type = {"노랑" : "#ee9d00", "주황" : "#ee6900", "초록" : "#3c979a", "파랑" : "#1531a3", "검정" : "#323232", "빨강" : "#f54242"}

def split_address(df):
    '''
    df를 input data로 받고 주소명 split이 추가된 df를 retrun 합니다. 
    주소명 컬럼을 추가로 입력받습니다.
    if문 사용하여 지번 주소/도로명 주소를 잘게 쪼개서 모두 정확히 분류할 수 있는 코드로 수정해야 함.
    '''
    print("현재 컬럼명 : ",df.columns)
    time.sleep(1)
    address = input("주소명 컬럼을 입력하세요 :")
    df["광역시/도"] = df[f"{address}"].str.split(" ",expand=True)[0]
    df["시/군/구"] = df[f"{address}"].str.split(" ",expand=True)[1]
    df["동/읍/면"] = df[f"{address}"].str.split(" ",expand=True)[2]
    df["도로명/지번"] = df[f"{address}"].str.split(" ",expand=True)[3]
    
    return df

def color_add(df):
    '''
    df를 input data로 받고 색깔add 컬럼이 추가된 df를 retrun 합니다. 
    '''
    
    df["색깔add"] = 0
    print("현재 컬럼명 : ",df.columns)
    time.sleep(1)
    target_col = input("색깔을 구분할 컬럼명을 입력하세요 :")
    target_col_values = df[f"{target_col}"].unique()
    print(f"색깔을 지정해줄 값들입니다 : {target_col_values}")
    time.sleep(1)
    for i in range(len(target_col_values)):
        print("색깔을 지정해줄 값 :", target_col_values[i])
        time.sleep(1)
        print("색깔 별 코드 예시 : ", color_type)
        pick_color = input(f"{target_col_values[i]}에 원하는 색깔 코드를 입력하세요 :")
        df.loc[df[f"{target_col}"] == f"{target_col_values[i]}", "색깔add"] = pick_color

    return df


def col_plus_col(df):
    '''
    df를 input data로 받고 hovertext 컬럼이 추가된 df를 retrun 합니다. 
    '''
    df["hovertext"] = ""

    print("현재 컬럼명 : ",df.columns)
    time.sleep(1)
    input_column = ""
    column_list = []
    while(input_column != "stop"):
        input_column = input("hover text 에 들어갈 컬럼들을 모두 입력해주세요. stop 을 입력하면 멈출 수 있습니다.  :")
        if input_column == "stop":
            break
        column_list.append(input_column)

    for i in tqdm(range(len(df.index))):
        for j in range(len(column_list)):
            df.loc[i, "hovertext"] += f"/{column_list[j]}: " + str(df.loc[i,f"{column_list[j]}"])

    return df




if __name__ == "__main__":
    print("모듈을 import 해서 실행파일에서 함수로 사용하세요")
