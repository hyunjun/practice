package com.oreilly.testingscala

import org.scalatest._

//  http://www.scalatest.org/quick_start
class FooTest extends FlatSpec with Matchers  {
  it should "foo's basic method test" in {
    val foo = new Foo(3, 4)
    foo.addition should be (7)
    foo.multiply should be (12)
  }
}
