(begin
    (define count (lambda (item L)
        (if (not (null? L)) 
            (+ (if (equal? item (car L)) 1 0) (count item (cdr L)))
            0
        )))
    (count (quote the) (quote (the more the merrier the bigger the better)))
)