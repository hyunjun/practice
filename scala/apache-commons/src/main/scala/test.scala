import org.apache.commons.lang3.StringEscapeUtils

object Test {
  def main(args: Array[String]) {
    val s = "test escape sequence \"  \\n \\"
    println(s)
    println(StringEscapeUtils.escapeJson(s))
  }
}
