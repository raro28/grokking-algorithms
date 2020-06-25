package grokking.algorithms;

import org.junit.Assert;
import org.junit.Test;

public class SelectionSortTest {

    @Test
    public void test(){
        int[] expected = new int[] {2,3,5,6,10};
        int[] array = new int[] {5,3,6,2,10};
        Assert.assertArrayEquals(expected, SelectionSort.sort(array));
    }
}