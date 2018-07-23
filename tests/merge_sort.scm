(begin
  (define merge-lists
    (lambda (l1 l2)
      (if (null? l1)
          l2
          (if (null? l2)
              l1
              (if (< (car l1) (car l2))
                  (cons (car l1) (merge-lists (cdr l1) l2))
                  (cons (car l2) (merge-lists (cdr l2) l1)))))))
  (define even-numbers
    (lambda (l)
      (if (null? l)
          (list)
          (if (null? (cdr l))
              (list)
              (cons (car (cdr l)) (even-numbers (cdr (cdr l))))))))
  (define odd-numbers
    (lambda (l)
      (if (null? l)
          (list)
          (if (null? (cdr l))
              (list (car l))
              (cons (car l) (odd-numbers (cdr (cdr l))))))))
  (define merge-sort
    (lambda (l)
      (if (null? l)
          l
          (if (null? (cdr l))
              l
              (merge-lists
                (merge-sort (odd-numbers l))
                (merge-sort (even-numbers l)))))))

  (define a (even-numbers (list 2 7 6 5 4 5 6 7 4)))
  (define b (odd-numbers (list 2 7 6 5 4 5 6 7 4)))
  (define c (merge-sort (list 3 4 5 2 3 8 9 70 34 23 12 3 45 34)))
  (print c)
)