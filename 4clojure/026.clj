(fn fib [n]
    (cond
        (= n 1) '(1)
        (= n 2) '(1 1)
        :else (let [p (fib (- n 1))]
            (concat p
                (list (+
                    (last p)
                    (nth p (- (count p) 2))))))))
