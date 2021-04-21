% Simple facts.

number(pikachu, 25).
evolves(pikachu, raichu).
evolves(charmander, charmeleon).
evolves(charmeleon, charizard).
evolves(eevee, jolteon).
evolves(eevee, flareon).
evolves(eevee, vaporeon).

%Updated evolve facts.
evolves(eevee, jolteon, item(thunderStone)).
evolves(eevee, flareon, item(fireStone)).
evolves(eevee, vaporeon, item(waterStone)).
evolves(eevee, espeon, time(dayTime)).
evolves(eevee, umbreon, time(nightTime)).
evolves(charmander, charmeleon, level(16)).
evolves(charmeleon, charizard, level(36)).
evolves(pikachu, raichu, item(thunderStone)).

%type-effectiveness.
%Types: fire, water, grass, electric, and ground

%Electric
effective(electric, water).
ineffective(electric,grass).
ineffective(electric,electric).
immune(electric,ground).

%Fire
effective(fire,grass).
ineffective(fire, fire).
ineffective(fire, water).

%Water
effective(water, ground).
effective(water, fire).
ineffective(water,water).
ineffective(water, grass).

%Grass
effective(grass, ground).
effective(grass, water).
ineffective(grass, fire).
ineffective(grass, grass).

%Ground
effective(ground, fire).
effective(ground, electric).
ineffective(ground, grass).


%Damage Done
damageMultiplier(MoveType, TargetType, 2.0) :- effective(MoveType, TargetType). 
% a move does 2x damage against a target if it is effective against that target.
damageMultiplier(MoveType, TargetType, 0.5) :- ineffective(MoveType, TargetType). 
damageMultiplier(MoveType, TargetType, 0) :- immune(MoveType, TargetType). 
damageMultiplier(_, _, 1.0).





% Slightly more complex facts.

move(thunderbolt, electric, special, 90).
move(thunderpunch, electric, physical, 75).
learns(pikachu, thunderbolt, level(36)). % Pikachu learns Thunderbolt at level 36.
learns(pikachu, thunderpunch, tm(5)).


% Simple rules.

sibling(X, Y) :- evolves(Parent, X), evolves(Parent, Y), X \= Y. % the comma means "and". "\=" means "does not unify".

canUseItem(Pokemon, tm(X)) :- learns(Pokemon, _, tm(X)). % _ is "don't care", yet again.


% A rule with multiple clauses.
descendent(X, Y) :- evolves(Y, X).
descendent(X, Y) :- evolves(Y, Z), descendent(X, Z). % This one is recursive!!

%Query
% evolves(pikachu, Who);
% sibling(jolteon, Y);
% canUseItem(pikachu, tm(X));
% descendent(charizard, Z).