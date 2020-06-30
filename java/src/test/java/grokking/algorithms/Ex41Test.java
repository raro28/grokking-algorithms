package grokking.algorithms;

import org.junit.Test;

public class Ex41Test {
    @Test
    public void test() {
        int[] array = { 2, 4, 6 };
        org.junit.Assert.assertEquals(12, Ex41.iterativeSum(array));
        org.junit.Assert.assertEquals(12, Ex41.recursiveSum(array));
    }
}