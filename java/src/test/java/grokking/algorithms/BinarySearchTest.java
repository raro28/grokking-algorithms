package grokking.algorithms;

import org.junit.Test;

/**
 * Unit test for simple App.
 */
public class BinarySearchTest 
{
    /**
     * Rigorous Test :-)
     */
    @Test
    public void test()
    {
        int[] myList = {1,3,5,7};
        org.junit.Assert.assertTrue(BinarySearch.search(myList, 3) == 1);
        org.junit.Assert.assertNull(BinarySearch.search(myList, -1));
    }
}
