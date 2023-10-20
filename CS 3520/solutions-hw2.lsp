;Problem 1
(defun palindromep (lst) 
    (equal lst (reverse lst)))

;Problem 2
(defun occr-helper (lst elems num result)
    (if (null elems)
        (nreverse result)
        (occr-helper lst (cdr elems) (car (cdr elems)) (cons (cons num (count num lst)) result))
    )
)
(defun occr (lst)
    (occr-helper lst (sort (remove-duplicates lst) #'<) (car (sort (remove-duplicates lst) #'<)) '())
)

;Problem 3
(defun nodups (lst)
    (if (null lst)
        nil
        (if (equal (first lst) (second lst))
            (nodups (cdr lst))
            (cons (car lst) (nodups (cdr lst)))
        )
    )
)

;Problem 4
(defun factorsL-helper (lst itr num result temp)
    (if (null lst)
        result
        (if (= num 1)
            (factorsL-helper (cdr lst) 2 (car (cdr lst)) (nconc result (list (sort temp #'<))) '())
            (if (= (mod num itr) 0)
                (factorsL-helper lst 2 (/ num itr) result (adjoin itr temp))
                (factorsL-helper lst (+ itr 1) num result temp)
            )
        )
    )
)
(defun factorsL (lst)
    (factorsL-helper lst 2 (car lst) '() '())
)

;Problem 5
(defun dups-helper (elem count)
    (if (equal count 0)
        nil
        (cons elem (dups-helper elem (- count 1)))
    )
)
(defun dups (lst count)
    (if (null lst)
        nil
        (append (dups-helper (car lst) count) (dups (cdr lst) count))
    )
)