"""
1.We have provided you with two lists, letters and points. We would like to combine these two into a dictionary that would map a letter to its point value.create a dictionary called letter_to_points that has the elements of letters as the keys and the elements of points as the values.

2.We want to create a function that will take in a word and return how many points that word is worth.Define a function called score_word that takes in a parameter word.

3.Inside score_word, create a variable called point_total.

4.After defining point_total, create a for loop that goes through the letters in word and adds the point value of each letter to point_total.
You should get the point value from the letter_to_points dictionary. 

5.After the for loop is finished, return point_total.

6.Let’s test this function! Create a variable called brownie_points and set it equal to the value returned by the score_word() function with an input of "BROWNIE".

7.Create a dictionary called player_to_words that maps players to a list of the words they have played. This table represents the data to transcribe into your dictionary:

8.Iterate through the items in player_to_words. Call each player player and each list of words words.Within your loop, create a variable called player_points and set it to 0.

9.Within the loop, create another loop that goes through each word in words and adds the value of score_word() with word as an input.

10.After the inner loop ends, set the current player value to be a key of player_to_points, with a value of player_points.

11.player_to_points should now contain the mapping of players to how many points they’ve scored. Print this out to see the current standings for this game!If you’ve calculated correctly, wordNerd should be winning by 1 point.

12.If you want extended practice, try to implement some of these ideas with the Python you’ve learned:play_word() — a function that would take in a player and a word, and add that word to the list of words they’ve playedupdate_point_totals() — turn your nested loops into a function that you can call any time a word is playedmake your letter_to_points dictionary able to handle lowercase inputs as well

"""

letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]

zipped_file = zip(letters,points)
# print(zipped_file)
letter_to_points = {key:value for key, value in zipped_file}
print(letter_to_points)
print('\n')
letter_to_points[""] = 0
print(letter_to_points)
print('\n')

#start function
def score_word(word):
  point_total = 0
  #for start
  for i in word.lower():
    #inside for loop
    point_total += letter_to_points.get(i, 0)
    #inside for loop finish
  #for finish
  return point_total
#end of function

brownie_points  = score_word("BROWNIE")
print(brownie_points)
print('\n')
player_to_words = {
  "player1":["BLUE","TENNIS","EXIT"],
  'wordNerd':["EARTH","EYES","MACHINE"],
  "Lexi Con":["ERASER","BELLY","HUSKY"],
  "Prof Reader":["ZAP","COMA","PERIOD"]
  }

print(player_to_words)

player_to_points = {}

for player, words in player_to_words.items():
  player_points = 0
  for word in words:
    player_points += score_word(word)
  player_to_points[player] = player_points


print(player_to_points)
print('\n')

def play_word(player,word):
    player_to_words["player"] = "word"
    return play_word
    
def update_point_totals():
  for player, words in player_to_words.items():
    player_points = 0
    for word in words:
      player_points += score_word(word)
    player_to_points[player] = player_points









