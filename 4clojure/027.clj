(fn pal [s]
    (cond
        (= (count s) 0) true
        (= (count s) 1) true
        :else (and
            (= (first s) (last s))
            (pal (take (- (count s) 2) (rest s))))))
