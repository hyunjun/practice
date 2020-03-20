import com.typesafe.config._
import net.ceedubs.ficus.Ficus._

object TestConfig {
  def main(args: Array[String]): Unit = {

    val config = ConfigFactory.load("test.conf")
    println("simple: " + config.getString("my.password1"))
    println("simple: " + config.getString("my.password2"))
    println("simple: " + config.getString("test.password"))

    val complexConfig = config.as[Map[String, Config]]("encryption.versions")
    val keyVersions = complexConfig.keys.toSeq(0)
    println("complex: " + complexConfig)
    println("keyVersions: " + keyVersions)
    println("complex: " + complexConfig.get(keyVersions))
    println("complex: " + complexConfig.mapValues { c => c.getString("key") }.get(keyVersions).getOrElse(""))
  }
}
