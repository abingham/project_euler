import sys

values = {
    '2':1,
    '3':2,
    '4':3,
    '5':4,
    '6':5,
    '7':6,
    '8':7,
    '9':8,
    'T':9,
    'J':10,
    'Q':11,
    'K':12,
    'A':13
    }

def basic_flush(cards):
    suit = cards[0].suit
    for v in range(1,5):
        if not cards[v].suit == suit:
            return False
    return True

def basic_straight(cards):
    for i in range(len(cards) - 1):
        if cards[i].value != (cards[i + 1].value - 1):
            return False
    return True

# bool, initial_value
def straight(hand):
    return (basic_straight(hand.cards), hand.cards[0].value)

# bool, 0
def flush(hand):
    return (basic_flush(hand.cards), 0)

# bool, initial_value
def straight_flush(hand):
    return (basic_flush(hand.cards) and basic_straight(hand.cards), hand.cards[0].value)

# bool, 0
def royal_flush(hand):
    return (straight_flush(hand) and hand.cards[0].value == 9, 0)

def n_of_a_kind(hand, target):
    sum = 0
    vals = []
    for card,count in hand.counts.items():
        if count == target:
            sum += 1
            vals.append(card)
    vals.sort()
    vals.reverse()
    return sum, vals

# bool, ([3-vals], [2-vals])
def full_house(hand):
    c3,v3 = n_of_a_kind(hand, 3)
    c2,v2 = n_of_a_kind(hand, 2)
    return (c3 == 1 and c2 == 1, (v3, v2))

# bool, [vals]
def pair(hand):
    c,v = n_of_a_kind(hand, 2)
    return (c == 1, v)

# bool, [vals]
def two_pairs(hand):
    c,v = n_of_a_kind(hand, 2)
    return (c == 2, v)

# bool, [val]
def three_of_a_kind(hand):
    c,v = n_of_a_kind(hand, 3)
    return (c > 0, v)

# bool, [val]
def four_of_a_kind(hand):
    c,v = n_of_a_kind(hand, 4)
    return (c > 0, v)

ROYAL_FLUSH     = 10
STRAIGHT_FLUSH  = 9
FOUR_OF_A_KIND  = 8
FULL_HOUSE      = 7
FLUSH           = 6
STRAIGHT        = 5
THREE_OF_A_KIND = 4
TWO_PAIRS       = 3
PAIR            = 2
HIGH_CARD       = 1

score_table = [
    (royal_flush, ROYAL_FLUSH),
    (straight_flush, STRAIGHT_FLUSH),
    (four_of_a_kind, FOUR_OF_A_KIND),
    (full_house, FULL_HOUSE),
    (flush, FLUSH),
    (straight, STRAIGHT),
    (three_of_a_kind, THREE_OF_A_KIND),
    (two_pairs, TWO_PAIRS),
    (pair, PAIR)
    ]

class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    def __lt__(self, other):
        return self.value < other.value
    
    def __repr__(self):
        return 'Card<%s, %s>' % (self.value, self.suit)

class Hand:
    def __init__(self, cards):
        self.cards = cards[:]
        self.cards.sort()
        
        self._init_counts()

        self.score, self.discriminator = self._get_score()

    def __lt__(self, other):
        if self.score < other.score:
            return True
        elif self.score == other.score:
            if self.discriminator < other.discriminator:
                return True
            elif self.discriminator == other.discriminator:
                for i in range(len(self.cards) - 1, -1, -1):
                    if self.cards[i] != other.cards[i]:
                        return self.cards[i] < other.cards[i]
        return False

    def __repr__(self):
        return 'CARDS: %s\nCOUNTS: %s\nSCORE: %s\nDISC: %s' % (self.cards,
                                                               self.counts,
                                                               self.score,
                                                               self.discriminator)

    def _init_counts(self):
        self.counts = {}
        for c in self.cards:
            try:
                self.counts[c.value] += 1
            except KeyError:
                self.counts[c.value] = 1

    # score, discriminator
    def _get_score(self):
        for func,score in score_table:
            match, disc = func(self)
            if match:
                return (score, disc)
        return (HIGH_CARD, self.cards[len(self.cards) - 1].value)

def run(fname):
    f = open(fname, 'r')
    wins = 0
    losses = 0
    for l in f:
        cards = l.split()
        hand1 = Hand([Card(values[c[0]], c[1]) for c in cards[:5]])
        hand2 = Hand([Card(values[c[0]], c[1]) for c in cards[5:]])
        
        if hand1 < hand2 and hand2 < hand1:
            print hand1
            print hand2

        if hand2 < hand1 and not hand1 < hand2:
            wins += 1
        elif hand1 < hand2:
            losses += 1

    f.close()
    return wins

def test():
    hands = [
        ('high_8',                  # label
         Hand([Card(1, 'C'),        # hand
               Card(2, 'D'),
               Card(3, 'S'),
               Card(6, 'H'),
               Card(8, 'C')]),
         HIGH_CARD),                        # expected score
        ('high_k', 
         Hand([Card(1, 'C'),
               Card(2, 'D'),
               Card(3, 'S'),
               Card(6, 'H'),
               Card(12, 'C')]),
         HIGH_CARD),
        ('pair_4', 
         Hand([Card(1, 'C'),
               Card(4, 'D'),
               Card(4, 'S'),
               Card(6, 'H'),
               Card(12, 'C')]),
         PAIR),
        ('pair_9', 
         Hand([Card(1, 'C'),
               Card(4, 'D'),
               Card(9, 'S'),
               Card(6, 'H'),
               Card(9, 'C')]),
         PAIR),
        ('two_pair_5_7', 
         Hand([Card(1, 'C'),
               Card(5, 'D'),
               Card(7, 'S'),
               Card(5, 'H'),
               Card(7, 'C')]),
         TWO_PAIRS),
        ('two_pair_4_q', 
         Hand([Card(4, 'C'),
               Card(9, 'D'),
               Card(11, 'S'),
               Card(11, 'H'),
               Card(4, 'C')]),
         TWO_PAIRS),
        ('three_5', 
         Hand([Card(5, 'C'),
               Card(9, 'D'),
               Card(5, 'S'),
               Card(11, 'H'),
               Card(5, 'C')]),
         THREE_OF_A_KIND),
        ('three_6', 
         Hand([Card(6, 'C'),
               Card(6, 'D'),
               Card(6, 'S'),
               Card(11, 'H'),
               Card(5, 'C')]),
         THREE_OF_A_KIND),
        ('straight_3', 
         Hand([Card(3, 'C'),
               Card(7, 'D'),
               Card(4, 'S'),
               Card(6, 'H'),
               Card(5, 'C')]),
         STRAIGHT),
        ('straight_6',
         Hand([Card(9, 'C'),
               Card(7, 'D'),
               Card(8, 'S'),
               Card(6, 'H'),
               Card(10, 'C')]),
         STRAIGHT),
        ('flush_9',
         Hand([Card(1, 'C'),
               Card(3, 'C'),
               Card(5, 'C'),
               Card(7, 'C'),
               Card(9, 'C')]),
         FLUSH),
        ('flush_q',
         Hand([Card(1, 'C'),
               Card(3, 'C'),
               Card(5, 'C'),
               Card(7, 'C'),
               Card(11, 'C')]),
         FLUSH),
        ('fullhouse_3_9',
         Hand([Card(3, 'C'),
               Card(9, 'D'),
               Card(3, 'H'),
               Card(9, 'S'),
               Card(3, 'H')]),
         FULL_HOUSE),
        ('fullhouse_k_2',
         Hand([Card(12, 'D'),
               Card(12, 'C'),
               Card(1, 'D'),
               Card(12, 'S'),
               Card(1, 'H')]),
         FULL_HOUSE),
        ('four_4',
         Hand([Card(4, 'D'),
               Card(4, 'S'),
               Card(12, 'S'),
               Card(4, 'H'),
               Card(4, 'H')]),
         FOUR_OF_A_KIND),
        ('four_6',
         Hand([Card(6, 'D'),
               Card(6, 'S'),
               Card(6, 'S'),
               Card(2, 'H'),
               Card(6, 'H')]),
         FOUR_OF_A_KIND),
        ('straight_flush_7',
         Hand([Card(7, 'D'),
               Card(9, 'D'),
               Card(8, 'D'),
               Card(11, 'D'),
               Card(10, 'D')]),
         STRAIGHT_FLUSH),
        ('straight_flush_8',
         Hand([Card(12, 'D'),
               Card(9, 'D'),
               Card(8, 'D'),
               Card(11, 'D'),
               Card(10, 'D')]),
         STRAIGHT_FLUSH),
        ('royal_flush',
         Hand([Card(10, 'D'),
               Card(12, 'D'),
               Card(13, 'D'),
               Card(11, 'D'),
               Card(9, 'D')]),
         ROYAL_FLUSH),
        ]

    for i in xrange(len(hands)):
        ni,hi,ei = hands[i]
        if not hi.score == ei:
            print ni,'expected score is no actual score: %s != %s'%(ei,hi.score)
            print hi
            continue
        if hi < hi:
            print ni,'should not be less than itself!'
        for j in xrange(i + 1, len(hands)):
            nj,hj,ej = hands[j]
            if not hi < hj:
                print ni,'should be less than',nj
                print hi
                print hj
                print ' '

print run(sys.argv[1])
# test()
