% Simple facts.

number(pikachu, 25).
evolves(pikachu, raichu).
evolves(charmander, charmeleon).
evolves(charmeleon, charizard).
evolves(eevee, jolteon).
evolves(eevee, flareon).
evolves(eevee, vaporeon).
evolves(pikachu,raichu,item(thunderStone)).
evolves(eevee, jolteon, item(thunderStone)).
evolves(eevee, vaporeon, item(waterStone)).
evolves(eevee, flareon, item(fireStone)).
evolves(charmander,charmeleon,level(16)).
evolves(charmeleon,charizard,level(36)).


%Effective Types

%electric
effective(electric, water).
ineffective(electric, grass).
ineffective(electric, electric).
immune(electric, ground).

%water
effective(water, fire).
effective(water, ground).
ineffective(water, water).
ineffective(water, grass).

%fire
effective(fire, grass).
ineffective(fire, water).
ineffective(fire, fire).

%grass
effective(grass, water).
effective(grass, ground).
ineffective(grass, fire).
ineffective(grass, grass).

%ground
effective(ground, electric).
effective(ground, fire).
ineffective(ground, grass).





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

%Damage Multiplier

damageMultiplier(MoveType, TargetType, 2.0) :- effective(MoveType, TargetType).
damageMultiplier(MoveType, TargetType, 0.5) :- ineffective(MoveType, TargetType).
damageMultiplier(MoveType, TargetType, 0.0) :- immune(MoveType, TargetType).
damageMultiplier(MoveType, TargetType, 1.0) :- not(effective(MoveType,TargetType)), not(ineffective(MoveType,TargetType)), not(immune(MoveType,TargetType)).








%evolves(pikachu, Who);
%sibling(jolteon, Y);
%canUseItem(pikachu, tm(X));
%descendent(charizard, Z).