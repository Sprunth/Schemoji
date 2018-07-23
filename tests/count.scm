(begin
    (define count (lambda (search L)
        (if (not (null? L)) 
            (+ (if (equal? search (car L)) 1 0) (count search (cdr L)))
            0
        )))
    (print (count (quote the) (quote (the more the merrier the bigger the better))))
)