//  test
//  typically yields a binary output
val xs = List(1, 2, 3)
assert(xs.reverse == List(3, 2, 1))

//  benchmark
//  typically yields a continuous value,
//    which denotes the extent to which the program is correct
val startTime = System.nanoTime
xs.reverse
println((System.nanoTime - startTime) / 1000000)

//  Performance Factors
//    processor speed
//    number of processors
//    memory access latency and throughput (affects contention)
//      latency = delta of t
//      throughput = # kB / s
//    cache behavior
//    runtime behavior

//  Measurement Methodologies
//    multiple repetitions
//    statistical treatment - computing mean and variance
//    eliminating outliers
//    ensuring steady state (warm-up)
//    preventing anomalies (GC, JIT compilation, aggressive optimizations)

//  ScalaMeter
//    performance regression testing - comparing
//    benchmarking - measuring
/*
resolvers += "Sonatype OSS Snapshots" at
  "https://oss.sonatype.org/content/repositories/snapshots"

libraryDependencies += "com.storm-enroute" %% "scalameter-core" % "0.7"
 */
/*
import org.scalameter.api._
val time = measure {
  (0 until 1000000).toArray
}
println(s"Array initialization time: $time ms")
*/

//  JVM Warmup
/*
import org.scalameter.api._
withWarmer(new Warmer.Default) measure { (0 until 1000000).toArray }
*/
/*
val time = config(
  Key.exec.minWarmupRuns -> 20,
  Key.exec.maxWarmupRuns -> 60,
  Key.verbose -> true
) withWarmer(new Warmer.Default) measure {
  (0 until 1000000).toArray
}
*/

/*
//  ScalaMeter measures
Measurer.Default
IgnoringGC
OutlierElimination
MemoryFootprint
GarbageCollectionCycles
 */
