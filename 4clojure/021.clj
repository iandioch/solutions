(fn ans [coll index]
    (if (= index 0)
    (first coll)
    (ans (next coll) (- index 1))))
