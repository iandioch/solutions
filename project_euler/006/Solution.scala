object Solution{
	def main(args: Array[String]) = {
		var n = 100
		var sumOfSquares = 0
		var squareOfSums = 0
		for(i <- 1 to n) {
			sumOfSquares += i*i
			squareOfSums += i
		}
		squareOfSums *= squareOfSums
		println(squareOfSums - sumOfSquares)
	}
}
