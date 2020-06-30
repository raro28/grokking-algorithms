package grokking.algorithms;

public class GCD {
    public static int get(int a, int b) {
        if (a == 0) {
            return b;
        }
        if (b == 0) {
            return a;
        }

        return get(b, a % b);
    }
}