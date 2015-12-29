name := "apache-commons"

version := "0.1"

scalaVersion := "2.10.6"

libraryDependencies ++= Seq(
  "org.apache.commons" % "commons-lang3" % "3.4",
  "com.google.code.gson" % "gson" % "2.5",
  "org.scala-lang" % "scala-reflect" % "2.10.6"
  )
