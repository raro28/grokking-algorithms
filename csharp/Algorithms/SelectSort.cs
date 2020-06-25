namespace Algorithms{
    public class SelectSort{

        private static int FindSmallest(int[] array){
            int smallest = array[0];
            int smallestIndex = 0;
            for (var i = 0; i < array.Length; i++)
            {
                if(array[i] < smallest){
                    smallest = array[i];
                    smallestIndex = i;
                }
            }

            return smallestIndex;
        }

        private static int[] RemoveElement(int[] array, int index){
            var result = new int[array.Length - 1];

            int i = 0;
            int j = 0;

            while(i < array.Length){
                if(i != index){
                    result[j] = array[i];

                    j++;
                }
                i++;
            }


            return result;
        }

        public static int[] Sort(int[] array){
            var result = new int[array.Length];

            for (var i = 0; i < result.Length; i++)
            {
                int smallestIndex = FindSmallest(array);
                result[i] = array[smallestIndex];
                array = RemoveElement(array, smallestIndex);
            }

            return result;
        }
    }
}