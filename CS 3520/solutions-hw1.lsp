(defun flip (lst)
	(if (null lst)
		nil
		(if (= (length lst) 1)
			lst
			(cons (car (cdr lst)) (cons (car lst) (flip (cdr (cdr lst)))))
			)))

(defun remove-i (i L)
	(if (null L)
		nil
		(if (= i (car l))
			(remove-i i (cdr L))
			(cons (car L) (remove-i i (cdr L)))
			))) 

(defun product-of-diff (lst)
  (let ((prod 1))
	(dotimes (i (- (length lst) 1))
		(dotimes (j (length lst))
			(when (< i j)
				(setf prod (* prod (abs (- (nth j lst) (nth i lst))))))))
		prod))
