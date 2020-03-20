lazy val root = (project in file(".")).
  settings(
    name := "test-config",
    version := "1.0",
    scalaVersion := "2.12.10"
  )

libraryDependencies += "com.typesafe" % "config" % "1.3.2"
libraryDependencies += "com.iheart" %% "ficus" % "1.4.3"

