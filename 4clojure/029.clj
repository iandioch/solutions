(fn caps [s]
    (clojure.string/join
        (filter
            #(contains? (set "ABCDEFGHIJKLMNOPQRSTUVWXYZ") %)
            s)))
