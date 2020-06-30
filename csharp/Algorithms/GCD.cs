namespace Algorithms
{
    public class GCD
    {
        public static int Get(int a, int b)
        {
            if (a == 0)
            {
                return b;
            }
            if (b == 0)
            {
                return a;
            }

            return Get(b, a % b);
        }
    }
}