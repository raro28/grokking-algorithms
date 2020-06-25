using Xunit;

namespace Algorithms.Tests{
    public class SelectionSortTest{
        [Fact]
        public void Test(){
            int[] list = {5,3,6,2,10};
            int[] expected = {2,3,5,6,10};
            Assert.Equal(expected, SelectSort.Sort(list));
        }
    }
}