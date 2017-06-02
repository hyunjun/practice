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
//  Basic Spark SQL Data Types
//  Scala Type vs. SQL Type
//  Byte > ByteTYpe, ... String > StringType
//  Array[T] > ArrayType(elementType, containsNull)
//    e.g. Array[String] > ArrayType(StringType, true)
//  Map[K, V] > MapType(keyType, valueType, valueContainsNull)
//  case class > StructType(List[StructFields])
//    e.g. case class Person(name: String, age: Int)
//         StructType(List(StructField("name", StringType, true),
//                         StructField("age", IntegerType, true)))
//    Complex Data Types can be combined
//    case class Account(balance: Double, employees: Array[Employee])
//    case class Employee(id: Int, name: String, jotTitle: String)
//    case class Project(title: String, team: Array[Employee], acct: Account)

//  import org.apache.spark.sql.types._

//  DataFrames Operations are more structured
/*
case class Employee(id: Int, fname: String, lname: String, age: Int, city: String)
val employeeDF = sc.parallelize(...).toDF
employeeDF.show()
employeeDF.printschema()
//  def select(col: String, cols: String*): DataFrame
//  def agg(expr: Column, exprs: Column*): DataFrame
//  def groupBy(col1: String, cols: String*): DataFrame
//  def join(right: DataFrame): DataFrame
*/

//  Specifying Columns, 1 & 2 is better than 3
/*
//  1. Using $-notation
import spark.implicits._
df.filter($"age" > 18)
//  2. Referring to the DataFrame
df.filter(df("age") > 18)
//  3. Using SQL query string
df.filter("age > 18")
*/

//  Exmample; obtain just IDs and user names in a specific city, say, Sydney
/*
val sydneyEmployeeDF = employeeDF.select("id", "lname")
                                 .where("city == 'Sydney'")
                                 .orderBy("id")
val over30 = employeeDF.filter("age > 30").show()
employeeDF.filter(($"age"> 25) && ($"city" === "Sydney")).show()
*/

//  Grouping and Aggregating on DataFrames
//  a groupBy returns RelationalGroupedDataset
//  aggregation; count, sum, max, min, avg, stddev, first, last
/*
df.groupBy($"attribute1")
  .agg(sum($"attribute2"))
df.grouBy($"attribute1")
  .count($"attribute2")
*/
//  Example
/*
case class Listring(street: String, zip: Int, price: Int)
val listingsDF = ...
import org.apache.spark.sql.functions._
val mostExpensiveDF = listingsDF.groupBy($"zip").max("price")
val leastExpensiveDF = listingsDF.groupBy($"zip").min("price")
*/
//  Example
/*
case class Post(authorID: Int, subforum: String, likes: Int, date: String)
val postsDF = ...
import org.apache.spark.sql.functions._
val rankedDF =
  postsDF.groupBy($"authorID", $"subforum")
         .agg(count($"authorID")) //  new DF with columns authorID, subforum, count(authorID)
         .orderBy($"subforum", $"count(authorID)".desc)
*/

//---------------
//  DataFrames(2)
//---------------
//  drop rows/records with unwanted values like null or "NaN"
//  drop()
//  drop("all")
//  drop(Array("id", "name"))

//  fill(0)
//  fill(Map("minBalance" -> 0))
//  replace(Array("id"), Map(1234 -> 8923))

//  actions
//  collect(): Array[Row]
//  count(): Long
//  first(): Row/head(): Row
//  show(): Unit
//  take(n: Int): Array[Row]

//  join
//  inner, outer, left_outer, right_outer, leftsemi
//  df1.join(df2, $"df1.id" === $"df2.id")
//  df1.join(df2, $"df1.id" === $"df2.id", "right_outer")

//  Example
case class Abo(id: Int, v: (String, String))
case class Loc(id: Int, v: String)

val as = List(Abo(101, ("Ruetli", "AG")), Abo(102, ("Brelaz", "DemiTarif")),
              Abo(103, ("Gress", "DemiTarifVisa")), Abo(104, ("Schatten", "DemiTarif")))
//val abosDF = sc.parallelize(as).toDF
val ls = List(Loc(101, "Bern"), Loc(101, "Thun"), Loc(102, "Lausanne"), Loc(102, "Geneve"),
              Loc(102, "Nyon"), Loc(103, "Zurich"), Loc(103, "St-Gallen"), Loc(103, "Chur"))
//val locationsDF = sc.parallelize(ls).toDF

//  default inner join
//val trackedCustomersDF = abosDF.join(locationsDF, abosDF("id") === locationsDF("id"))

//val trackedWithOptionalLocationsDF =
// abosDF.join(locationsDF, abosDF("id") === locationsDF("id"), "left_outer")
//  id = 104 has null

//  Example
case class Demographic(id: Int,
                       age: Int,
                       codingBootcamp: Boolean,
                       country: String,
                       gender: String,
                       isEthnicMinority: Boolean,
                       servedInMilitary: Boolean)
//val demographcisDF = sc.textFile(...).toDF
case class Finances(id: Int,
                    hasDebt: Boolean,
                    hasFinancialDependents: Boolean,
                    hasStudentLoans: Boolean,
                    income: Int)
//val financesDF = sc.textFile(...).toDF
/*
//  count Swiss students who have debt & financial dependents
//  RDD based solutions have various performances
//  almost the same with RDD 2.(RDD fastest solution)
demographicsDF.join(finanacesDF, demographicsDF("ID") === financesDF("ID"), "inner")
  .filter($"HasDebt" && $"HasFinancialDependents")
  .filter($"CountryLive" === "Switzerland")
  .count
*/

//  Optimizations
//  Catalyst, Spark SQL's query optimizer
//  Tungsten, Spark SQL's highly specialized, column-based, off-heap data encoder
//    off the heap, manually managed by Tungsten, avoid garbage collection

//  Limitations
//  Untyped
//    listingsDF.filter($"state" === "CA")
//      org.apache.spark.sql.AnalysisException
//      cannot resolve 'state' given input columns: [street, zip, price];;
//      compiles, but runtime exception
//  Limited Data Types
//    e.g. complicated regular Scala class
//  Requires Semi-Structured/Structured Data
//    unstructured data; better to use RDDs

//----------
//  DataSets
//----------
/*
case class Listing(street: String, zip: Int, price: Int)
val listingsDF = ...//  DataFrame of Listings
import org.apache.spark.sql.functions._
val averagePricesDF = listingsDF.groupBy($"zip")
                                .avg("price")
val averagePrices = averagePricesDF.collect
//  averagePrices: Array[org.apache.spark.sql.Row]
val averagePricesAgain = averagePrices.map {
  row => (row(0).asInstanceOf[String], row(1).asInstanceOf[Int])
}
//  java.lang.ClassCastException
vaeragePrices.head.schema.printTreeString()
//  root
//  |-- zip: integer (nullable = true)
//  |-- avg(price): double (nullable = true)
val averagePricesAgain = averagePrices.map {
  row => (row(0).asInstanceOf[String], row(1).asInstanceOf[Double])
}
//  mostExpensiveAgain: Array[(Int, Double)]
//  works, however error prone
*/

//  type DataFrame = DataSet[Row]
//  DataSet = a compromise between RDDs & DataFrames
//    typed distributed collections of data
//    API unifies the DataFrame and RDD APIs
//    requires structured/semi-structured data
/*
listingsDS = Dataset[Listing]
listingsDS.groupByKey(l => l.zip)         //  like groupByKey on RDD
          .agg(avg($"price").as[Double])  //  like DataFrame operations
*/
//  more typed operations
//  can use higher order functions like map flatMap filter

//  Creating Datasets
/*
//  from a DataFrame
//  1.
import spark.implicits._
myDF.toDS
//  2.
val myDS = spark.read.json("people.json").as[Person]
//  3. from an RDD
import spark.implicits._
myRDD.toDS
//  4. from common Scala types
import spark.implicits._
List("yay", "ohnoes", "hooray!").toDS
*/
//  use TypedColumn instead of Column from DataFrame

//  Transformations on Datasets
//  untyped transformations
//  typed transformations
/*
val keyValuesDF =
  List((3, "Me"), (1, "Thi"), (2, "Se"), (3, "ssa"), (3, "-)"), (2, "cre"), (2, "t")).toDF
val res = keyValuesDF.map(row => row(0).asInstanceOf[Int] + 1)
*/
//  Common typed transformations
//    map[U](f: T => U): Dataset[U]
//    flatMap[U](f: T => TraversalbeOnce[U]): Dataset[U]
//    filter(pred: T => Boolean): Dataset[U]
//    distinct(): Dataset[U]
//    groupByKey[K](f: T => K): KeyValueGroupedDataset[K, T]
//      contains a number of aggregation operations which return Datasets
//      How to group & aggregate on Datasets?
//        Call groupByKey on Dataset, get back a KeyValueGroupedDataset
//        Use an aggregation operation on KeyValueGroupedDataset (return Datasets)
//    coalesce(numPartitions: Int): Dataset[T]
//    repartition(numPartitions: Int): Dataset[T]
//    reduceGroups(f: (V, V) => V): Dataset[(K, V)]
//    agg[U](col: TypedColumn[V, U]): Dataset[(K, U)]
//      someDS.agg(avg($"column"))  //  error
//      someDS.agg(avg($"column").as[Double])
//    mapGroups[U](f: (K, Iterator[V]) => U): Dataset[U]
//    flatMapGroups[U](f: (K, Iterator[V]) => TraversableOnce[U]): Dataset[U]
//    does NOT have reduceByKey
//      val keyValues =
//        List((3, "Me"), (1, "Thi"), (2, "Se"), (3, "ssa"), (3, "-)"), (2, "cre"), (2, "t"))
//      keyValuesDS = keyValues.toDS
//      1.
//      keyValuesDS.groupByKey(p => p._1)
//                 .mapGroups((k, vs) => (k, vs.foldLeft("")((acc, p) => acc + p._2)))
//                  mapGroups does not support partial aggregation, so shuffles all the data
//      2.
//      keyValuesDS.groupByKey(p => p._1)
//                 .mapValues(p => p._2)
//                 .reduceGroups((acc, str) => acc + str) //  with Aggregator

//  Aggregator
//  class Aggregator[-IN, BUF, OUT]
//  val myAgg = new Aggregator[IN, BUF, OUT]  {
//    def zero: BUF = ...                   //  the initial value
//    def reduce(b: BUF, a: IN): BUF = ...  //  Add an element to the running total
//    def merge(b1: BUF, b2: BUF): BUF = ...//  Merge intermediate values
//    def finish(r: BUF): OUT = ...         //  Return the final result
//  }.toColumn
//  val keyValues =
//    List((3, "Me"), (1, "Thi"), (2, "Se"), (3, "ssa"), (3, "-)"), (2, "cre"), (2, "t"))
//  val keyValuesDS = keyValues.toDS
//  val strConcat = new Aggregator[(Int, String), String, String] {
//    def zero: String = ""
//    def reduce(b: String, a: (Int, String)): String = b + a._2
//    def merge(b1: String, b2: String): String = b1 + b2
//    def finish(r: String): String = r
//  }.toColumn
//  keyValuesDS.groupByKey(pair => pair._1)
//             .agg(strConcat.as[String])
//  error, need Encoder

//  Encoders
//  convert data between JVM objects and Spark SQL's specialized internal (tabular) representation
//  required by all Datasets
//  Automatically
//    import spark.implicits._
//  Explicitly
//    org.apache.spark.sql.Encoders
//    Example
//      Encoders.scalaInt //  Encoder[Int]
//      Encoders.STRING //  Encoder[String]
//      Encoders.product[Person]  //  Encoder[Person], Person extends Product/is a case class
//  val strConcat = new Aggregator[(Int, String), String, String] {
//    def zero: String = ""
//    def reduce(b: String, a: (Int, String)): String = b + a._2
//    def merge(b1: String, b2: String): String = b1 + b2
//    def finish(r: String): String = r
//    override def bufferEncoder: Encoder[String] = Encoders.STRING
//    override def outputEncoder: Encoder[String] = Encoders.STRING
//  }.toColumn
//  keyValuesDS.groupByKey(pair => pair._1)
//             .agg(strConcat.as[String])
//  OK

//  Common Dataset Actions
//    collect(): Array[T]
//    count(): Long
//    first(): T/head(): T
//    foreach(f: T => Unit): Unit
//    reduce(f: (T, T) => T): T
//    show(): Unit
//    take(n: Int): Array[T]

//  When to USE?
//  Dataset
//    structured/semi-structured data
//    typesafety
//    work with functional API
//    good performance, but not the best
//  DataFrame
//    structured/semi-structured data
//    best possible performance, automatically optimized
//  RDD
//    unstructured data
//    fine-tune and manage low-level details of RDD computations
//    complex data types that cannot be serialized with Encoders

//  Limitations of Datasets
//  Catalyst can't optimized all operations
//    Relational filter operation e.g. ds.filter($"city".as[String] === "Boston")
//      can optimize
//    Functional filter operation e.g. ds.filter(p => p.city === "Boston")
//      cannot optimize

//  Limited Data Types
//    data cannot be expressed by case class/Product and standard Spark SQL data type
//      Tungsten cannot optimize
//    requires semi-structured/stuructured data