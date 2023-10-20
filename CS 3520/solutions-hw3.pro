% Base case if X is first item
is_member(X,[X|_]). 
% If X is still in the tail, run again with tail
is_member(X,[_|T]) :- is_member(X,T). 

% Base case if L1 is empty
is_subset([],_).
% If first element of both lists are same then call again with tail of both
is_subset([X|L1],[X|L2]) :- is_subset(L1,L2). 

%Base Cases if 1 or more lists are empty
is_union([], [], []).
is_union([],L2,L2).
is_union(L1,[],L1).
%Recursive Case if Head of L1 is in L2, recur with tail and move on
is_union([H|T],L2,LR) :- is_member(H,L2), is_union(T,L2,LR).
%Recursive Case if head isn't in L2, recur with tail but add head to LR
is_union([H|T],L2,[H|LR]) :- \+ is_member(H,L2), is_union(T,L2,LR).


%Base Cases if either lists are empty
is_intersect([],_,[]).
is_intersect(_,[],[]).
%Recursive Case if head of L1 is in L2, 
is_intersect([H|T],L2,[H|LR]) :- is_member(H,L2), is_intersect(T,L2,LR).
%Recursive case if head isn't in L2
is_intersect([H|T],L2,LR) :- \+ is_member(H,L2), is_intersect(T,L2,LR).

%Base case, subset of an empty list is an empty list
is_power_helper([],[]).
%When first element is in subset
is_power_helper([H|T],[H|T1]) :- is_power_helper(T,T1).
%When first element is not in subset yet
is_power_helper([_|T],LR) :- is_power_helper(T,LR).
%Function caller combining subsets
is_power(X,R):-setof(Y,is_power_helper(X,Y),R).


%Base case, empty list means its sorted
quicksort([],[]).
%Recursive case, non-empty list means not yet sorted
quicksort([H|T], Sorted) :-
    partition(T, H, Left, Right), %Partitions into two different portions where the head is the pivot
    quicksort(Left, LeftL), %Recur on left side
    quicksort(Right, RightL), %Recur on Right side
    append(LeftL, [H|RightL], Sorted). %Append the results together

%Base case if there is no list to partition
partition([],_,[],[]).
%Partition Left portion if value is less than pivot
partition([H|T],Pivot,[H|LeftL],RightL) :-
  H < Pivot, partition(T,Pivot,LeftL,RightL).
%Partition Right portion if value is greater or equal to pivot
partition([H|T],Pivot,LeftL,[H|RightL]) :-
  H >= Pivot, partition(T,Pivot,LeftL,RightL).


% Base case for empty or 1 item list is already sorted
mergesort([],[]).
mergesort([X],[X]).
% Recursive case splitting original list into two halves
% and recursively calling function on both halves then merging them back
mergesort(L, LR):-
    split(L,Left, Right),
    mergesort(Left,LeftR),
    mergesort(Right,RightR),
    merge(LeftR,RightR,LR).

% Base case for empty or 1 item list is left
split([],[],[]).
split([X],[X],[]).
%Split orignal list 1 by 1 into two halves
%First element into left list and second element to right list
split([X,Y|L],[X|Left],[Y|Right]):- split(L,Left,Right).

%Base cases if one of the list is empty
merge([], Right, Right).
merge(Left, [], Left).
%Merge left first element if smaller into result list
%then recur again without that first element
merge([X|Left],[Y|Right],[X|LR]):-
    X<Y, merge(Left,[Y|Right],LR).
%Merge right first element if smaller into result list
merge([X|Left],[Y|Right],[Y|LR]):-
    X>=Y, merge([X|Left],Right,LR).

% Function caller that checks sum of divisors are
% equal to the other number
are_amicable(X,Y):- sum_divisors(X,XR),sum_divisors(Y,YR),
    				X \= Y, XR =:= Y, YR =:= X.
% Base case when N is reduced all the way to 1
sum_divisors(1,1):-!.
% Calls helper
sum_divisors(N,R):- N>1, 
    			sum_divisors_helper(N,N-1,0,R).
% Base Case when no more divisors left
sum_divisors_helper(_,0,R,R).
%Recursive case when M(current divisor) > 0
sum_divisors_helper(N,M,Acc,R) :-
    			M > 0, 
    			0 is N rem M, %Find Proper divisor
    			Acc1 is Acc + M, %Add to accumulator
    			M1 is M-1, %Check next number in divisor
    			sum_divisors_helper(N,M1,Acc1,R).
sum_divisors_helper(N,M,Acc,R) :-
    			M > 0, 
    			\+ 0 is N rem M,%If not proper divisor
    			M1 is M-1, %Move on to next possible divisor
    			sum_divisors_helper(N,M1,Acc,R).

    			