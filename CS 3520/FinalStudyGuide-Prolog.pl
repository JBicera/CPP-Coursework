%Problem 1 power(5,2,Res).
%Base Case, if Y is 1 then X is just X, if Y is 0 then X is 1
power(_,0,1).
power(X,1,X).
%Recursive Case compute current result times x and decrement Y
power(X,Y, Res) :- 
    power(X,Y1,Res1), 
    Res is Res1*X, 
    Y1 is Y-1.

%Problem 2 squared(5,Res)
%Base Case if x is 0, 0^2 = 0
squared(0,0).
%Recur with X decrement and new result value
squared(X, Res) :- 
    			X>0, %Keep X positive
    			X1 is X-1, %Decrement X
    			squared(X1,Res1), 
    			Res is Res1 + X + X - 1. %n^2 = (n-1)^2 + n + n - 1

%Problem 3 orderedListPairs([(2, 1), (3, 2), (6, 1)], Ordered).
%Base Case empty list = add nothing
unorderedPair(X,Y) :- X>=Y. %Define what an unorderedPair is
orderedListPairs([],[]).
%Recursive case where (X,Y) if unordered is reordered into result
orderedListPairs([(X,Y)|Rest],[(Smaller,Bigger)|Result]):-
    unorderedPair(X,Y), %Make sure they are a pair that is out of order or skip
    %Get smaller and bigger of both
    Smaller is min(X,Y),
	Bigger is max(X,Y),
    orderedListPairs(Rest,Result).%Recur with cdr of original list and newer result list

%Problem 4 sumEvenOdd([1, 2, 3, 4], Sums).
%REMEMBER THAT VARIABLES ARE CAPITALIZED
%Base Case if list sum is 0
sumEvenOdd([],(0,0)).
%Recursive case: Add the head to either odd or even sum then recur with tail 
sumEvenOdd([H|T],(SumOdd,SumEven)):-
    H mod 2 =:= 0,
    sumEvenOdd(T,(SumOdd,SumEvenNew)),
    SumEven is SumEvenNew + H. %Remember the last line of predicate/or rule is the goal you're tryingo achieve
sumEvenOdd([H|T],(SumOdd,SumEven)):-
    H mod 2 =\= 0,
    sumEvenOdd(T,(SumOddNew,SumEven)),
    SumOdd is SumOddNew + H.

%Problem 5 pairSum([(2, 1), (3, 2), (6, 1)], Result).
%Base Case if list empty sum is 0
pairSum([],[]).
%Recursive case: Calculate sum then add to result then recur with rest of original list and result list
pairSum([(X,Y)|Rest],[Sum|Result]):-
    Sum is X+Y,
    pairSum(Rest,Result).

%Problem 6 pairPosSum([(1, 2), (3, 4), (5, 6)], Result).
%Base Case if list empty sum is 0
pairPosSum([],(0,0)).
%Recursive Case: Recursively call with SumLeftNew and SumRightNew being the tale recursive calls
pairPosSum([(X,Y)|Rest],(SumLeft,SumRight)):-
    pairPosSum(Rest,(SumLeftNew,SumRightNew)),
    SumLeft is X + SumLeftNew,
    SumRight is Y + SumRightNew.

%Problem 7 polynomial([1,0,3,7], 2)
%Base Case if list of coeffcients empty sum is 0
polynomial([],_,0).
%Recursive Case: Calculate length of list (Don't have to -1 for index because length of tail) then add result recursively
polynomial([H|T],X,Result):-
    length(T,Length),
    polynomial(T,X,Result1),
    Result is X**Length * H + Result1.

%Problem 8 removeDups([a,b,b,a,c,b,c,c,d,a,d],Result).
%Base Case: Empty list = Empty list result
removeDups([],[]).
removeDups([H|T],[H|Result]):- %Add head of list into result
    \+member(H,T), %Is not a member of resulting list yet
    removeDups(T,Result).
removeDups([H|T],Result):- %Try again
    member(H,T), %Is already in resulting list = Duplciate
    removeDups(T,Result).

%Problem 9 packConsecutiveDups([a,b,b,a,c,b,c,c,d,a,d], Result).
packConsecutiveDups([],[]).
packConsecutiveDups([X],[[X]]).%One size list(last item) put into list of itself( Nothing to compare it to)
packConsecutiveDups([X,Y|T],[[X|Acc]|Result]):-%If consecutive match pack into result
    X == Y,
    packConsecutiveDups([X|T],[Acc|Result]).
packConsecutiveDups([X,Y|T], [[X]|Result]):-%If not pack by itself
    X \== Y,
    packConsecutiveDups([Y|T],Result).

%Problem 10 packAllDups([a,b,b,a,c,b,c,c,d,a,d], Result).
packAllDups([], []). %Empty list Base case
packAllDups([X], [[X]]).%Last element put into list by itself
packAllDups([X, X | T], [[X | Acc] | Result]) :- %If matches add into accumulator then add into result
    packAllDups([X | T], [Acc | Result]).
packAllDups([X, Y | T], Result) :- %If doesn't matches add into result
    X \== Y,
    packAllDups([Y | T], Result).

%Problem 11 lengthEncoding([a,b,b,a,c,b,c,c,d,a,d], Result).
% Base case: Empty list = Result empty list
lengthEncoding([], []).
%Recursive Cases
lengthEncoding([X], [(1, X)]). %Last element can only occur once
lengthEncoding([X, X | T], [(N, X) | Result]) :-
    lengthEncoding([X | T], [(N1, X) | Result]), %Consecutive duplicates 
    N is N1 + 1.
lengthEncoding([X, Y | T], [(1, X) | Result]) :- %Not consecutive
    X \== Y, 
    lengthEncoding([Y | T], Result).

%Problem 12 lengthDecoding([(1,a),(2,b),(1,a),(1,c),(1,b),(2,c),(1,d),(1,a),(1,d)], Result).
%Base Case: Empty List
lengthDecoding([], []).
%Recursive Cases
lengthDecoding([(Size, Char)|T], [Char|Result]) :- %Add Char into result list size number of times
    Size > 0,
    Size1 is Size - 1,
    lengthDecoding([(Size1, Char)|T], Result). 
lengthDecoding([(_, Char)|T], [Char|Result]) :- %Add size 1 occurence as a sinpairListElementse character
    lengthDecoding(T, Result).

%Problem 13 sublist([1,2,3,4,5,6,7], 3, 5, Result).
%Doesn't work, dont know how to make the base case of A>B and
%The recursive case not clash
%Base Cases
sublist([], _, _, []).
sublist(_, A, B, Result) :-  %If A>B then Result is just nothing
    A > B,
    Result = []. 
%Recursive Case: Include Elements
sublist([H|T],A,B,[H|Result]) :- 
    A =< 0, 
    B >= 0, 
    A1 = A-1, 
    B1 = B-1, 
    sublist(T,A1,B1,Result).
%Skip elements
sublist([_|T],A,B,Result) :-  
    A1 = A-1, 
    B1 = B-1, 
    sublist(T,A1,B1,Result).

%Problem 14 sublistWrapped([1,2,3,4,5,6,7], 3, 5, Result).
%Base Case
sublistWrapped([],_,_,[]).
%Computer fornt and back then add together
sublistWrapped(X,A,B,TotalResult):- 
    sublistFront(X,B+1,ResultFront),
    sublistBack(X,A,ResultBack),
    append(ResultBack,ResultFront,TotalResult).
%Compute front 
sublistFront(_,0,[]).
sublistFront([H|T],A,[H|Result]) :- 
    A1 is A -1, 
    sublistFront(T,A1,Result).
%Compute Back
sublistBack([],_,[]).
sublistBack([H|T],A,[H|Result]):- 
    A =< 0, 
    A1 is A-1, 
    sublistBack(T,A1,Result).
sublistBack([_|T],A,Result):- 
    A > 0, 
    A1 is A-1, 
    sublistBack(T,A1,Result).

%Problem 15 betweenAB(2,7,Result).
betweenAB(X,X,[X]). %If equal add last number
betweenAB(A,B,[Acc|Result]) :- 
    A1 is A+1, 
    betweenAB(A1,B,Result), 
    Acc is A.
    
%Problem 16 comboK([a,b,c],2,Result)
%Function is made up of all subsets with specific length
comboK(Lst,Size,Result):- is_power(Lst,Subsets),isLength(Subsets,Size,Result).
%Generate ALl possible subsets
is_power(X,Z) :- setof(Y,list_subset(X,Y),Z).
list_subset([],[]).
list_subset([H|T],[H|S]) :- list_subset(T,S).
list_subset([_|T],S) :- list_subset(T,S).
%Filter Subsets by lenght
isLength([],_,[]).
isLength([H|T],M,[H|R]):-
    isLength(T,M,R),
    length(H,M).
isLength([_|T],M,R):- 
    isLength(T,M,R).

%Problem 17 pairListElement([3,0,5,7,5,1,2], Left,Right).
pairListElement([H|T],ResLeft,ResRight):- %Returns left list and right list greater and lesser than Head
    pairListElement-h(T,H,ResLeft1,ResRight),
    append(ResLeft1,[H],ResLeft). %Add the header element into smaller list
%Partitions List
%Base Case: List empty = Add nothing to both
pairListElement-h([],_,[],[]). 
pairListElement-h([H|T],X,[H|ResLeft],ResRight):- %Put in Result Left if smaller
    X >= H,
    pairListElement-h(T,X,ResLeft,ResRight).
pairListElement-h([H|T],X,ResLeft,[H|ResRight]):- %Put in Result Right if bigger
    X < H,
    pairListElement-h(T,X,ResLeft,ResRight).


%Problem 18
%Base Case if both empty = empty, one empty = dump into result
merge([],[],[]).
merge(L1,[],L1).
merge([],L2,L2).
%Recursive Case if Head of H1 is bigger, recur tail and all of list 2
merge([H1|T1],[H2|T2],[H1|Result]):-
    H1 =< H2,
    merge(T1,[H2|T2],Result).
%Vice versa
merge([H1|T1],[H2|T2],[H2|Result]):-
    H1 >= H2,
    merge([H1|T1],T2,Result).

%Problem 19 minMax([0,1,2,3,4],(Min, Max)).
%Base Case set values to 0
minMax([], (0,0)).
%Recursive Case get min and max compared ot head then reassign and recur with tail
minMax([H|T], (Min, Max)) :-
    minMax(T, (MinT, MaxT)),
    Min is min(H, MinT),
    Max is max(H, MaxT).

%Problem 20 removeX([a,b,c,a,d,a,e],a,Result).
%Base Case add empty list
removeX([],_,[]).
%Recursive case if X is not Head, add to Result list
removeX([H|T],X,[H|Result]):-
    H \== X,
    removeX(T,X,Result).
%Recursive case if X is head, recur again doing nothing
removeX([H|T],X,Result):-
    H == X,
    removeX(T,X,Result).








