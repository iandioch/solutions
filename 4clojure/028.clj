(fn flat [d]
    (if (sequential? d)
        (mapcat flat d)
        [d]))
