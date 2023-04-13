import java.util.Scanner;
import java.util.Arrays;

public class greedy {
    public static void main(String[] args) {
        thisIsCodingTestForGettingJob codingTest = new thisIsCodingTestForGettingJob();
        codingTest.chapter3q4();
    }
}

// 이것이 취업을 위한 코딩테스트다. with Python
class thisIsCodingTestForGettingJob {
    Scanner sc = new Scanner(System.in);
    /*
     * P/92 큰 수의 법칙
     * https://github.com/ndb796/python-for-coding-test/blob/master/3/2.java
    * === input example ===
5 8 3
2 4 5 4 6
    * === output example ===
    * 46
     */
    void chapter3q2() {
        int n = sc.nextInt();
        int m = sc.nextInt();
        int k = sc.nextInt();

        int[] nums = new int[n];
        for (int i = 0; i < n; i++) {
            nums[i] = sc.nextInt();
        }

        Arrays.sort(nums);

        int count = (m / (k + 1)) * k + m % (k + 1);
        int answer = nums[n - 1] * count + nums[n - 2] * (m - count);
        System.out.println(answer);
        return;
    }

    /*
     * P/96 숫자 카드 게임
     *  https://github.com/ndb796/python-for-coding-test/blob/master/3/3.java
     * === input example ===
3 3
3 1 2
4 1 4
2 2 2
     * === output example ===
     * 2
     * === input example ===
2 4
7 3 1 8
3 3 3 4
     * === output example ===
     * 3
     */
    void chapter3q3() {
        int n = sc.nextInt();
        int m = sc.nextInt();
        int result = 0;
        for (int i=0; i<n; i++) {
            int min_value = 10000;
            for (int j=0; j<m; j++){
                int x = sc.nextInt();
                min_value = Math.min(min_value, x);
            }
            result = Math.max(result, min_value);
        }
        System.out.println(result);
        return;
    }

    /*
     * P/99 1이 될 때까지
     * === input example ===
25 5
     * === output example ===
     * 2
     */
    void chapter3q4() {
        int n = sc.nextInt();
        int k = sc.nextInt();
        int cnt = 0;
        while ( n != 1) {
            cnt++;
            if ( n % k == 0){
                n = n/k;
            } else {
                n--;
            }
        }
        System.out.println(cnt);
        return;
    }
}