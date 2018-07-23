(begin
  (define mergel
    (lambda (l1 l2)
      (if (null? l1)
          l2
          (if (null? l2)
              l1
              (if (< (car l1) (car l2))
                  (cons (car l1) (mergel (cdr l1) l2))
                  (cons (car l2) (mergel (cdr l2) l1)))))))
  (define evennumbers
    (lambda (l)
      (if (null? l)
          (list)
          (if (null? (cdr l))
              (list)
              (cons (car (cdr l)) (evennumbers (cdr (cdr l))))))))
  (define oddnumbers
    (lambda (l)
      (if (null? l)
          (list)
          (if (null? (cdr l))
              (list (car l))
              (cons (car l) (oddnumbers (cdr (cdr l))))))))
  (define mergesort
    (lambda (l)
      (if (null? l)
          l
          (if (null? (cdr l))
              l
              (mergel
                (mergesort (oddnumbers l))
                (mergesort (evennumbers l)))))))

  (define a (evennumbers (list 2 7 6 5 4 5 6 7 4)))
  (define b (oddnumbers (list 2 7 6 5 4 5 6 7 4)))
  (define c (mergesort (list 3 4 5 2 3 8 9 70 34 23 12 3 45 34)))
  (print c)
)