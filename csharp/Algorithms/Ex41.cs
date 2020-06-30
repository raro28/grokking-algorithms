namespace Algorithms
{
    using System.Linq;
    public class Ex41
    {
        public static int iterativeSum(int[] array)
        {
            int result = 0;
            foreach (var item in array)
            {
                result += item;
            }

            return result;
        }

        public static int recursiveSum(int[] array)
        {
            if (array.Length == 0)
            {
                return 0;
            }
            if (array.Length == 1)
            {
                return array[0];
            }

            return array[0] + recursiveSum(array.Skip(1).ToArray());
        }
    }
}