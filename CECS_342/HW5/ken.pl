:- use_module(library(clpfd)).


% sum and product not really used in this program.
sum_list([],0).
sum_list([H|T], S) :- sum_list(T,D), S is D + H.

product_list([],0).
product_list([H],H).
product_list([H|T], S) :- product_list(T,D), S is D * H.


cage([],[],[]). %atom, target value, list of cell cords


%cell values

get_cell(S,[I,J],Val) :- 
    nth0(I,S,Elem),
    nth0(J,Elem,Return),
    Val #= Return.

cell_values(Cells, S, Values) :- 
    maplist(get_cell(S), Cells, Values).

%validating cages

%
check_constraint(S, cage(id, Value, Cells)) :-
    cell_values(Cells, S, Values),
    nth0(0, Values, A),%grabs the index values
    Value #= A.%returns value itself

check_constraint(S, cage(add, Value, Cells)):-
    cell_values(Cells, S, Values),
    foldl(adds_to, Values, 0, Result),%recursively adds 
    Value #= Result.

check_constraint(S, cage(mult, Value, Cells)):-
    cell_values(Cells, S, Values),
    foldl(mults_to, Values, 1, Result),%recursively multiplies must be 1 accumulator cant be 0 else it multi by 0
    Value #= Result.
%Does the subtraction operation of the values of the cells after the conversion from the cell coordinates, uses the or operator to choose which values to return from
check_constraint(S, cage(sub, Value, Cells)) :-
    cell_values(Cells, S, Values),
    nth0(0, Values, A),
    subs_to(A, B, RetVal_1),
    nth0(1, Values, B),
    subs_to(B, A, RetVal_2),
    (Value #= RetVal_1 ; Value #= RetVal_2).


check_constraint(S, cage(div, Value, Cells)) :-
    cell_values(Cells, S, Values),
    nth0(0, Values, A),%looks for index 
    divs_to(A, B, RetVal_1), %does the div function to get value
    nth0(1, Values, B),
    divs_to(B, A, RetVal_2),
    (Value #= RetVal_1; Value #= RetVal_2). 


%check one cage to see if all the constraints are satisfied(true),
%if so, then the cage is true. Put this functor inside maplist.
check_cages(S, Cages):- 
    maplist(check_constraint(S),Cages).

%solving the game 



solve(S, Cages) :-
    % S must have 6 rows
    length(S,6), %checks for length of 6
    % Each row in S must be length 6
    transpose(S, Rows), %transposes the S matrix
    length(Rows, 6), % checks to see if Rows has length of 6
    % Each row in S must only contain values of 1 to 6
    append(S,Values),%Values is a list that will append all values of S
    Values ins 1..6, %checks if list contains values btw 1-6
    % The entries in S must satisfy the cages of the puzzle
    check_cages(S,Cages),
    % Each row in S must contain all distinct values(no dups)
    maplist(all_different,S),

    %Each column in S must contain all distinct value
    transpose(Rows,Columns), %flip rows back to columns to check 
    maplist(all_different, Columns),
    maplist(label,S).
    


%sums | products | sub | divs

adds_to(X,Y,Z):- Z #= Y + X.
mults_to(X,Y,Z):- Z #= Y * X.
subs_to(X,Y,Z):- Z #= Y - X.
divs_to(X,Y,Z):- Z #= Y//X.