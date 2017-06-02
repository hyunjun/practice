//-----------
//  Spark SQL
//-----------
//  DataFrame = table in RDB
//            = RDDs full of records with a know schema
//            untyped, scala compiler doesn't check the types
//              (RDD[T], typed)
//            untyped transformations
//            starts with SparkSession
/*
import org.apache.spark.sql.SparkSession

val spark = SparkSession
  .builder()
  .appName("My App")
  //.config("spark.som.config.option", "some-value")
  .getOrCreate()
*/
//  1. From an existing RDD
/*
val tupleRDD = ... // RDD[(Int, String, String, String)]
val tupleDF = tupleRDD.toDF("id", "name", "city", "country")  //  column names

case class Person(id: Int, name: String, city: String)
val peopleRDD = ... //  RDD[Person]
val peopleDF = peopleRDD.toDF

case class Person(name: String, city: String)
val peopleRDD = sc.textFile(...)
val schemaString = "name age"
val fields = schemaString.split(" ")
  .map(fieldName => StructFiled(fieldName, StringType, nullable=true))
val schema = StructType(fields)
val rowRDD = peopleRDD
  .map(_.split(","))
  .map(attributes => Row(attributes(0), attributes(1).trim)
val peopleDF = spark.createDataFrame(rowRDD, schema)
*/
//  2. Reading in a specific data source from file
/*
val df = spark.read.json("examples/src/main/resources/people.json")
//  json, csv, parquet, JDBC
*/

//  SQL Literals
/*
peopleDF.createOrReplaceTempView("people")
val adultsDF = spark.sql("SELECT * FROM people WHERE age > 17")
//  SELECT FROM WHERE COUNT
//  HAVING GROUP BY ORDER BY SORT BY
//  DISTINCT JOIN (LEFT|RIGHT|FULL) OUTER JOIN
//  Subqueries e.g. SELECT col FROM (SELECT a + b AS col from t1) t2
*/
/*
case class Employee(id: Int, fname: String, lname: String, age: Int, city: String)
val employeeDF = sc.parallelize(...).toDF
//  registered table "employees"
val sydneyEmployeeDF = spark.sql(
  """SELECT id, lname
     FROM employees
     WHERE city = "Sydney"
     ORDER BY id
  """)
*/


//---------------
//  DataFrames(1)
//---------------
