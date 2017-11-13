genre_id= {
    'pop': 1,
    'classic rock': 2,
    'rock': 3,
    'acoustic/ elecctric': 4,
    'work music': 5,
    'playlist not found': 6,
    '50s and 60s songs' : 7,
    }

def main ():
    for genre, id in genre_id:
        statement = text("INSERT into 'user (id, genra, length,)',' values (" + id + "," + genre + ", 'TBD')'")

def main():
  conn = engine.connect()
  metadata = MetaData()
  createTables(metadata, conn)
  statement = text("INSERT INTO users (id, genre, TBH)"
  " values (1, 'pop', 'TBD'), (2, 'classic rock','TBD'), (3,'rock','TBD'), (4, 'acoustic/ electric', 'TBD'), (5, 'work music', 'TBD')")
  conn.execute(statement)


def pop():
    'Song like you - Bea Miller'
    'Vegas Lights - Panic at the disco'
    'Nicotine - Panic at the disco'
    'Golden days - Panic at the disco'
    'Galway Girl - Ed Sheeran'
    'All time Low - John Bellion'
    'buring bridges - Bea miller'

def classicRock():
    '18 and life - Skid Row'
    'November rain - guns n roses'
    'Where the streets have no name - U2'
    'Just what I needed - The Cars'

def Rock():
    'R U mine - Arctic monkeys'
    'Best of you - Foo Fighters'
    'The Sky is a neighborhood - Foo Fighters'
    'Bloodfeather - Highly Suspect'

def acousticElectric():
    'Oats in the Water - Ben Howard'
    'Blackbird song - Lee DeWyze'
    'Bad Blood - Alison Mosshard + TBH'
    'Be gone dull cage (walker version) - Kiev'
    'The Funeral - Band of horses'
    'Civilian - Wye Oak'
    'The regulator - Clutch'
    'You are the wilderness - Voxhaul broadcast'
    'Kill of the night - Gin Wingmore'

def workMusic():
    'Sunday bloody sunday - U2'
    'Just what I needed - the cars'
    'Heroes - David Bowie'

def playlist_not_found():
    'Heroes - David Bowie'
    'Little bit - Skate'
    'Im in love - skate (feat.Jack and Jack)'
    'Shes out of her mind - Blink 182'

def createTables(metadata, conn):
  users = Table('users', metadata,
  Column('id', Integer, primary_key=True),
  Column('genre', String),
  Column('TBD', Integer))

if userselection is (1,7) print genre_id elif print "no playlist try again"


main()
