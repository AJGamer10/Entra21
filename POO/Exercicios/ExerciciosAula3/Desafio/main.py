from pokemon import Pokemon
from attack import Attack
from battle import Battle


leaf_blade = Attack("Leaf Blade", "Grass", 20)
brick_break = Attack("Brick Break", "Fighting", 25)
return_atk = Attack("Return", "Normal", 15)
dragon_claw = Attack("Dragon Claw", "Dragon", 25)
dig = Attack("Dig", "Ground", 30)
flamethrower = Attack("Flamethrower", "Fire", 35)
crunch = Attack("Crunch", "Dark", 25)
sky_uppercut = Attack("Sky Uppercut", "Fighting", 25)
bulk_up = Attack("Bulk Up", "Fighting", 0, )


attacks_sceptile = [leaf_blade, brick_break, return_atk, dragon_claw]
sceptile = Pokemon("Sceptile", ["Grass"], 70, 85, 75, attacks_sceptile)

attacks_blaziken = [flamethrower, ]
blaziken = Pokemon("Blaziken", ["Fire", "Fighting"], 80, 95, 70, attacks_blaziken)

attacks_flygon = [dig, flamethrower, dragon_claw, crunch]
flygon = Pokemon("Flygon", ["Ground", "Dragon"], 80, 90, 80, attacks_flygon)

batalha1 = Battle(sceptile, flygon)
batalha1.turno_battle()
