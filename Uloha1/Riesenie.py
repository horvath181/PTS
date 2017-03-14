# import math for floor function
import math
# dictionary of players and their scores
players = {}
# list of juniors
juniors = []
def sort_dict():
    return [(k, players[k]) for k in sorted(players, key=players.get, reverse=True)]
# decorator - checks the password and if it is correct calls the function with its arguments
def check_pass(function):
    def wrapper(*args, **kwargs):
        check = input("What's the password?")
        if(check == password):
            return function(*args, **kwargs)
        else:
            return print("Wrong password.")
    return wrapper
# adds 'number' to score of player with name 'name' (players[name]) or adds a player with name 'name' and score equal to 'number'
@check_pass
def points(name, number):
    if name in players:
        players[name] += number
    else:
        players[name] = number
# reduces points of all players by a 'precentage'%
@check_pass
def red(percentage):
    for key in players:
        players[key] = math.floor(players[key]*(1.0-(percentage/100)))
# adds 'name' among juniors (if he's not a player yet, it'll add him there as well with score equal to 0)
@check_pass
def junior(name):
    if not name in juniors:
        juniors.append(name)
        if not name in players:
            players[name] = 0
# sorts 'players' by score from the highest to the lowest and writes it out
def ranking():
    print('Ranking of all players:')
    s = sort_dict()
    for k, v in s:
        print(k,': ',v)
# same as ranking, but with juniors only
def ranking_junior():
    print('Ranking of juniors:')
    s = sort_dict()
    for k, v in s:
        if k in juniors:
            print(k,': ',v)
# ends the session
@check_pass
def end():
    quit()
# first set password for this session
password = input("Enter password for this session: ")
while True:
# asks for command
    com = input("Enter command: ").split()
    # decides which command you wrote and continues as is necessary
    if com[0] == "points":
        points(com[1], int(com[2]))
    elif com[0] == "reduce":
        red(float(com[1]))
    elif com[0] == "junior":
        junior(com[1])
    elif com[0] == "ranking":
        if len(com)>1:
            ranking_junior()
        else:
            ranking()
    elif com[0] == "quit":
        end()