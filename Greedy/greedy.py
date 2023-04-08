from functools import wraps
import time


def time_measurement(func, ):
    @wraps(func) # for doctest
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        print(f"소요시간 : {time.time()-start_time} seconds")
        return result
    return wrapper

# 이것이 취업을 위한 코딩테스트다. with Python
class this_is_coding_test_for_getting_job:
    def __init__(self):
        pass
    
    @time_measurement
    def chapter3q2_mine(self, *args):
        '''
        P/92 큰 수의 법칙
        https://github.com/ndb796/python-for-coding-test/blob/master/3/2.py
        >>> t.chapter3q2_mine("5 8 3", "2 4 5 4 6")
        46
        '''
        n, m, k = map(int, args[0].split())
        nums = sorted(list(map(int, args[1].split())))
        count = m//(k+1)*k + m % (k+1)
        answer = nums[-1]*count + nums[-2]*(m-count)
        print(answer)
        return

    @time_measurement
    def chapter3q3_mine(self, *args):
        '''
        P/96 숫자 카드 게임
        https://github.com/ndb796/python-for-coding-test/blob/master/3/4.py
        >>> t.chapter3q3_mine("3 3", "3 1 2", "4 1 4", "2 2 2")
        2
        >>> t.chapter3q3_mine("2 4", "7 3 1 8", "3 3 3 4")
        3
        '''
        n, m = map(int, args[0].split())
        mat = [min(map(int, args[idx].split())) for idx in range(1, n+1)]
        print(max(mat))
        return

    
if __name__ == "__main__":
    import doctest
    doctest.testmod(extraglobs={'t': this_is_coding_test_for_getting_job()})
