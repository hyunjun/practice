import org.apache.commons.lang3.StringEscapeUtils
import com.google.gson._

object Test {

  //  http://stackoverflow.com/questions/9913971/scala-how-can-i-get-an-escaped-representation-of-a-string
  //  http://stackoverflow.com/questions/25189608/cant-import-scala-reflect-runtime-universe
  /*def escape(raw: String): String = {
    import scala.reflect.runtime.universe._
    Literal(Constant(raw)).toString
  }*/
  //  http://www.ietf.org/rfc/rfc4627.txt
  //  https://commons.apache.org/proper/commons-lang/apidocs/src-html/org/apache/commons/lang3/StringEscapeUtils.html
  def escapeJson(raw: String): String = {
    raw.replace("\\", "\\\\").replace("\"", "\\\"").replace("/", "\\/")
  }

  val gson = new Gson
  def gsonEscapeJson(raw: String): String = {
    val escaped = gson.toJson(raw)
    escaped.substring(1, escaped.length - 1)
  }

  def main(args: Array[String]) {
    val s = "test escape sequence \"  \\n \\"
    println("original %s".format(s))
    println(StringEscapeUtils.escapeJson(s))
    println(gsonEscapeJson(s))
    val s1 = "이후 최택의 방으로 들어온 김선우는 \"사랑하는 친구야\"라며 비밀로 해달라고 부탁했다."
    println("original %s".format(s1))
    /*println(StringEscapeUtils.escapeCsv(s1))
    println(StringEscapeUtils.escapeEcmaScript(s1))
    println(StringEscapeUtils.escapeHtml3(s1))
    println(StringEscapeUtils.escapeHtml4(s1))
    println(StringEscapeUtils.escapeJava(s1))
    println(StringEscapeUtils.escapeJson(s1))
    println(StringEscapeUtils.escapeXml10(s1))
    println(StringEscapeUtils.escapeXml11(s1))*/
    println(StringEscapeUtils.escapeJson(s1))
    println(new String(StringEscapeUtils.escapeJson(s1).toString.getBytes("UTF-8"), "UTF-8"))
    println(escapeJson(s1))
    println(gsonEscapeJson(s1))
    val s2 = "('"
    println("original %s".format(s2))
    println(StringEscapeUtils.escapeJson(s2))
    println(escapeJson(s2))
    println(gsonEscapeJson(s2))
  }
}
