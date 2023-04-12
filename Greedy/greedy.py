from functools import wraps
import time


# 에러 처리
def error_measurement(func):
    @wraps(func)  # for doctest
    def wrapper(*args, **kwargs):
        try:
            result = func(*args, **kwargs)
        except Exception as e:
            match str(e):
                case "input error":
                    result = "input"
                case "timeout error":
                    result = "timeout"
                case _:
                    result = f" > error : {e}"
        finally:
            print(result)
        return
    return wrapper

# 시간 측정
def time_measurement(func):
    @wraps(func)  # for doctest
    def wrapper(*args, **kwargs):
        time_limit = kwargs["time_limit"]
        start_time = time.time()
        result = func(*args, **kwargs)
        if time_limit < time.time()-start_time:
            raise Exception("timeout error")
        return result
    return wrapper

# 이것이 취업을 위한 코딩테스트다. with Python
class this_is_coding_test_for_getting_job:
    def __init__(self):
        pass

    @error_measurement
    @time_measurement
    def chapter3q2_mine(self, *args, **kwargs):
        '''
        P/92 큰 수의 법칙
        https://github.com/ndb796/python-for-coding-test/blob/master/3/2.py
        >>> t.chapter3q2_mine("5 8 3", "2 4 5 4 6", time_limit=1)
        46
        >>> t.chapter3q2_mine("1 8 3", " 2 4 5 4 6", time_limit=1)
        input
        >>> t.chapter3q2_mine("5 8 3", " 2 4 5 4 6", time_limit=0.0000000001)
        timeout
        '''
        n, m, k = map(int, args[0].split())
        if not (2 <= n <= 1000) or not (1 <= m <= 10000) or not (1 <= k <= 10000):
            raise Exception("input error")
        nums = sorted(list(map(int, args[1].split())))
        if not (1 <= nums[-2] < 10000):
            raise Exception("input error")
        count = m//(k+1)*k + m % (k+1)
        return nums[-1]*count + nums[-2]*(m-count)

    @error_measurement
    @time_measurement
    def chapter3q3_mine(self, *args, **kwargs):
        '''
        P/96 숫자 카드 게임
        https://github.com/ndb796/python-for-coding-test/blob/master/3/4.py
        >>> t.chapter3q3_mine("3 3", "3 1 2", "4 1 4", "2 2 2", time_limit=1)
        2
        >>> t.chapter3q3_mine("2 4", "7 3 1 8", "3 3 3 4", time_limit=1)
        3
        >>> t.chapter3q3_mine("101 1", "7 3 1 8", "3 3 3 4", time_limit=1)
        input
        '''
        n, m = map(int, args[0].split())

        if not (1 <= n <= 100) or not (1 <= m <= 100):
            raise Exception("input error")
        # nums 입력값 테스트 추가해야함.
        mat = [min(map(int, args[idx].split())) for idx in range(1, n+1)]
        return max(mat)

    @error_measurement
    @time_measurement
    def chapter3q4_mine(self, *args, **kwargs):
        '''
        P/99 1이 될 때까지
        >>> t.chapter3q4_mine("25 5", time_limit=1)
        2
        >>> t.chapter3q4_mine("25 3", time_limit=1)
        6
        >>> t.chapter3q4_mine("25 28", time_limit=1)
        input
        '''
        n, k = map(int, args[0].split())
        if not (2 <= n <= 100000) or not (2 <= k <= 100000) or n < k:
            raise Exception("input error")
        cnt = 0
        while n != 1:
            cnt += 1
            if n % k == 0:
                n /= k
            else:
                n -= 1
        return cnt


if __name__ == "__main__":
    import doctest
    doctest.testmod(extraglobs={'t': this_is_coding_test_for_getting_job()})

    # this_is = this_is_coding_test_for_getting_job()
    # this_is.chapter3q4_mine("5 2", time_limit=0.00000000000005)
