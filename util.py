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
