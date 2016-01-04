(princ
	(map 'string
		#'(lambda (x) (if (char= x #\A) #\T (if (char= x #\G) #\C (if (char= x #\C) #\G #\A))))
		(reverse
			(string (read)))))