using Xunit;

namespace Algorithms.Tests{
    public class GCDTest{

        [Fact]
        public void Test()
        {
            Assert.Equal(80, GCD.Get(1680,640));
        }
    }
}