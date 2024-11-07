

def sum1(a, b):
    return a + b


def safe_sum(a,b):
    '''
    [summary]


    함수나 클래스의 상세 설명


    Args:
        a (int): Description of param1.
        b (int): Description of param2.


    Returns:
        return_type: Description of the return value.
    '''

    if type(a) == type(b):
        return sum1(a,b)
    
    else:
        print('타입이 같지 않음')
        return None
    
    
    #모듈을 사용하는 방식
    #1.모듈을 직접 사용: 파이썬
    
    #2. 다른 모듈에서 임포트해서 사용
if  __name__ == '__main__': # 직접 실행 할 경우 
    print('mod1.py에서 실행')
    print(safe_sum(1,3))
    print(sum1(2,2))