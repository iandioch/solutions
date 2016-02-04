object Solution{

	def isPal(n : Int) : Boolean = {
		var s = n.toString()
		for (i <- 0 to s.length() - 1) {
			if(s.charAt(i) != s.charAt(s.length() - i - 1)) {
				return false
			}
		}
		return true
	}

	def main(args : Array[String]) = {
		var best = 9
		for (a <- 2 to 999){
			for (b <- a to 999){
				var prod = a*b
				if (prod > best){
					best = if(isPal(prod)) prod else best
				} 
			}
		}
		println(best)
	}
}
