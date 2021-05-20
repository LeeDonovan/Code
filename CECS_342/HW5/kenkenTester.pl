:- use_module(library(clpfd)).


% sum and product
sum_list([],0).
sum_list([H|T], S) :- sum_list(T,D), S is D + H.

product_list([],0).
product_list([H],H).
product_list([H|T], S) :- product_list(T,D), S is D * H.

adds_to(X,Y,Z):- Z #= Y + X.
mults_to(X,Y,Z):- Z #= Y * X.
subs_to(X,Y,Z):- Z #= Y - X.
divs_to(X,Y,Z):- Z #= Y//X.
%get cells

get_cell(S,[I,J],Val) :- 
    nth0(I,S,Elem),
    nth0(J,Elem,Return),
    Val #= Return.

%create cage

cage([],[],[]).

%create cell values
cell_values(Cells, S, Values) :- 
    maplist(get_cell(S), Cells, Values).

check_constraint(S, cage(add, Value, Cells)):-
    cell_values(Cells, S, Values),
    foldl(adds_to, Values, 0, Result),
    Value #= Result.

check_constraint(S, cage(mult, Value, Cells)):-
    cell_values(Cells, S, Values),
    foldl(mults_to, Values, 1, Result),
    Value #= Result.

check_constraint(S, cage(sub, Value, Cells)) :-
    cell_values(Cells, S, Values),
    nth0(0, Values, A),
    nth0(1, Values, B),
    subs_to(A, B, RetVal_1),
    subs_to(B, A, RetVal_2),
    (Value #= RetVal_1 ; Value #= RetVal_2).

check_constraint(S, cage(id, Value, Cells)) :-
    cell_values(Cells, S, Values),
    nth0(0, Values, A),
    Value #= A.

check_cages(S, Cages):- 
    maplist(check_constraint(S),Cages).