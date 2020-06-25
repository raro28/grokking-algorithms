package grokking.algorithms;

import java.util.stream.IntStream;

public class SelectionSort {
    private static int findSmallest(int[] array){
        int smallest = array[0];
        int smallestIndex = 0;
        for (int i = 1; i < array.length; i++) {
            if(array[i] < smallest){
                smallest = array[i];
                smallestIndex = i;
            }
        }

        return smallestIndex;
    }

    private static int[] removeElement(int[] array, int index){
        int[] result = new int[array.length - 1];
        
        int i = 0;
        int j = 0;
        while(i < array.length){
            if(i != index){
                result[j] = array[i];
                j++;
            }
            i++;
        }

        return result;
    }

    public static int[] sort(int[] array){
        int[] result =  new int[array.length];
        
        for (int i = 0; i < result.length; i++) {
            int smallestIndex = findSmallest(array);
            result[i] = array[smallestIndex];
            array = removeElement(array, smallestIndex);
        }

        return result;
    }
}