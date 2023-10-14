from typing import Callable, Union
from ability import Ability
from utils import element_to_color, plural


ABILITIES: dict[str, Union[Ability, Callable]] = {
    'Defender': Ability(
        name='Defender',
        description='Defender',
    ),
    'Attacker': Ability(
        name='Attacker',
        description='Attacker',
    ),
    'OnRevealShackle': Ability(
        name='OnRevealShackle',
        description='On reveal: shackle a random enemy character.',
    ),
    'OnSurviveDamagePump': lambda x, y: Ability(
        name='OnSurviveDamagePump',
        description=f'When I survive damage, I get +{x}/+{y}.',
        number=x,
        number_2=y,
    ),
    'Deathtouch': Ability(
        name='Deathtouch',
        description='I kill any character I fight with.',
    ),
    'InvincibilityWhileAttacking': Ability(
        name='InvincibilityWhileAttacking',
        description='When I attack I don\'t take damage back.',
    ),
    'DoubleTowerDamage': Ability(
        name='DoubleTowerDamage',
        description='When I attack the enemy tower, I deal double damage.',
    ),
    'EndOfTurnFullHeal': Ability(
        name='EndOfTurnFullHeal',
        description='At the end of each turn, I fully heal.',
    ),
    'OnRevealPumpFriends': lambda x, y: Ability(
        name='OnRevealPumpFriends',
        description=f'On reveal: give +{x}/+{y} to other friendly characters.',
        number=x,
        number_2=y,
    ),
    'OnTowerAttackDealMassDamage': lambda x: Ability(
        name='OnTowerAttackDealMassDamage',
        description=f'When I attack the enemy tower, I deal {x} damage to enemy characters.',
        number=x,
    ),
    'OnRevealPumpAttackers': lambda x, y: Ability(
        name='OnRevealPumpAttackers',
        description=f'On reveal: give +{x}/+{y} to other friendly attackers.',
        number=x,
        number_2=y,
    ),
    'PumpCharactersPlayedHere': lambda x, y: Ability(
        name='PumpCharactersPlayedHere',
        description=f'Other characters played here get +{x}/+{y}.',
        number=x,
        number_2=y,
    ),
    'OnTowerAttackDrawCard': Ability(
        name='OnTowerAttackDrawCard',
        description='When I attack the enemy tower, draw a random card.',
    ),
    'ShacklesLastExtraTurn': Ability(
        name='ShacklesLastExtraTurn',
        description='Shackles on enemy characters last an additional turn.',
    ),
    'OnRevealGainMana': lambda x: Ability(
        name='OnRevealGainMana',
        description=f'On reveal: gain {x} mana next turn only.',
        number=x,
    ),
    'OnRevealShackleAllEnemies': Ability(
        name='OnRevealShackleAllEnemies',
        description='On reveal: shackle the enemy characters here.',
    ),
    'ShacklesDealDamage': lambda x: Ability(
        name='ShacklesDealDamage',
        description=f'When you shackle an enemy character, deal {x} damage to it.',
        number=x,
    ),
    'DealMoreDamageWhenLosing': lambda x: Ability(
        name='DealMoreDamageWhenLosing',
        description=f'I deal {x} more damage when my team is losing my lane.',
        number=x,
    ),
    'SwitchLanesAfterAttacking': Ability(
        name='SwitchLanesAfterAttacking',
        description='After I attack, I switch lanes.',
    ),
    'HealFriendlyCharacterAndTower': lambda x: Ability(
        name='HealFriendlyCharacterAndTower',
        description=f'When I am played, heal a friendly character fully and your tower for {x}.',
        number=x,
    ),
    'SwitchLanesInsteadOfDying': Ability(
        name='SwitchLanesInsteadOfDying',
        description='When I would die, I heal fully and switch lanes instead.',
    ),
    'CharacterMovesHerePumps': lambda x, y: Ability(
        name='CharacterMovesHerePumps',
        description=f'Whenever another friendly character switches into this lane, I get +{x}/+{y}.',
        number=x,
        number_2=y,
    ),
    'OnRevealHealAllFriendliesAndTowers': lambda x: Ability(
        name='OnRevealHealAllFriendliesAndTowers',
        description=f'On reveal: fully heal friendly characters in ALL lanes and ALL friendly towers for {x}.',
        number=x,
    ),
    'OnRevealBonusAttack': lambda x: Ability(
        name='OnRevealBonusAttack',
        description=f'On reveal: I make {x} bonus attack{plural(x)}.',
        number=x,
    ),
    'OnRevealLaneFightsFirst': Ability(
        name='OnRevealLaneFightsFirst',
        description='On reveal: this lane fights first this turn.',
    ),
    'OnKillSwitchLanes': Ability(
        name='OnKillSwitchLanes',
        description='When I kill a character, I switch lanes.',
    ),
    'PumpOnFriendlyHeal': lambda x, y: Ability(
        name='PumpOnFriendlyHeal',
        description=f'Whenever another friendly character is healed, that character gets +{x}/+{y}.',
        number=x,
        number_2=y,
    ),
    'OnKillBuffHealth': lambda x, y: Ability(
        name='OnKillBuffHealth',
        description=f'When I kill a character, I get +{x}/+{y}.',
        number=x,
        number_2=y,
    ),
    'OnRevealFriendliesSwitchLanes': Ability(
        name='OnRevealFriendliesSwitchLanes',
        description='On reveal: other friendly characters here switch lanes.',
    ),
    'CharacterMovesHereThatCharacterPumps': lambda x, y: Ability(
        name='CharacterMovesHereThatCharacterPumps',
        description=f'Whenever another friendly character switches into this lane, it gets +{x}/+{y}.',
        number=x,
        number_2=y,
    ),
    'OnRevealDamageToAll': lambda x: Ability(
        name='OnRevealDamageToAll',
        description=f'On reveal: deal {x} damage to all characters here (including your own).',
        number=x,
    ),
    'EndOfTurnFullHealForAllFriendlies': Ability(
        name='EndOfTurnFullHealForAllFriendlies',
        description='At the end of each turn, fully heal other friendly characters.',
    ),
    'OnFriendlyHealPumpMyself': lambda x, y: Ability(
        name='OnFriendlyHealPumpMyself',
        description=f'Whenever another friendly character is healed, I get +{x}/+{y}.',
        number=x,
        number_2=y,
    ),
    'OnRevealDamageSelf': lambda x: Ability(
        name='OnRevealDamageSelf',
        description=f'On reveal: I deal {x} damage to myself.',
        number=x,
    ),
    'OnRevealDrawCards': lambda x: Ability(
        name='OnRevealDrawCards',
        description=f'On reveal: draw {x} random card{plural(x)}.',
        number=x,
    ),
    'OnDrawCardPump': lambda x, y: Ability(
        name='OnDrawCardPump',
        description=f'When you draw a card, I get +{x}/+{y}.',
        number=x,
        number_2=y,
    ),
    'OnDamageTowerPumpTeam': lambda x, y: Ability(
        name='OnDamageTowerPumpTeam',
        description=f'When I damage the enemy tower, other friendly characters get +{x}/+{y}.',
        number=x,
        number_2=y,
    ),
    'OnFriendlySlayPump': lambda x, y: Ability(
        name='OnFriendlySlayPump',
        description=f'Whenever another friendly character kills an enemy character, I get +{x}/+{y}.',
        number=x,
        number_2=y,
    ),
    'OnTowerDamageGainMana': lambda x: Ability(
        name='OnTowerDamageGainMana',
        description=f'When I damage the enemy tower, gain {x} mana next turn.',
        number=x,
    ),
    'DoNotDamageEnemyCharacters': Ability(
        name='DoNotDamageEnemyCharacters',
        description='I do not damage enemy characters.',
    ),
    'ShackleOnFriendlyEarth': Ability(
        name='ShackleOnFriendlyEarth',
        description='When another friendly Earth (green) character is played here, shackle a random enemy character.',
    ),
    'OnShackleDrawCard': Ability(
        name='OnShackleDrawCard',
        description='When you shackle an enemy character, draw a random card.',
    ),
    'OnRevealPumpFriendlyCharactersOfElement': lambda x, y, z: Ability(
        name='OnRevealPumpFriendlyCharactersOfElement',
        description=f'On reveal: give +{x}/+{y} to other friendly {z} ({element_to_color(z)}) characters.',
        number=x,
        number_2=y,
        creature_type=z,
    ),
    'OnCharacterMoveHereMakeSpirit': Ability(
        name='OnCharacterMoveHereMakeSpirit',
        description='Whenever another friendly character moves into this lane, make a 4/2 Spirit in another lane.',
    ),
    'PumpFriendlyCharactersOfElementPlayedHere': lambda x, y, z: Ability(
        name='PumpFriendlyCharactersOfElementPlayedHere',
        description=f'Whenever you play another {z} ({element_to_color(z)}) character in this lane, it gets +{x}/+{y}.',
        number=x,
        number_2=y,
        creature_type=z,
    ),
    'OnAttackDoubleAttack': Ability(
        name='OnAttackDoubleAttack',
        description='After I attack, double my strength.',
    ),
    'OnFriendlyCharacterDeathHealFullyAndSwitchLanes': Ability(
        name='OnFriendlyCharacterDeathHealFullyAndSwitchLanes',
        description='If a friendly character in ANY other lane would die, heal it fully and switch it to my lane instead.',
    ),
    'OnCharacterMoveHereShackle': Ability(
        name='OnCharacterMoveHereShackle',
        description='Whenever a friendly character moves into this lane, shackle a random enemy character.',
    ),
    'SwitchLanesAtEndOfTurn': Ability(
        name='SwitchLanesAtEndOfTurn',
        description='At the end of each turn, I switch lanes.',
    ),
    'OnRevealFillEnemyLaneWithCabbages': Ability(
        name='OnRevealFillEnemyLaneWithCabbages',
        description='On reveal: fill the enemy lane with 0/1 Cabbages.',
    ),
    'DealDamageEqualToCurrentHealth': Ability(
        name='DealDamageEqualToCurrentHealth',
        description='I deal damage equal to my current health.',
    ),
    'OnRevealDiscardRandomCardAndDealDamageEqualToCost': Ability(
        name='OnRevealDiscardRandomCardAndDealDamageEqualToCost',
        description='On reveal: discard a random card and deal damage to a random enemy equal to its cost.',
    ),
    'OnRevealAllAttackersMakeBonusAttack': Ability(
        name='OnRevealAllAttackersMakeBonusAttack',
        description='On reveal: your other friendly attackers in ALL lanes make a bonus attack.',
    ),
    'OnRevealSilenceRandomEnemy': Ability(
        name='OnRevealSilenceRandomEnemy',
        description='On reveal: silence a random enemy character. This can counter on reveals.',
    ),
    'OnRevealSilenceAllCharacters': Ability(
        name='OnRevealSilenceAllCharacters',
        description='On reveal: silence all other characters in this lane (including your own). This can counter on reveals.',
    ),
    'OnDamageCharacterSilenceIt': Ability(
        name='OnDamageCharacterSilenceIt',
        description='After I damage a character, silence it.',
    ),
}