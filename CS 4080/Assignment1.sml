val lst = [1, 2, 3, 4, 5];
val palindrome = [1, 2, 3, 2, 1];
val palindromeStr = ["r", "a", "c", "e", "c", "a", "r"];
val dup = [1,1,2,3,3,2,4,4];

(* Problem 1 *)
fun find_last_helper([], last) = last
|   find_last_helper([x], _) = x
|   find_last_helper(_::rest, last) = find_last_helper(rest, last);

fun find_last(lst: 'a list) =
    case lst of
        [] => raise Empty
        | x::xs => find_last_helper(xs, x);

(* Problem 2 *)
fun element_at(lst: 'a list,i: int) =
    case (lst,i) of
        ([],_) => raise Empty
    | (head::tail,1) => head
    | (_::tail,i) => element_at(tail, i-1)

(* Problem 3 *)
fun size([]:'a list): int = 0
|   size(_::tail): int = 1 + size(tail);

(* Problem 4 *)
fun reverse ([]) = [] 
  | reverse(head::tail) = (reverse(tail)) @ [head];

fun is_palindrome(lst) =
    let
        val rev = reverse lst
    in
        lst = rev
    end;

(* Problem 5 *)
fun no_dup([]) = []
        |no_dup [x] = [x]
        |no_dup (x::y::tail) = if x = y then no_dup(y::tail)
                        else x:: no_dup(y::tail);

(* Testing *)
val a1 = find_last(lst); (* Should return 5 *)
val a2 = element_at(lst,3);(* Should return 3 *)
val a3 = size(lst); (* Should return 5 *)
val a4 = is_palindrome(lst); (* Should return False *)
val a4_2 = is_palindrome(palindrome); (* Should return True *)
val a4_3 = is_palindrome(palindromeStr); (* Should return True *)
val a5 = no_dup(dup); (* Should return [1,2,3,2,4] *)
