# **Q-TETRIS**

**Description:**
Qtetris is inspired from tetris game. In qtetris there are finite shapes that user have to arrange to complete one line similar to classical tetris but these shapes are made up of Quantum gates/ operators. For simplicity the rotation angle theta is considered as π radians
For example:
  ![](.files/2022-01-30-12-35-55-image.png)
**Flowchart:**
 ![](.files/2022-01-30-12-36-21-image.png)
**Game Rules:**

1. Run the code! to start playing the game
2. **Objective:** Usually, goal is to clear as many rows as possible while creating identity operation with as many gates as possible
3. Every completed row is executed on quantum computer: First qubit is prepared in |0\> then the different combination of gates in a same sequence (in that row) are applied to this single qubit and output is observed.
   1. If the combination of quantum gates which creates identity will be scored
   2. Score will be given as:
      Example- completed row have [Rz, Y, Rx, I, Rz, Rx, Y]
      ![](.files/2022-01-30-12-36-40-image.png)
      This gives the ouput |0\> with 100% probability, so the score will be 7(number of quantum gates) \* 10 = 70
   3. Similarly in each completed row the maximum number of gates which gives 100% probability of occurrence of state |0\> with decide the score.
   4. In a completed line if multiple gate combinations create identity operation, then the maximum score is given based on number of gates used to create 100% probability of occurrence of state |0\>.
      For example – [I, I, I] and [I, Ry, Rx, X, X, Rz] do make |0\> with 100% probability, so the score will be 60 (maximum value between 30 and 60).
      ![](.files/2022-01-30-12-37-05-image.png)
      **Note: Here 100% probability is observed through quantum simulator not actual quantum computer.**
