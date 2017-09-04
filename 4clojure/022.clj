(fn len [coll]
  (if (= (next coll) nil)
    1
    (+ (len (next coll)) 1)))
