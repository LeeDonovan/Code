effective(bug, dark).
effective(bug, grass).
effective(bug, psychic).
effective(dark, psychic).
effective(dark, ghost).
effective(dragon, dragon).
effective(electric, water). % electric is effective against water
effective(electric, flying). % electric is effective against flying
effective(fairy, dark).
effective(fairy, dragon).
effective(fairy, fighting).
effective(fighting, dark). % fighting is effective against dark.
effective(fighting, ice). % fighting is effective against ice.
effective(fighting, normal). % fighting is effective against normal.
effective(fighting, rock). % fighting is effective against rock.
effective(fighting, steel). % fighting is effective against steel.
effective(fire, bug).
effective(fire, grass).
effective(fire, ice).
effective(fire, steel).
effective(flying, bug).
effective(flying, fighting).
effective(flying, grass).
effective(ghost, psychic). %ghost is effective against psychic
effective(ghost, ghost). %ghost is effective against ghosts
effective(grass, rock).
effective(grass, water).
effective(grass, ground).
effective(ground, electric). % ground is effective against electric.
effective(ground, fire ). % ground is effective against fire.
effective(ground, poison). % ground is effective against poison.
effective(ground, rock). % ground is effective against rock.
effective(ground, steel). % ground is effective against steel.
effective(ice, dragon).
effective(ice, flying).
effective(ice, grass).
effective(ice, ground).
effective(poison, fairy).
effective(poison, grass).
effective(psychic, fighting).
effective(psychic, poison).
effective(rock, bug).
effective(rock, fire).
effective(rock, flying).
effective(rock, ice).
effective(steel, fairy).
effective(steel, ice).
effective(steel, rock).
effective(water, fire).
effective(water, rock).
effective(water,ground).
immune(dragon, fairy).
immune(electric, ground). % ground is immune against electric
immune(fighting, ghost). % fighting is immune against ghost.
immune(ghost, normal). % normal is immune to ghost
immune(ground, flying). % ground does no damage to flying types.
immune(normal, ghost).
immune(poison, steel).
immune(psychic, dark).
ineffective( grass, fire).
ineffective(bug, fairy).
ineffective(bug, fighting).
ineffective(bug, fire).
ineffective(bug, flying).
ineffective(bug, ghost).
ineffective(bug, poison).
ineffective(bug, steel).
ineffective(dark, dark).
ineffective(dark, fairy).
ineffective(dark, fighting).
ineffective(dragon, steel).
ineffective(electric, dragon). % electric is ineffective against dragon
ineffective(electric, electric). % electric is ineffective against electric
ineffective(electric, grass). % electric is ineffective against grass
ineffective(fairy, fire).
ineffective(fairy, poison).
ineffective(fairy, steel).
ineffective(fighting,bug). %fighting is ineffective against bug
ineffective(fighting,fairy). %fighting is ineffective against fairy
ineffective(fighting,flying). %fighting is ineffective against flying
ineffective(fighting,poison). %fighting is ineffective against poison
ineffective(fighting,psychic). %fighting is ineffective against psychic
ineffective(fire, dragon).
ineffective(fire, fire).
ineffective(fire, rock).
ineffective(fire, water).
ineffective(flying, electric).
ineffective(flying, rock).
ineffective(flying, steel).
ineffective(ghost, dark). %ghost is ineffective against dark
ineffective(grass, bug).
ineffective(grass, dragon).
ineffective(grass, fly).
ineffective(grass, steel).
ineffective(grass, grass).
ineffective(grass, poison).
ineffective(ground, bug). % ground is ineffective against bug.
ineffective(ground, grass). % ground is ineffective against grass.
ineffective(ice, fire).
ineffective(ice, ice).
ineffective(ice, steel).
ineffective(ice, water).
ineffective(normal, rock).
ineffective(normal, steel).
ineffective(poison, ghost).
ineffective(poison, ground).
ineffective(poison, poison).
ineffective(poison, rock).
ineffective(psychic, psychic).
ineffective(psychic, steel).
ineffective(rock, fighting).
ineffective(rock, ground).
ineffective(rock, steel).
ineffective(steal, electric).
ineffective(steel, fire).
ineffective(steel, steel).
ineffective(steel, water).
ineffective(water, dragon).
ineffective(water, grass).
ineffective(water, water).

maplist(TransformFunction, Collection, MappedCollection).

foldl(CombinerFunction, Collection, StartingAccumulator, FinalAccumulator).