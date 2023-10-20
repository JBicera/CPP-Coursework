;Problem 1
(defun power (x y)
	(if (= y 0)
		1
		(* x (power x (- y 1))) ;Recursively multiply x
		)
)
;Problem 2
(defun squared (x)
	(if (= x 0)
        0 ;Base case
        (+ (squared (- x 1)) x (- x 1)) ;n^2 = (n-1)^2 + n + n - 1
        )
    )
;Problem 3   Test case (increaseList '((2 . 1) (3 . 2) (6 . 1)))
(defun increaseList (lst)
    (if (null lst)
        nil
        (if (>= (car (car lst)) (cdr (car lst))) ;Access dotted pairs in list by getting the car and getting the car or cdr of that
            (cons (cons (cdr (car lst)) (car (car lst))) (increaseList (cdr lst))) ;Switch dotted pairs
            (cons (cons (car (car lst)) (cdr (car lst))) (increaseList (cdr lst))) ;Keep original pairs
            )
        )
    )
;Problem 4    Test Case (evenOddPairs '(1 2 3 4))
(defun evenOddPairs (lst)
    (evenOddPairs-h lst 0 0))
(defun evenOddPairs-h (lst resultOdd resultEven)
    (if (null lst)
        (cons resultOdd resultEven)
        (if (= (mod (car lst) 2) 0) ;If element is even
            (evenOddPairs-h (cdr lst) resultOdd (+ resultEven (car lst)))
            (evenOddPairs-h (cdr lst) (+ resultOdd (car lst)) resultEven)
        )
    )
)
;Problem 5    Test Case (dottedPairSum '((1 . 2) (3 . 4) (5 . 6)))
(defun dottedPairSum (lst)
    (if (null lst)
        nil
        (cons (+ (car (car lst)) (cdr (car lst))) (dottedPairSum (cdr lst)))
    )
)
;Problem 6 Test Case (dottedPairTotal '((1 . 2) (3 . 4) (5 . 6)))
(defun dottedPairTotal (lst)
    (dottedPairTotal-h lst 0 0))
(defun dottedPairTotal-h (lst resLeft resRight)
    (if (null lst)
        (cons resLeft resRight)
        (dottedPairTotal-h (cdr lst) (+ resLeft (car(car lst))) (+ resRight (cdr (car lst))))
    )
)
;Problem 7 Test Case (polynomial '(1 0 3 7) 2)
(defun polynomial (lst x)
    (polynomial-h lst x (- (length lst) 1)))
(defun polynomial-h (lst x size)
    (if (null lst)
        0
        (+ (* (car lst) (power x size)) (polynomial-h (cdr lst) x (- size 1))) 
        )
    )

;Problem 8 (removeDups '(a b b a c b c c d a d))
(defun removeDups (lst)
    (removeDups-h lst '()))
(defun removeDups-h (lst res)
    (if (null lst)
        (reverse res)
        (if (null (member (car lst) res)) ;member returns nil if item is in list and returns cdr at the index of the first instance of the element
            (removeDups-h (cdr lst) (cons (car lst) res)) ;If no more duplicates in list add to result
            (removeDups-h (cdr lst) res) ;If there are still duplicates recur again
        )
    )
)

;Problem 9 (packConsecutive '(a b b a c b c c d a d))
(defun packConsecutive (lst)
    (packConsecutive-h lst '() '())
)
(defun packConsecutive-h (lst current res)
    (if (null lst)
        (reverse res)
        (if (equal (car lst) (car (cdr lst))) ; Use "equal" when comparing characters instead of numbers
            (packConsecutive-h (cdr lst) (cons (car lst) current) res) ;If consecutive found add onto current list and cdr lst
            (if (null current) ;Current = The current list of matched items to add into result
                (packConsecutive-h (cdr lst) '() (cons (list (car lst)) res)) ;If mismatch found and current list empty then just add value by itself as a single item list
                (packConsecutive-h (cdr lst) '() (cons (cons (car lst) current) res )) ;If mismatch found and there is still items in list then add item with the current list into result
            )
        )
    )
)

;Problem 10 (packDups '(a b b a c b c c d a d))
(defun packDups (lst)
    (packDups-h lst (car lst) '()))
(defun packDups-h (lst element res)
    (if (null lst)
        (reverse res)
        ;Remove current element from rest of list and recur on next element of that while adding the collectDups list to the resulting list
        (packDups-h (remove element lst) (car (remove element lst)) (cons (collectDups lst element) res))
    )
)
(defun collectDups (lst element) ;Takes list and element and searches for element returning a list of the dups
    (if (null lst)
        nil
        (if (equal element (car lst))
            (cons element (collectDups (cdr lst) element))
            (collectDups (cdr lst) element)
        )
    )
)

;Problem 11 (pairLengthList '(a b b a c b c c d a d))
(defun pairLengthList (lst)
    (pairLengthList-h lst 0 '())
)
(defun pairLengthList-h (lst current res)
    (if (null lst)
        (reverse res)
        (if (equal (car lst) (car (cdr lst))) ;If consecutive match found or not
            (pairLengthList-h (cdr lst) (+ current 1) res) ;Add 1 to current element total then recur
            (pairLengthList-h (cdr lst) 0 (cons (cons (+ current 1) (car lst)) res)) ;Matching stopped so add current result + 1 to result list
        )
    )
)

;Problem 12 (decodeLength '((1 . a) (2 . b) (1 . a) (1 . c) (1 . b) (2 . c) (1 . d) (1 . a) (1 . d)))
(defun decodeLength (lst)
    (if (null lst)
        nil
        (append (getLengthSubstring (cdr (car lst)) (car (car lst))) (decodeLength (cdr lst)))
    )
)
(defun getLengthSubstring (element size)
    (if (= size 0)
        nil
        (cons element (getLengthSubstring element (- size 1)))
    )
)

;Problem 13 (sublist '(1 2 3 4 5 6 7) 3 5)
(defun sublist (lst a b)
    (if (= a (+ b 1)) ;b + 1 because index is at 0
        (cons (nth a lst) (sublist lst (+ a 1) b)) ;Add value of index a into list until you reach b
        nil
    )
)

;Problem 14 (sublistWrapped '(1 2 3 4 5 6 7) 5 3)
(defun sublistWrapped (lst a b)
    (if (> a (+ b 1)) ;b + 1 because index is at 0
        (append (endOfList lst a) (sublist lst 0 b) ) ;Add before b and after a together, utilizes function in problem 13 (sublist)
        nil
    )
)
(defun endOfList (lst index)
    (if (= index (length lst))
        nil
        (cons (nth index lst) (endOfList lst (+ index 1))) ;Returns sublist of index a until end of list
    )
)

;Problem 15 (intInBetween 2 7)
(defun intInBetween (a b)
    (if (< a (+ b 1)) ; b + 1 because index is 0
        (cons a (intInBetween (+ a 1) b))
        nil
    )
)

;Problem 16 I have the approach but I feel like this requires using 
;mapcar or lambda which I am not as familiar with
(defun comboK (k lst)
  comboK-h(k lst '()))
(defun comboK-h (k lst result)
    ;Assemble a list of all subsets
    ;Recursively add into result if size of list is k
)
(defun powerset (lst)
    (if (null lst)
        '(())
        ;Find some way to generate powerset from lst
    )
)


;Problem 17 (pairListElement '(3 1 4 2 0 5))
(defun pairListElement (lst)
    (pairListElement-h lst (car lst) '() '()))
(defun pairListElement-h (lst element resLess resMore)
    (if (null lst)
        (cons (sort resLess #'<) (list (sort resMore #'<))) ; Return both lists sorted
        (if (<= (car lst) element)
            (pairListElement-h (cdr lst) element (cons (car lst) resLess) resMore)
            (pairListElement-h (cdr lst) element resLess (cons (car lst) resMore))
        )
    )
)

;Problem 18 (mergeCustom '(0 2 4) '(1 3 5))
(defun mergeCustom (lst1 lst2)
    (merge-h lst1 lst2 '()))
;Notice you can have if blocks right after the other and can run sequentially
(defun merge-h (lst1 lst2 res)
    ;Base Cases = One of the lists are empty
    (if (and (null lst1) (not (null lst2))) ;List 1 empty and list 2 non-empty, dump in rest of lst 2 and return reverse
        (reverse (append lst2 res))
        (if (and (not (null lst1)) (null lst2)) ;List 2 is empty and list 1 non-empty, dump in rest of lst 1 and return reverse
            (reverse (append lst1 res))
            ;Recursive Case if neither list are empty = Still sorting to do
            (if (<= (car lst1) (car lst2))
                (merge-h (cdr lst1) lst2 (cons (car lst1) res))
                (merge-h lst1 (cdr lst2) (cons (car lst2) res))
            )
        )
    )
)

;Problem 19 (minMaxPair '(0 1 2 3 4 5))
(defun minMaxPair (lst)
    (cons (findMin lst (car lst)) (findMax lst (car lst))))

(defun findMin (lst min)
    (if (null lst)
        min
        (if (<= (car lst) min)
            (findMin (cdr lst) (car lst))
            (findMin (cdr lst) min)
        )
    )
)
(defun findMax (lst max)
    (if (null lst)
        max
        (if (> (car lst) max)
            (findMax (cdr lst) (car lst))
            (findMax (cdr lst) max)
        )
    )
)

;Problem 20 (removeXList '(a b c a d a e) 'a)
(defun removeXList (lst x)
    (if (null lst)
        nil
        (if (equal x (car lst))
            (removeXList (cdr lst) x)
            (cons (car lst) (removeXList (cdr lst) x))
        )
    )
)