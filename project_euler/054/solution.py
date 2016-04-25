import sys

class Card:
 
    def __init__(self, s):
        self.suit = s[1]
        self.face = s[0]
        self.value = self.getValue()

    def getValue(self):
        value = -1
        if self.face == 'A':
            value = 14
        elif self.face == 'T':
            value = 10
        elif self.face == 'J':
            value = 11
        elif self.face == 'Q':
            value = 12
        elif self.face == 'K':
            value = 13
        else:
            value = int(self.face)
        return value

    def __lt__(self, other):
        return self.value < other.getValue()

class PokerHand():

    def __init__(self, cards = list()):
        self.cards = cards
        

    def checkHand(self):
        if self.checkRoyalFlush():
            return 9 
        elif self.checkStraightFlush():
            return 8
        elif self.checkFourOfAKind():
            return 7
        elif self.checkFullHouse():
            return 6
        elif self.checkFlush():
            return 5
        elif self.checkStraight():
            return 4
        elif self.checkThreeOfAKind():
            return 3            
        elif self.checkTwoPair():
            return 2
        elif self.checkPair():
            return 1   
        else:
            return 0

    def countFaces(self):
    	counts = {}
    	for card in self.cards:
    		if card.face in counts:
    			counts[card.face] += 1
    		else:
    			counts[card.face] = 1
    	return counts
        
    def checkRoyalFlush(self):
    	if not self.checkFlush():
    		return False
    	# make a list of all of the card faces we have
    	faces = [card.face for card in self.cards]
    	# check that we have all the right card faces
    	return 'A' in faces and 'K' in faces and 'Q' in faces and 'J' in faces and "10" in faces

    def checkStraightFlush(self):
    	if not self.checkFlush():
    		return False
    	return self.checkStraight()

    def checkFourOfAKind(self):
    	counts = self.countFaces()

    	for c in counts:
    		if counts[c] == 4:
    			return True
    	return False

    def checkFullHouse(self):
    	counts = self.countFaces()
    	occurances = [counts[f] for f in counts]
    	return 3 in occurances and 2 in occurances

    def checkFlush(self):
    	# pick out the suit of the first card
    	suit = self.cards[0].suit
    	# iterate through the rest of the cards
    	for card in self.cards[1:]:
    		if card.suit != suit:
    			# if any of the cards is a different suit, we can stop here
    			return False
    	return True

    def checkStraight(self):
    	self.cards.sort()
    	for f in range(0, 5): # range(0, 5) -> [0,1,2,3,4]

    		#order is between 2 and 14
    		#we are making it to be between 0 and 12
	    	first = self.cards[f].value - 2

	    	ok = True

	    	for i in range(1, 5): # range(1, 5) -> [1,2,3,4]
	    		card = self.cards[(f + i) % 5] # puts indexes >= 5 back to the start
	    		o = card.value - 2

	    		if o != first + i:
	    			ok = False

	    	if ok:
	    		return True

    	return False

    def checkThreeOfAKind(self):
    	counts = self.countFaces()
    	for c in counts:
    		if counts[c] == 3:
    			return True
    	return False

    def checkTwoPair(self):
    	counts = self.countFaces()

    	found_one = False
    	for c in counts:
    		if counts[c] == 2:
    			if found_one:
    				return True
    			else:
    				found_one = True
    	return False

    def checkPair(self):
    	counts = self.countFaces()
    	for c in counts:
    		if counts[c] == 2:
    			return True
    	return False

def p1_win(p1, p2):
    a = p1.checkHand()
    b = p2.checkHand()
    if a > b:
        return True
    elif a == b:
        x = sorted([c.getValue() for c in p1.cards], reverse=True)
        y = sorted([c.getValue() for c in p2.cards], reverse=True)
        if a == 0:
            i = 0
            while x[i] == y[i]:
                i += 1
            return x[i] > y[i]
        elif a == 1:
            i = -1
            j = -1
            p1_cards = set()
            p2_cards = set()
            for c in x:
                if c in p1_cards:
                    i = c
                    break
                p1_cards.add(c)
            for c in y:
                if c in p2_cards:
                    j = c
                    break
                p2_cards.add(c)
            return i > j
        else:
            print a, x, y, 'draw'
            return False
    else:
        return False

ans = 0
for line in sys.stdin.readlines():
    parts = line.strip().split()
    p1 = PokerHand([Card(s) for s in parts[:5]])
    p2 = PokerHand([Card(s) for s in parts[5:]])
    if p1_win(p1, p2):
        ans += 1
print ans
