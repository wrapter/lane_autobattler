from sqlalchemy import exists
from database import SessionLocal
from db_deck import DbDeck, add_db_deck
from deck import Deck
from redis_utils import rget_json, rlock, rset_json
from settings import BOT_DECK_USERNAME, COMMON_DECK_USERNAME


COMMON_DECKS = [
    {
        'name': 'Learn to play',
        'cards': [
            'Pabu',
            'Meelo',
            'Roku',
            'Hakoda',
            'Visola',
            'Momo',
            'Southern Raider',
            'Naga',
            'Mai',
            'Opal',
            'Yon Rha',
            'Zaheer',
            'Oogi',
            'Gran Gran Kanna',
            'Korra',
            'Master Pakku',
            'Kyoshi',
            'Tarrlok',
        ],
    },
    {
        'name': 'Healing Hands',
        'cards': [
            'Zuko',
            'Zuko',
            'Tonraq',
            'Mother Kya',
            'Mother Kya',
            'Kya',
            'Kya',
            'Katara',
            'Katara',
            'Sokka',
            'Sokka',
            'Hama',
            'Hama',
            'Ghazan',
            'Ghazan',
            'Unalaq',
            'Taqukaq',
            'Gran Gran Kanna',
            'Kyoshi',
        ]
    },
    {
        'name': 'Switcheroo',
        'cards': [
            'Monk Gyatso',
            'Monk Gyatso',
            'Ikki',
            'Momo',
            'Momo',
            'Yangchen',
            'Bumi II',
            'Opal',
            'Opal',
            'Appa',
            'Jinora',
            'Jinora',
            'Ming Hua',
            'Tenzin',
            'Tenzin',
            'Aang',
            'Aang',
            'Uncle Iroh',
        ]
    },
    {
        'name': 'Attack and Defense',
        'cards': [
            'Iroh II',
            'Iroh II',
            'Combustion Man',
            'Pabu',
            'Hiroshi',
            'Tonraq',
            'Izumi',
            'Izumi',
            'Taqukaq',
            'Taqukaq',
            'Riley',
            'Toph',
            'Toph',
            'Sozin',
            'Sozin',
            'Mai',
            'Fire Lord Ozai',
            'Master Pakku',
        ],
    },
    {
        'name': 'The Card Advantage',
        'cards': [
            'Hiroshi',
            'Hiroshi',
            'Tonraq',
            'Tonraq',
            'Dai Li Agent',
            'Kai',
            'Kai',
            'Prince Wu',
            'La',
            'La',
            'The Big Bad Hippo',
            'The Big Bad Hippo',
            'Appa',
            'Professor Zei',
            'Moon Spirit Yang',
            'Moon Spirit Yang',
            'The Boulder',
            'The Boulder',
        ]
    },
    {
        'name': 'Naked Aggression',
        'cards': [
            'Combustion Man',
            'Combustion Man',
            'Iroh II',
            'Iroh II',
            'Hakoda',
            'Hakoda',
            'Riley',
            'Opal',
            'Opal',
            'Sozin',
            'Sokka',
            'Ghazan',
            'Oogi',
            'Oogi',
            'Admiral Zhao',
            'Admiral Zhao',
            'Uncle Iroh',
            'Fire Lord Ozai',
        ]
    },
    {
        'name': 'Lock and Chain',
        'cards': [
            'Dai Li Agent',
            'Dai Li Agent',
            'Pabu',
            'Kuvira',
            'Kuvira',
            'Kai',
            'Kai',
            'La',
            'La',
            'Roku',
            'Baatar Jr',
            'Baatar Jr',
            'Mai',
            'Lin',
            'Lin',
            'Professor Zei',
            'Suyin',
            'Suyin',
        ]
    },
]


BOT_DRAFT_DECKS = [
    {
        'name': 'Bot draft deck 1',
        'cards': [
            'Monk Gyatso',
            'Kai',
            'Appa',
            'Hakoda',
            'Oogi',
            'Hakoda',
            'Kai',
            'Appa',
            'Admiral Zhao',
            'Naga',
            'Tenzin',
            'Appa',
            'Admiral Zhao',
            'Bumi II',
            'Hakoda',
            'Oogi',
            'Riley',
            'Combustion Man',
        ]
    },
    {'name': 'Bot draft deck 2',
    'cards': ['Toph',
    'Fire Lord Ozai',
    'Combustion Man',
    'Fire Lord Ozai',
    'Iroh II',
    'Hakoda',
    'Hakoda',
    'Korra',
    'Mai',
    'Yon Rha',
    'Uncle Iroh',
    'Sozin',
    'Uncle Iroh',
    'Pabu',
    'Sozin',
    'Mai',
    'Mai',
    'Pabu']},
    {'name': 'Bot draft deck 3',
 'cards': ['Izumi',
  'Mother Kya',
  'Zaheer',
  'Master Pakku',
  'Mother Kya',
  'Katara',
  'Mother Kya',
  'Cabbage Man',
  'Sokka',
  'Hama',
  'Naga',
  'Ghazan',
  'Gran Gran Kanna',
  'Zuko',
  'Zaheer',
  'Hama',
  'Kya',
  'Zuko']},
  {'name': 'Bot draft deck 4',
 'cards': ['Baatar Jr',
  'La',
  'Zaheer',
  'Korra',
  'Fang',
  'Zaheer',
  'Dai Li Agent',
  'La',
  'Sozin',
  'Uncle Iroh',
  'Zaheer',
  'Kyoshi',
  'Hakoda',
  'Dai Li Agent',
  'Kai',
  'Ghazan',
  'Kai',
  'Appa']},
  {'name': 'Bot draft deck 5',
  'cards': ['Yangchen',
  'Roku',
  'Aang',
  'Cabbage Man',
  'Tonraq',
  'Hiroshi',
  'Appa',
  'Aang',
  'Kuvira',
  'Zaheer',
  'Korra',
  'Aang',
  'Sozin',
  'Opal',
  'Zaheer',
  'Kyoshi',
  'Korra',
  'Momo']},
{'name': 'Bot draft deck 6',
 'cards': ['Jinora',
  'Aang',
  'Uncle Iroh',
  'Zuko',
  'Momo',
  'Hakoda',
  'Katara',
  'Suyin',
  'Opal',
  'Opal',
  'Aang',
  'Gran Gran Kanna',
  'Korra',
  'Yangchen',
  'Suyin',
  'Lin',
  'Pabu',
  'Monk Gyatso']}  
]


def create_common_decks():
    with SessionLocal() as sess:
        for deck in COMMON_DECKS:
            if not sess.query(exists().where(DbDeck.name == deck['name']).where(DbDeck.username == COMMON_DECK_USERNAME)).scalar():
                add_db_deck(sess, deck['cards'], COMMON_DECK_USERNAME, deck['name'], None)

        for deck in BOT_DRAFT_DECKS:
            if not sess.query(exists().where(DbDeck.name == deck['name']).where(DbDeck.username == BOT_DECK_USERNAME)).scalar():
                add_db_deck(sess, deck['cards'], BOT_DECK_USERNAME, deck['name'], None)
