# **Q-TETRIS**

**Description:**

Qtetris is inspired from tetris game. In qtetris there are finite shapes that user have to arrange to complete one line similar to classical tetris but these shapes are made up of Quantum gates/ operators. For simplicity the rotation angle theta is considered as π radians

For example:

![](RackMultipart20220130-4-x7mere_html_9d8b5da8b4fa4c0c.gif) ![](RackMultipart20220130-4-x7mere_html_e66e26e7d4169e15.gif) ![](RackMultipart20220130-4-x7mere_html_426f4e77cd4bd54b.gif)

**Flowchart:**

![Shape1](RackMultipart20220130-4-x7mere_html_de589941a76beff2.gif) ![Shape2](RackMultipart20220130-4-x7mere_html_79647042be1d7149.gif)

**Game Rules:**

1. Run the code! to start playing the game
2. **Objective:** Usually, goal is to clear as many rows as possible while creating identity operation with as many gates as possible
3. Every completed row is executed on quantum computer: First qubit is prepared in |0\> then the different combination of gates in a same sequence (in that row) are applied to this single qubit and output is observed.
  1. If the combination of quantum gates which creates identity will be scored
  2. Score will be given as:

Example- completed row have [Rz, Y, Rx, I, Rz, Rx, Y]

![](RackMultipart20220130-4-x7mere_html_70c75bf4e761d764.gif)

This gives the ouput |0\> with 100% probability, so the score will be 7(number of quantum gates) \* 10 = 70

  1. Similarly in each completed row the maximum number of gates which gives 100% probability of occurrence of state |0\> with decide the score.
  2. In a completed line if multiple gate combinations create identity operation, then the maximum score is given based on number of gates used to create 100% probability of occurrence of state |0\>.

For example – [I, I, I] and [I, Ry, Rx, X, X, Rz] do make |0\> with 100% probability, so the score will be 60 (maximum value between 30 and 60).

![](RackMultipart20220130-4-x7mere_html_512454448447c759.gif)

**Note: Here 100% probability is observed through quantum simulator not actual quantum computer.**
