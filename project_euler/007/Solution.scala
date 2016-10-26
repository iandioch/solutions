import scala.collection.mutable

object Solution{

	def sieve(n: Int): Int = {
		var isComposite = new Array[Boolean](n)
		var count = 0
		for(i <- 2 to (n - 1)) {
			if(!isComposite(i)){
				count += 1
				if(count == 10001) {
					return i
				}
				for(j <- (i+i) to (n-1) if j % i == 0) {
					isComposite(j) = true
				}
			}
		}
		return -1
	}
	def main(args: Array[String]): Unit = {
		var n = 
		println(sieve(110000))
	}
}
