# 주어진 리스트에서 중복된 요소를 제거한 후, 셋으로 변환하는 remove_duplicates_to_set 함수를 작성하시오. 
# 리스트를 인자로 받아 중복이 제거된 셋을 반환해야 한다.
# 아래 함수를 수정하시오.
def remove_duplicates_to_set(arr):
    result = set()
    for item in arr:
        result.add(item)
    return result


# 더 짧은 pythonic 한 코드
# def remove_duplicates_to_set(arr):
#   return set(arr)

result = remove_duplicates_to_set([1, 2, 2, 3, 4, 4, 5])
print(result) 