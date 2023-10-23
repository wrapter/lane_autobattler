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
        abilities=['ShackleOnFriendlyEarth'],
        cost=1,
        attack=2,
        health=3,
        creature_types=['Earth'],
    ),
    'Katara': CardTemplate(
        name='Katara',
        abilities=['Defender', 'EndOfTurnFullHeal'],
        cost=3,
        attack=2,
        health=6,
        creature_types=['Water'],
    ),
    'Korra': CardTemplate(
        name='Korra',
        abilities=['Attacker', ('OnSurviveDamagePump', 1, 1)],
        cost=5,
        attack=6,
        health=7,
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
        abilities=['Defender', ('OnSurviveDamagePump', 0, 2)],
        cost=1,
        attack=1,
        health=4,
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
        abilities=['SwitchLanesAtEndOfTurn'],
        cost=1,
        attack=2,
        health=6,
        creature_types=['Air'],
    ),
    'Riley': CardTemplate(
        name='Riley',
        abilities=['Attacker', ('OnRevealPumpFriends', 1, 1)],
        cost=2,
        attack=2,
        health=3,
        creature_types=['Earth'],
    ),
    'Visola': CardTemplate(
        name='Visola',
        abilities=[('OnSurviveDamagePump', 1, 1)],
        cost=2,
        attack=3,
        health=7,
        creature_types=['Air'],
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
        health=7,
        creature_types=['Air'],
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
        abilities=['Attacker', 'EndOfTurnFullHeal', ('OnKillBuffHealth', 1, 1)],
        cost=3,
        attack=3,
        health=4,
        creature_types=['Water'],
    ),
    'Mai': CardTemplate(
        name='Mai',
        abilities=['DoubleTowerDamage'],
        cost=3,
        attack=3,
        health=3,
        creature_types=['Fire'],
    ),
    'Naga': CardTemplate(
        name='Naga',
        abilities=[('OnKillBuffHealth', 2, 2)],
        cost=3,
        attack=4,
        health=7,
        creature_types=['Water'],
    ),
    'Admiral Zhao': CardTemplate(
        name='Admiral Zhao',
        abilities=['Attacker', ('OnRevealPumpAttackers', 2, 2)],
        cost=4,
        attack=4,
        health=5,
        creature_types=['Fire'],
    ),
    'Iroh II': CardTemplate(
        name='Iroh II',
        abilities=[('PumpCharactersPlayedHere', 1, 0)],
        cost=1,
        attack=1,
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
        abilities=['OnRevealShackle', ('OnShacklePumpSelf', 2, 2)],
        cost=4,
        attack=3,
        health=3,
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
        abilities=[('OnRevealShackleSeveral', 2)],
        cost=5,
        attack=6,
        health=4,
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
    'Oogi': CardTemplate(
        name='Oogi',
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
        attack=4,
        health=6,
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
        attack=3,
        health=1,
        creature_types=['Avatar'],
    ),
    'Tenzin': CardTemplate(
        name='Tenzin',
        abilities=[('CharacterMovesHerePumps', 3, 3)],
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
        abilities=['Attacker', ('OnRevealPumpFriendlyCharactersOfElement', 3, 0, 'Fire')],
        cost=5,
        attack=5,
        health=8,
        creature_types=['Fire'],
    ),
    'Ming Hua': CardTemplate(
        name='Ming Hua',
        abilities=['Attacker', 'KillEnemyAttackAgain'],
        cost=4,
        attack=4,
        health=6,
        creature_types=['Water'],
    ),
    'Master Pakku': CardTemplate(
        name='Master Pakku',
        abilities=['Defender', ('OnKillBuffHealth', 1, 1)],
        cost=5,
        attack=3,
        health=10,
        creature_types=['Water'],
    ),
    'Opal': CardTemplate(
        name='Opal',
        abilities=['Attacker', 'SwitchLanesAfterAttacking'],
        cost=3,
        attack=3,
        health=7,
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
    'Bato': CardTemplate(
        name='Bato',
        abilities=['Defender', ('OnSurviveDamagePump', 1, 1)],
        cost=4,
        attack=2,
        health=7,
        creature_types=['Water'],
    ),
    'Tarrlok': CardTemplate(
        name='Tarrlok',
        abilities=['OnRevealStealEnemy'],
        cost=6,
        attack=3,
        health=3,
        creature_types=['Water'],
    ),
    'Appa': CardTemplate(
        name='Appa',
        abilities=['OnRevealFriendliesSwitchLanes'],
        cost=3,
        attack=4,
        health=5,
        creature_types=['Air'],
    ),
    'Monk Gyatso': CardTemplate(
        name='Monk Gyatso',
        abilities=[('CharacterMovesHereThatCharacterPumps', 2, 0)],
        cost=1,
        attack=2,
        health=2,
        creature_types=['Air'],
    ),
    'Ghazan': CardTemplate(
        name='Ghazan',
        abilities=['Attacker', ('OnRevealDamageToAll', 1)],
        cost=3,
        attack=3,
        health=6,
        creature_types=['Air'],
    ),
    'Elder Katara': CardTemplate(
        name='Elder Katara',
        abilities=['EndOfTurnFullHealForAllFriendlies', ('OnFriendlyHealPumpMyself', 2, 0)],
        cost=3,
        attack=2,
        health=6,
        creature_types=['Water'],
    ),
    'Hama': CardTemplate(
        name='Hama',
        abilities=['OnRevealEnemiesFight'],
        cost=3,
        attack=3,
        health=1,
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
    'Zuko': CardTemplate(
        name='Zuko',
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
        attack=3,
        health=2,
        creature_types=['Fire'],
    ),
    'Kyoshi': CardTemplate(
        name='Kyoshi',
        abilities=['Attacker', ('OnRevealDamageToAll', 2)],
        cost=5,
        attack=4,
        health=10,
        creature_types=['Avatar'],
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
        health=6,
        creature_types=['Earth'],
    ),
    'La': CardTemplate(
        name='La',
        abilities=[('OnDrawCardPump', 2, 0)],
        cost=2,
        attack=1,
        health=2,
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
        attack=3,
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
    'Roku': CardTemplate(
        name='Roku',
        abilities=['DoNotDamageEnemyCharacters'],
        cost=2,
        attack=6,
        health=8,
        creature_types=['Avatar'],
    ),
    'Kuvira': CardTemplate(
        name='Kuvira',
        abilities=['OnRevealShackle', 'OnShackleDrawCard'],
        cost=2,
        attack=2,
        health=2,
        creature_types=['Earth'],
    ),
    'Jinora': CardTemplate(
        name='Jinora',
        abilities=['OnCharacterMoveHereMakeSpirit'],
        cost=3,
        attack=3,
        health=3,
        creature_types=['Air'],
    ),
    'Spirit': CardTemplate(
        name='Spirit',
        abilities=[],
        cost=1,
        attack=4,
        health=2,
        creature_types=[],
        not_in_card_pool=True,
    ),
    'Unalaq': CardTemplate(
        name='Unalaq',
        abilities=['Attacker', ('OnRevealPumpFriendlyCharactersOfElement', 1, 3, 'Water')],
        cost=4,
        attack=3,
        health=8,
        creature_types=['Water'],
    ),
    'Bumi II': CardTemplate(
        name='Bumi II',
        abilities=[('PumpFriendlyCharactersOfElementPlayedHere', 2, 1, 'Air')],
        cost=2,
        attack=2,
        health=3,
        creature_types=['Air'],
    ),
    'Toph': CardTemplate(
        name='Toph',
        abilities=['Attacker', 'OnAttackDoubleAttack'],
        cost=3,
        attack=1,
        health=8,
        creature_types=['Earth'],
    ),
    'Uncle Iroh': CardTemplate(
        name='Uncle Iroh',
        abilities=['Defender', 'OnFriendlyCharacterDeathHealFullyAndSwitchLanes'],
        cost=4,
        attack=2,
        health=5,
        creature_types=['Fire'],
    ),
    'Yangchen': CardTemplate(
        name='Yangchen',
        abilities=['OnCharacterMoveHereShackle'],
        cost=2,
        attack=3,
        health=4,
        creature_types=['Avatar'],
    ),
    'Cabbage Man': CardTemplate(
        name='Cabbage Man',
        abilities=['Attacker', 'OnRevealFillEnemyLaneWithCabbages'],
        cost=3,
        attack=3,
        health=3,
        creature_types=['Earth'],
    ),
    'Cabbage': CardTemplate(
        name='Cabbage',
        abilities=[],
        cost=0,
        attack=0,
        health=1,
        creature_types=[],
        not_in_card_pool=True,
    ),
    'generic_1drop': CardTemplate(
        name='generic_1drop',
        abilities=[],
        cost=1,
        attack=2,
        health=2,
        creature_types=[],
        not_in_card_pool=True,
    ),
    'generic_2drop': CardTemplate(
        name='generic_2drop',
        abilities=[],
        cost=2,
        attack=3,
        health=3,
        creature_types=[],
        not_in_card_pool=True,
    ),
    'generic_3drop': CardTemplate(
        name='generic_3drop',
        abilities=['Attacker'],
        cost=3,
        attack=3,
        health=5,
        creature_types=[],
        not_in_card_pool=True,
    ),
    'generic_4drop': CardTemplate(
        name='generic_4drop',
        abilities=['Attacker'],
        cost=4,
        attack=3,
        health=7,
        creature_types=[],
        not_in_card_pool=True,
    ),
    'Elephant Rat': CardTemplate(
        name='Elephant Rat',
        abilities=[],
        cost=1,
        attack=1,
        health=1,
        creature_types=[],
        not_in_card_pool=True,
    ),
    'The Colossus': CardTemplate(
        name='The Colossus',
        abilities=['Attacker'],
        cost=8,
        attack=8,
        health=8,
        creature_types=[],
        not_in_card_pool=True,
    ),
    'The Painted Lady': CardTemplate(
        name='The Painted Lady',
        abilities=['DealDamageEqualToCurrentHealth'],
        cost=2,
        attack=1,
        health=4,
        creature_types=['Water'],
    ),
    'Azula': CardTemplate(
        name='Azula',
        abilities=['OnRevealDiscardRandomCardAndDealDamageEqualToCost'],
        cost=2,
        attack=3,
        health=4,
        creature_types=['Fire'],
    ),
    'Kuruk': CardTemplate(
        name='Kuruk',
        abilities=['Attacker', 'OnRevealAllAttackersMakeBonusAttack'],
        cost=5,
        attack=5,
        health=9,
        creature_types=['Avatar'],
    ),
    'Ty Lee': CardTemplate(
        name='Ty Lee',
        abilities=['OnRevealSilenceRandomEnemy'],
        cost=3,
        attack=4,
        health=4,
        creature_types=['Fire'],
    ),
    'Amon': CardTemplate(
        name='Amon',
        abilities=['Attacker', 'OnRevealSilenceAllCharacters'],
        cost=5,
        attack=3,
        health=7,
        creature_types=['Water'],
    ),
    'Thod': CardTemplate(
        name='Thod',
        abilities=['Attacker', 'InvincibilityWhileAttacking', 'OnDamageCharacterSilenceIt'],
        cost=3,
        attack=1,
        health=1,
        creature_types=['Earth'],
    ),
    'Senna': CardTemplate(
        name='Senna',
        abilities=['Defender', ('OnSurviveGainMana', 1)],
        cost=3,
        attack=1,
        health=7,
        creature_types=['Water'],
    ),
    'Taqukaq': CardTemplate(
        name='Taqukaq',
        abilities=['Defender', ('OnKillBuffHealth', 1, 0)],
        cost=2,
        attack=1,
        health=8,
        creature_types=['Water'],
    ),
    'Eska': CardTemplate(
        name='Eska',
        abilities=['Attacker', 'OnRevealSummonDesna'],
        cost=4,
        attack=5,
        health=2,
        creature_types=['Water'],
    ),
    'Desna': CardTemplate(
        name='Desna',
        abilities=['Defender'],
        cost=3,
        attack=2,
        health=5,
        creature_types=['Water'],
        not_in_card_pool=True,
    ),
    'Kelsang': CardTemplate(
        name='Kelsang',
        abilities=[('OnTriggerSurvivePump', 1, 0)],
        cost=1,
        attack=2,
        health=4,
        creature_types=['Air'],
    ),
    'Varrick': CardTemplate(
        name='Varrick',
        abilities=[('OnTriggerSurvivePumpSelf', 2, 2)],
        cost=2,
        attack=2,
        health=2,
        creature_types=['Water'],
    ),
    'Princess Yue': CardTemplate(
        name='Princess Yue',
        abilities=[('OnTriggerSurvivePump', 2, 3)],
        cost=3,
        attack=3,
        health=3,
        creature_types=['Water'],
    ),
    'Yagoda': CardTemplate(
        name='Yagoda',
        abilities=['OnRevealHealAndPumpSelf'],
        cost=3,
        attack=2,
        health=2,
        creature_types=['Water'],
    ),
    'Tashi': CardTemplate(
        name='Tashi',
        abilities=['Defender', 'SurviveSwitchLanes'],
        cost=4,
        attack=2,
        health=10,
        creature_types=['Air'],
    ),
    'Malu': CardTemplate(
        name='Malu',
        abilities=['Attacker', ('OnSurviveDamagePump', 1, 0)],
        cost=1,
        attack=1,
        health=6,
        creature_types=['Air'],
    ),
    'Tsemo': CardTemplate(
        name='Tsemo',
        abilities=['OnTowerAttackDrawCard', 'OnRevealDiscard'],
        cost=1,
        attack=1,
        health=1,
        creature_types=['Air'],
    ),
    'Yung': CardTemplate(
        name='Yung',
        abilities=[('HitTowerPumpSelf', 2, 2)],
        cost=2,
        attack=2,
        health=2,
        creature_types=['Air'],
    ),
    'Juicy': CardTemplate(
        name='Juicy',
        abilities=['Attacker', 'OnRevealEnemiesSwitchLanes'],
        cost=5,
        attack=3,
        health=6,
        creature_types=['Air'],
    ),
    'Otaku': CardTemplate(
        name='Otaku',
        abilities=[('OnDiscardPump', 3, 0)],
        cost=2,
        attack=3,
        health=5,
        creature_types=['Air'],
    ),
    'Ryu': CardTemplate(
        name='Ryu',
        abilities=[('HitTowerDamageAllCharacters', 1)],
        cost=4,
        attack=5,
        health=8,
        creature_types=['Air'],
    ),
    'Council of Elders': CardTemplate(
        name='Council of Elders',
        abilities=[('OnTriggerHitTowerPump', 3, 0)],
        cost=3,
        attack=4,
        health=3,
        creature_types=['Air'],
    ),
    'Lefty': CardTemplate(
        name='Lefty',
        abilities=['HitTowerOtherCharactersSwitchLanes'],
        cost=2,
        attack=4,
        health=3,
        creature_types=['Air'],
    ),
    'Huu': CardTemplate(
        name='Huu',
        abilities=[('OnTriggerKillEnemyHealAndPumpSelf', 2, 2)],
        cost=3,
        attack=4,
        health=5,
        creature_types=['Water'],
    ),
    'Master Yu': CardTemplate(
        name='Master Yu',
        abilities=['Attacker', 'InvincibilityAgainstShackled'],
        cost=3,
        attack=3,
        health=6,
        creature_types=['Earth'],
    ),
    'Joo Dee': CardTemplate(
        name='Joo Dee',
        abilities=['AttackersDontDealDamage'],
        cost=3,
        attack=4,
        health=1,
        creature_types=['Air'],
    ),
    'Teo': CardTemplate(
        name='Teo',
        abilities=['HitTowerGiveShield'],
        cost=2,
        attack=3,
        health=2,
        creature_types=['Earth'],
    ),
    'King Bumi': CardTemplate(
        name='King Bumi',
        abilities=['Attacker', ('OnRevealDiscardHandAndPump', 4, 4)],
        cost=6,
        attack=3,
        health=3,
        creature_types=['Earth'],
    ),
    'Suki': CardTemplate(
        name='Suki',
        abilities=['Defender', 'Shield', ('OnShieldBreakPumpSelf', 2, 2)],
        cost=4,
        attack=2,
        health=4,
        creature_types=['Earth'],
    ),
    'Badgermole': CardTemplate(
        name='Badgermole',
        abilities=['Shield'],
        cost=3,
        attack=4,
        health=5,
        creature_types=['Earth'],
    ),
    'Champion Ming': CardTemplate(
        name='Champion Ming',
        abilities=['EarlyFighter', 'HitTowerShackle'],
        cost=4,
        attack=5,
        health=4,
        creature_types=['Earth'],
    ),
    'Queen Hou Ting': CardTemplate(
        name='Queen Hou Ting',
        abilities=['OnTriggerHitTowerBonusAttack'],
        cost=4,
        attack=5,
        health=6,
        creature_types=['Earth'],
    ),
    'Resistance Fighter': CardTemplate(
        name='Resistance Fighter',
        abilities=['DeathtouchAgainstDefenders'],
        cost=1,
        attack=2,
        health=4,
        creature_types=['Earth'],
    ),
    'Canyon Guide': CardTemplate(
        name='Canyon Guide',
        abilities=['Shield', 'OnRevealShieldFriendlies'],
        cost=3,
        attack=3,
        health=1,
        creature_types=['Earth'],
    ),
    'Bolin': CardTemplate(
        name='Bolin',
        abilities=['HitTowerDamageAllEnemiesEqualToDamage'],
        cost=5,
        attack=3,
        health=7,
        creature_types=['Earth'],
    ),
    'Tyro': CardTemplate(
        name='Tyro',
        abilities=[('PumpOnGainShield', 2, 2)],
        cost=2,
        attack=3,
        health=3,
        creature_types=['Earth'],
    ),
}
