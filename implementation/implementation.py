if __package__ is None:
    import sys
    from os import path
    sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))
    from util import error_measurement, time_measurement
else:
    from ..util import error_measurement, time_measurement


# 이것이 취업을 위한 코딩테스트다. with Python
class this_is_coding_test_for_getting_job:
    def __init__(self):
        pass

    @error_measurement
    @time_measurement
    def chapter4q1(self, *args, **kwargs):
        """
        P/110 상하좌우
        https://github.com/ndb796/python-for-coding-test/blob/master/4/1.py
        >>> t.chapter4q1("5", "R R R U D D", time_limit=1)
        3 4
        """
        n = int(args[0])
        if not (1 <= n <= 100):
            raise Exception("input error")
        plan = args[1].split()

        # Up, Down, Left, Right
        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]
        moves = ['U', 'D', 'L', 'R']
        x, y = 1, 1

        for p in plan:
            direc = moves.index(p)
            nx = x + dx[direc]
            ny = y + dy[direc]
            if nx < 1 or ny < 1 or nx > n or ny > n:
                continue
            x, y = nx, ny

        return f"{x} {y}"

    @error_measurement
    @time_measurement
    def chapter4q2(self, *args, **kwargs):
        """
        P/113
        https://github.com/ndb796/python-for-coding-test/blob/master/4/2.py
        >>> t.chapter4q2("5", time_limit=2)
        11475
        """
        n = int(args[0])
        if not (0 <= n <= 23):
            raise Exception("input error")
        cnt = 0
        for hour in range(n+1):
            for min in range(60):
                for second in range(60):
                    if '3' in str(hour)+str(min)+str(second):
                        cnt += 1
        return cnt

    @error_measurement
    @time_measurement
    def chapter4q3(self, *args, **kwargs):            
        """
        P/115
        https://github.com/ndb796/python-for-coding-test/blob/master/4/3.py
        >>> t.chapter4q3("a1", time_limit=1)
        2
        """
        cur = args[0]
        x, y = ord(cur[0])-ord('a'), int(cur[1])-1
        print(x, y)
        if not ( 0 <= x <= 7 or 0 <= y <= 7):
            raise Exception("input error")
        # lhu, lhd, rhu, rhd, uvl, uvr, dvl, dvr
        move = ['h']

if __name__ == "__main__":
    import doctest
    doctest.testmod(extraglobs={'t': this_is_coding_test_for_getting_job()})
