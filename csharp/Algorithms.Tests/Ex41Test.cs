using Xunit;

namespace Algorithms.Tests
{
    public class Ex41Test
    {
        [Fact]
        public void Test()
        {
            int[] array = { 2, 4, 6 };
            Assert.Equal(12, Ex41.iterativeSum(array));
            Assert.Equal(12, Ex41.recursiveSum(array));
        }
    }
}