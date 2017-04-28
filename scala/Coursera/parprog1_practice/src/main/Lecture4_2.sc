//  https://www.coursera.org/learn/parprog1/lecture/4Yabo/parallel-two-phase-construction

//  Most data structures can be constructed in parallel using two-phase construction

//  The intermediate data structure is a data structure that
//    has an efficient combine method O(logN + logM)
//    has an efficient += method
//    can be converted to the resulting data structure in O(n/P) time

//  Array Combiner
import scala.collection.mutable.ArrayBuffer
import scala.reflect.ClassTag

class ArrayCombiner[T <: AnyRef: ClassTag](val parallelism: Int)  {
  private var numElems = 0
  private val buffers = new ArrayBuffer[ArrayBuffer[T]]
  buffers += new ArrayBuffer[T]

  def +=(x: T) = {
    buffers.last += x
    numElems += 1
    this
  }

  def result: Array[T] = {
    val array = new Array[T](numElems)
    val step = math.max(1, numElems / parallelism)
    val starts = (0 until numElems by step) :+ numElems
    val chunks = starts.zip(starts.tail)
    val tasks = for ( (from, end) <- chunks ) yield task {
      copyTo(array, from, end)
    }
    tasks.foreach(_.join())
    array
  }

  def size = numElems

  def clear() = buffers.clear()

  private def copyTo(array: Array[T], from: Int, end: Int): Unit = {
    var i = from
    var j = 0

    while ( i >= buffers(j).length )  {
      i -= buffers(j).length
    }
  }
}
xs.par.aggregate(newCombiner)(_ += _, _ combine _).result