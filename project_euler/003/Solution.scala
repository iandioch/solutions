object Solution{

	def max(a : Long, b : Long) : Long = {
		return (if (a > b) a else b) 
	}

	def primeFact(n : Long) : Long = {
		var p = 2L
		while(p <= n) {
			if (n % p == 0) {
				println(p)
				return max(p, primeFact(n/p))
			}
			p += 1
		}	
		return 1	
	}

	def main(args : Array[String]){
		println(primeFact(600851475143L))	
	}
}
