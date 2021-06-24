# PSO
Finding the minimum of 2 function with particle swarm optimization algorithm.
# explanation
finding minimum of function:

- ![image](https://user-images.githubusercontent.com/47561586/123279121-ce303b00-d51c-11eb-8fbc-6d6c930df971.png)

and function:
- ![image](https://user-images.githubusercontent.com/47561586/123279150-d6887600-d51c-11eb-93ac-90d5765c4508.png)
# executation
- run with python3.
# algorithm
First, we randomly place the points in the given interval to the size of the count or the initial number, and in each step, the speed and locations change.
FindMin(count, function1, -10, 10, w, c1, c2, end_point)
- Speed: The initial speed is given randomly in the range of 1 to 3 and each time the speed is updated as follows.

v (t + 1) = wxv (t) + c1 random (-1,1) * (Pbest - x (t)) + c2 * random (-1,1) * (Gbest - x (t))
- Location of points: In each step (x (t + 1) = x (t) + vt is the location.
- best self (Pbest): In each step the current value of the function is checked with its previous values and the minimum is stored in Pbest.
- Best Total Population (Gbest): At each stage, all points are checked and the best one (meaning that the function has a lower response) is replaced than the previous Gbest.
- End of the algorithm: The algorithm stops after the best answer (Gbest) did not change after the end_point step.
