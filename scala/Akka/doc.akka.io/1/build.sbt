name := "First example"

version := "0.1"

scalaVersion := "2.13.1"

libraryDependencies ++= Seq(
  "com.typesafe.akka" %% "akka-actor-typed" % "2.6.3",
  "com.typesafe.akka" %% "akka-slf4j" % "2.6.3",
  "ch.qos.logback" % "logback-classic" % "1.2.3"
)
