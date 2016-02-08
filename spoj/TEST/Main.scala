object Main extends App {
	var ok = true
	while(ok){
		val line = scala.io.StdIn.readLine()
		if (line == "42") {
			ok = false
		}else{
			println(line)
		}
	}
}