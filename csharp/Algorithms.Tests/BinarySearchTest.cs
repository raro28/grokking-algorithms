using System;
using Xunit;
using Algorithms;

namespace Algorithms.Tests
{
    public class BinarySearchTest
    {
        [Fact]
        public void Test()
        {
            int[] myList = {1,3,5,7,9};
            Assert.True(BinarySearch.Search(myList,3) == 1);
            Assert.Null(BinarySearch.Search(myList,-1));
        }
    }
}
