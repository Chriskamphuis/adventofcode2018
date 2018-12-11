from collections import defaultdict

class marble:
    def __init__(self, value, p=None, n=None):
        self.value = value
        self.p = p
        self.n = n

if __name__ == '__main__':
    last_marble = 7202600
    n_players = 471
    scores = defaultdict(int)
    
    first = marble(0)
    first.p = first
    first.n = first
    current_marble = first

    turn = 1
    while turn < last_marble:
        if turn % 23 != 0:
            cw_1 = current_marble.n
            cw_2 = cw_1.n
            new = marble(turn, cw_1, cw_2)
            cw_1.n = new
            cw_2.p = new
            current_marble = new
        else:
            current_player = (turn - 1) % n_players + 1
            current_marble = current_marble.p.p.p.p.p.p
            scores[current_player] += turn + current_marble.p.value
            two_back = current_marble.p.p
            current_marble.p = two_back
            two_back.n = current_marble

        turn += 1

    print(max([value for key, value in scores.items()]))
