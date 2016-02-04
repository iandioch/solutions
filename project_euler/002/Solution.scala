object Scala{
	def main(args : Array[String]){
		var a = 1
		var b = 1
		var sum = 0
		while (b < 4000000){
			var c = a + b
			if (c % 2 == 0) {
				sum += c
			}
			a = b
			b = c
		}
		println(sum)
	}
}
