package com.oreilly.testingscala

//import org.scalatest.FunSpec
//import org.scalatest.matchers.ShouldMatchers
import org.scalatest._

/*class AlbumTest extends FunSpec with ShouldMatchers  {
  describe("An Album") {
    it ("can add an Artist object to the album") {
      val album = new Album("Thriller", 1981, new Artist("Michael", "Jackson"))
    }
  }
}*/
class AlbumTest extends FlatSpec with Matchers  {
  it should "can add an Artist object to the album" in {
    val album = new Album("Thriller", 1981, new Artist("Michael", "Jackson"))
  }
}
