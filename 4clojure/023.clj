(fn rev [coll]
        (if (= (next coll) nil)
        (list (first coll))
        (concat
            (rev (next coll))
            (list (first coll)))))
