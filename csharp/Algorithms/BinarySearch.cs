namespace Algorithms{
    public static class BinarySearch{

        public static int? Search(int[] list, int item){
            int low = 0;
            int high = list.Length - 1;
            while(low <= high){
                int mid = (low + high) / 2;
                int guess = list[mid];
                if(guess == item){
                    return mid;
                } else if(guess > item){
                    high = mid - 1;
                } else{
                    low = mid + 1;
                }
            }

            return null;
        }
    }
}