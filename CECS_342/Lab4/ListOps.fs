//Students: Donovan Lee and Brian Tran

module ListOps

type Account =
    | Balance of int
    | Overdrawn of int
    | Empty

// For the functions described below, first give a comment that expresses the
// type of the function, then provide an implementation that matches the
// description. (Note: make sure you understand the type of the function if your
// editor provides you with the type automatically). All of the functions below
// take lists. Make sure to note when the list can be generic.
//
// The implementation *must* be recursive.
//
// Descriptions below were provided by Mr. Neal Terrell.

// count x coll
//
// count the number of values equal to x in coll.
//int -> List 'a -> int
let rec count x coll =
  if List.isEmpty coll then
    0
  elif x = coll.Head then
    1 + count x (List.tail coll)
  else
    count x (List.tail coll)


// countEvens coll
//
// count the number of even integers in coll.
//List int -> int
let rec countEvens coll = 
  match coll with
  | [] -> 0
  | head::tail -> if head % 2 = 0 then  
                    1 + countEvens tail            
                  else
                    countEvens tail

exception MyError of string
// lastElement coll
//
// return the last element in the list
//List 'a -> int 
let rec lastElement coll = 
  match coll with
  | []  -> raise (MyError("List should not return empty and needs an int to be returned."))
  | [x] -> x
  | head::tail -> lastElement tail
// maxOverdrawn coll
//
// given a list of Accounts, return the largest Overdrawn amount, or 0 if none
// are overdrawn
//List int -> int
let rec maxOverdrawn coll =
  match coll with
  | [] -> 0
  | head :: tail ->
    match head with 
      | Overdrawn amt -> if amt > maxOverdrawn tail then amt 
                         else
                          maxOverdrawn tail 
      | _ -> maxOverdrawn tail 
  