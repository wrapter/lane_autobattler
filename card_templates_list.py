from card_template import CardTemplate


CARD_TEMPLATES = {
    'Combustion Man': CardTemplate(
        name='Combustion Man',
        abilities=['Attacker', ('OnRevealBonusAttack', 1), 'InvincibilityWhileAttacking'],
        cost=1,
        attack=1,
        health=1,
        creature_types=['Fire'],
    ),
    'Dai Li Agent': CardTemplate(
        name='Dai Li Agent',
        abilities=['OnRevealShackle'],
        cost=1,
        attack=2,
        health=2,
        creature_types=['Earth'],
    ),
    'Katara': CardTemplate(
        name='Katara',
        abilities=['Defender', 'StartOfTurnFullHeal'],
        cost=3,
        attack=2,
        health=5,
        creature_types=['Water'],
    ),
    'Korra': CardTemplate(
        name='Korra',
        abilities=['Attacker', ('OnSurviveDamagePump', 1, 1)],
        cost=5,
        attack=6,
        health=9,
        creature_types=['Avatar'],
    ),
    'Meelo': CardTemplate(
        name='Meelo',
        abilities=[],
        cost=1,
        attack=3,
        health=2,
        creature_types=['Air'],
    ),
    'Pabu': CardTemplate(
        name='Pabu',
        abilities=['DoubleTowerDamage'],
        cost=1,
        attack=2,
        health=1,
        creature_types=['Fire'],
    ),
    'Tonraq': CardTemplate(
        name='Tonraq',
        abilities=['Defender'],
        cost=1,
        attack=1,
        health=5,
        creature_types=['Water'],
    ),
    'Zaheer': CardTemplate(
        name='Zaheer',
        abilities=['Attacker', 'Deathtouch'],
        cost=4,
        attack=1,
        health=6,
        creature_types=['Air'],
    ),
    'Ikki': CardTemplate(
        name='Ikki',
        abilities=[],
        cost=1,
        attack=2,
        health=6,
        creature_types=['Air'],
    ),
    'Riley': CardTemplate(
        name='Riley',
        abilities=['Attacker', ('OnRevealPumpFriends', 1, 1)],
        cost=2,
        attack=1,
        health=2,
        creature_types=['Earth'],
    ),
    'Visola': CardTemplate(
        name='Visola',
        abilities=[],
        cost=2,
        attack=3,
        health=7,
        creature_types=['Water'],
    ),
    'Southern Raider': CardTemplate(
        name='Southern Raider',
        abilities=[],
        cost=2,
        attack=4,
        health=3,
        creature_types=['Fire'],
    ),
    'Hakoda': CardTemplate(
        name='Hakoda',
        abilities=['Attacker'],
        cost=2,
        attack=2,
        health=6,
        creature_types=['Water'],
    ),
    'Yon Rha': CardTemplate(
        name='Yon Rha',
        abilities=[('OnTowerAttackDealMassDamage', 2)],
        cost=4,
        attack=4,
        health=4,
        creature_types=['Fire'],
    ),
    'Sokka': CardTemplate(
        name='Sokka',
        abilities=['Attacker', 'StartOfTurnFullHeal'],
        cost=3,
        attack=3,
        health=5,
        creature_types=['Water'],
    ),
    'Zuko': CardTemplate(
        name='Zuko',
        abilities=['DoubleTowerDamage'],
        cost=3,
        attack=3,
        health=3,
        creature_types=['Fire'],
    ),
    'Naga': CardTemplate(
        name='Naga',
        abilities=[],
        cost=3,
        attack=4,
        health=8,
        creature_types=['Water'],
    ),
    'Admiral Zhao': CardTemplate(
        name='Admiral Zhao',
        abilities=['Attacker', ('OnRevealPumpAttackers', 2, 2)],
        cost=4,
        attack=2,
        health=3,
        creature_types=['Fire'],
    ),
    'Iroh II': CardTemplate(
        name='Iroh II',
        abilities=[('PumpCharactersPlayedHere', 1, 0)],
        cost=1,
        attack=0,
        health=2,
        creature_types=['Fire'],
    ),
    'Great Sage': CardTemplate(
        name='Great Sage',
        abilities=['OnTowerAttackDrawCard'],
        cost=4,
        attack=4,
        health=2,
        creature_types=['Fire'],
        not_in_card_pool=True,
    ),
    'Professor Zei': CardTemplate(
        name='Professor Zei',
        abilities=['OnTowerAttackDrawCard'],
        cost=4,
        attack=5,
        health=2,
        creature_types=['Earth'],
    ),
    'Lin': CardTemplate(
        name='Lin',
        abilities=['OnRevealShackle', 'ShacklesLastExtraTurn'],
        cost=4,
        attack=4,
        health=6,
        creature_types=['Earth'],
    ),
    'Prince Wu': CardTemplate(
        name='Prince Wu',
        abilities=[('OnRevealGainMana', 1)],
        cost=2,
        attack=3,
        health=3,
        creature_types=['Earth'],
    ),
    'Suyin': CardTemplate(
        name='Suyin',
        abilities=['OnRevealShackleAllEnemies'],
        cost=5,
        attack=4,
        health=5,
        creature_types=['Earth'],
    ),
    'Baatar Jr': CardTemplate(
        name='Baatar Jr',
        abilities=['OnRevealShackle', ('ShacklesDealDamage', 2)],
        cost=3,
        attack=3,
        health=4,
        creature_types=['Earth'],
    ),
    'Fang': CardTemplate(
        name='Fang',
        abilities=['Attacker', ('DealMoreDamageWhenLosing', 6)],
        cost=4,
        attack=2,
        health=6,
        creature_types=['Air'],
    ),
    'Momo': CardTemplate(
        name='Momo',
        abilities=['SwitchLanesAfterAttacking'],
        cost=2,
        attack=3,
        health=1,
        creature_types=['Air'],
    ),
    'Kya': CardTemplate(
        name='Kya',
        abilities=[('HealFriendlyCharacterAndTower', 3), ('PumpOnFriendlyHeal', 1, 1)],
        cost=2,
        attack=2,
        health=6,
        creature_types=['Water'],
    ),
    'Aang': CardTemplate(
        name='Aang',
        abilities=['Attacker', 'SwitchLanesInsteadOfDying'],
        cost=4,
        attack=4,
        health=2,
        creature_types=['Avatar'],
    ),
    'Tenzin': CardTemplate(
        name='Tenzin',
        abilities=[('CharacterMovesHerePumps', 2, 2)],
        cost=4,
        attack=5,
        health=5,
        creature_types=['Air'],
    ),
    'Gran Gran Kanna': CardTemplate(
        name='Gran Gran Kanna',
        abilities=[('OnRevealHealAllFriendliesAndTowers', 5)],
        cost=4,
        attack=3,
        health=3,
        creature_types=['Water'],
    ),
    'Fire Lord Ozai': CardTemplate(
        name='Fire Lord Ozai',
        abilities=['Attacker', ('OnRevealBonusAttack', 1)],
        cost=5,
        attack=5,
        health=10,
        creature_types=['Fire'],
    ),
    'Ming Hua': CardTemplate(
        name='Ming Hua',
        abilities=['OnRevealLaneFightsFirst'],
        cost=3,
        attack=5,
        health=3,
        creature_types=['Water'],
    ),
    'Master Pakku': CardTemplate(
        name='Master Pakku',
        abilities=['Defender'],
        cost=5,
        attack=3,
        health=11,
        creature_types=['Water'],
    ),
    'Jinora': CardTemplate(
        name='Jinora',
        abilities=['Attacker', 'SwitchLanesAfterAttacking'],
        cost=3,
        attack=2,
        health=6,
        creature_types=['Air'],
    ),
    'Mother Kya': CardTemplate(
        name='Mother Kya',
        abilities=[('PumpOnFriendlyHeal', 3, 3)],
        cost=2,
        attack=2,
        health=5,
        creature_types=['Water'],
    ),
    'Air Nomads': CardTemplate(
        name='Air Nomads',
        abilities=[],
        cost=3,
        attack=4,
        health=4,
        creature_types=['Air'],
        not_in_card_pool=True,
    ),
    'Taqukaq': CardTemplate(
        name='Taqukaq',
        abilities=['Defender', ('OnKillBuffHealth', 1, 2)],
        cost=4,
        attack=2,
        health=7,
        creature_types=['Water'],
    ),
    'Tarrloq': CardTemplate(
        name='Tarrloq',
        abilities=['Defender'],
        cost=2,
        attack=1,
        health=9,
        creature_types=['Water'],
    ),
    'Appa': CardTemplate(
        name='Appa',
        abilities=['OnRevealFriendliesSwitchLanes'],
        cost=3,
        attack=4,
        health=4,
        creature_types=['Air'],
    ),
    'Monk Gyatso': CardTemplate(
        name='Monk Gyatso',
        abilities=[('CharacterMovesHereThatCharacterPumps', 1, 1)],
        cost=1,
        attack=2,
        health=2,
        creature_types=['Air'],
    ),
    'Toph': CardTemplate(
        name='Toph',
        abilities=['Attacker', ('OnRevealDamageToAll', 1)],
        cost=3,
        attack=3,
        health=5,
        creature_types=['Earth'],
    ),
    'Hama': CardTemplate(
        name='Hama',
        abilities=['EndOfTurnFullHealForAllFriendlies', ('OnFriendlyHealPumpMyself', 1, 1)],
        cost=3,
        attack=2,
        health=6,
        creature_types=['Water'],
    ),
    'Hiroshi': CardTemplate(
        name='Hiroshi',
        abilities=['Defender', ('OnRevealDrawCards', 1)],
        cost=1,
        attack=1,
        health=1,
        creature_types=['Earth'],
    ),
    'Hong Mushi': CardTemplate(
        name='Hong Mushi',
        abilities=[('OnRevealDamageSelf', 4)],
        cost=1,
        attack=3,
        health=5,
        creature_types=['Fire'],
    ),
    'Sozin': CardTemplate(
        name='Sozin',
        abilities=[('PumpCharactersPlayedHere', 2, 0)],
        cost=3,
        attack=1,
        health=2,
        creature_types=['Fire'],
    ),
    'Kuvira': CardTemplate(
        name='Kuvira',
        abilities=['Attacker', ('OnRevealDamageToAll', 2)],
        cost=5,
        attack=4,
        health=10,
        creature_types=['Earth'],
    ),
    'The Big Bad Hippo': CardTemplate(
        name='The Big Bad Hippo',
        abilities=['Defender', ('OnRevealDrawCards', 2)],
        cost=3,
        attack=2,
        health=3,
        creature_types=['Earth'],
    ),
    'The Boulder': CardTemplate(
        name='The Boulder',
        abilities=['Defender', ('OnRevealDrawCards', 3)],
        cost=5,
        attack=3,
        health=5,
        creature_types=['Earth'],
    ),
    'La': CardTemplate(
        name='La',
        abilities=[('OnDrawCardPump', 2, 0)],
        cost=2,
        attack=1,
        health=3,
        creature_types=['Water'],
    ),
    'Moon Spirit Yang': CardTemplate(
        name='Moon Spirit Yang',
        abilities=['Attacker', ('OnDrawCardPump', 3, 3)],
        cost=4,
        attack=2,
        health=2,
        creature_types=['Water'],
    ),
    'Izumi': CardTemplate(
        name='Izumi',
        abilities=[('OnDamageTowerPumpTeam', 1, 0)],
        cost=2,
        attack=2,
        health=2,
        creature_types=['Fire'],
    ),
    'Kai': CardTemplate(
        name='Kai',
        abilities=[('OnTowerDamageGainMana', 1)],
        cost=2,
        attack=1,
        health=3,
        creature_types=['Air'],
    ),
}
