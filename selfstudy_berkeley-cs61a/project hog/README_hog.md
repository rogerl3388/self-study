This is the first project of the course, where student must define the logic for the game of Hog
- Student only updates the file 'hog.py'

The game of Hog is a 2-player game in which players take turn choosing a number of six-sided dice (up to 10) and rolling
- Sow Sad: if a "1" is rolled on any of the dice, the score of that roll is 1
- Otherwise, the score of the roll is the sum of all dice values

The first player to accumulate 100 points wins the game

There are 2 special rules you can optionally add:
- Pig Tail: if you choose to roll zero dice, you add a score 2*abs(tens - ones) + 1, where the "tens" and "ones" are the tens and ones place of your opponent's score, respectively
- Square Swine: if your total score is a perfect square after gaining points, your score jumps to the next higher perfect square