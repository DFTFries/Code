# Greed is a dice game played with five six-sided dice. Your mission, should you choose to accept it, is to score a throw according to these rules. You will always be given an array with five six-sided dice values.

#  Three 1's => 1000 points
#  Three 6's =>  600 points
#  Three 5's =>  500 points
#  Three 4's =>  400 points
#  Three 3's =>  300 points
#  Three 2's =>  200 points
#  One   1   =>  100 points
#  One   5   =>   50 point
# Each of 5 dice can only be counted once in each roll. For example, a given "5" can only count as part of a triplet (contributing to the 500 points) or as a single 50 points, but not both in the same roll.

# Example scoring

#  Throw       Score
#  ---------   ------------------
#  5 1 3 4 1   250:  50 (for the 5) + 2 * 100 (for the 1s)
#  1 1 1 3 1   1100: 1000 (for three 1s) + 100 (for the other 1)
#  2 4 4 5 4   450:  400 (for three 4s) + 50 (for the 5)
# Note: your solution must not modify the input list.


#_________my solution_________________

def score(dice):
    dices = [die for die in dice]
    scores = {
        1 : {1 : 100,
             2 : 200,
             3 : 1000,
             4 : 1100,
             5 : 1200,
             6 : 2000},
        5 : {1 : 50,
             2 : 100,
             3 : 500,
             4 : 550,
             5 : 600,
             6 : 1000},
        6 : {3: 600},
        4 : {3: 400},
        3 : {3: 300},
        2 : {3: 200}
    }
    score = 0

    for i in range(1,7):
        if i in (2, 3, 4, 6) and dices.count(i) >= 3:
            score += scores.get(i).get(3)
        elif scores.get(i).get(dices.count(i)):
            score += scores.get(i).get(dices.count(i))
        else:
            pass

    return score

#_________ codewars solution__________

def score(dice): 
  sum = 0
  counter = [0,0,0,0,0,0]
  points = [1000, 200, 300, 400, 500, 600]
  extra = [100,0,0,0,50,0]
  for die in dice: 
    counter[die-1] += 1
  
  for (i, count) in enumerate(counter):
    sum += (points[i] if count >= 3 else 0) + extra[i] * (count%3)

  return sum 

#_______________________________________

def score(dice):
    # dice scores  [1   ,   2,   3,   4, 5,   6]
    scores_3same = [1000, 200, 300, 400, 500, 600]
    scores_single = [100 ,   0,   0,   0,  50,   0]
    
    sum = 0
    for i in range(1,7):
        count_i = dice.count(i)
        sum += (count_i // 3) * scores_3same[i-1] + (count_i % 3) * scores_single[i-1]
            
    return sum

#_______________________________________

def score(dice):
    total = 0
    for d in range(1, 7):
        count = dice.count(d)
        if count >= 3:
            total += 1000 if d == 1 else d * 100
            count -= 3
        total += 100 * count if d == 1 else 50 * count if d == 5 else 0
    return total