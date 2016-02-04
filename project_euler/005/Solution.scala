object Solution{
	def gcd(x : Int, y : Int) : Int = {
		var a = x
		var b = y
		while(b != 0){
			var tmp = b
			b = a % b
			a = tmp
		}
		return a
	}

	def main(args: Array[String]) = {
		var prod = 1
		for(i <- 2 to 19){
			prod *= i/gcd(prod, i)
		}	
		println(prod)
	}
}
