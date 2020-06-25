package grokking.algorithms;

public class BinarySearch {
    public static Integer search(int[] list, int item){
        int low = 0;
        int high = list.length - 1;
        while(low <= high){
            int mid = (low + high) / 2;
            int guess = list[mid];
            if(guess == item){
                return mid;
            }else if(guess > high){
                high = mid - 1;
            } else {
                low = mid + 1;
            }
        }

        return null;
    }
}