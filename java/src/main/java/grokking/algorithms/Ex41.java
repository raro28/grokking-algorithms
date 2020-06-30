package grokking.algorithms;

import java.util.Arrays;

public class Ex41 {
    public static int iterativeSum(int[] array) {
        int result = 0;
        for (int item : array) {
            result += item;
        }

        return result;
    }

    public static int recursiveSum(int[] array) {
        if (array.length == 0) {
            return 0;
        }
        if (array.length == 1) {
            return array[0];
        }

        return array[0] + recursiveSum(Arrays.stream(array).skip(1).toArray());
    }
}