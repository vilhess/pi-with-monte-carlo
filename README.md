# Estimating π with Monte Carlo Method

This project demonstrates the Monte Carlo method for estimating the value of π. The Monte Carlo method is a simulation technique that uses random numbers to estimate mathematical values.

## How does it work?

In this code, we use the Monte Carlo method to estimate π by utilizing the relationship between the area of a circle and the area of a square. Here's how the code works:

1. A matrix of size 1000x1000 is created and initialized with zeros.
2. A circle with a radius of 250 is drawn within the matrix, along with a square with a height equals of the radius. Points inside the circle are set to 1, and points inside the square are set to 0.5.
3. A loop is executed 10,000 times. At each iteration, a random point is chosen within the matrix.
4. The number of points chosen inside the circle is counted in the `circle` variable, and the number of points chosen inside the square is counted in the `square` variable.
5. The `circle/square` ratio is used to estimate the value of π.
6. The values of `circle/square` are recorded at specific iterations in the `vals` list.
7. Graphs are plotted to visualize the estimation of π over time.

## How to run the code?

To run the code, you need a Python environment with the matplotlib and numpy libraries installed. You can install them by running the following command:

`pip install -r requirements.txt`


Once the dependencies are installed, execute the code by running the `main.py` Python file. The graphs will be displayed in real-time, showing the estimation of π as the points are generated.

## Expected Results

As you run the code and generate more points, the estimation of π should get closer to its true value. The graphs will allow you to visualize the convergence of the estimation towards π.

Feel free to adjust parameters such as the radius of the circle or the number of iterations to explore their impact on the estimation of π.

---

Thank you for checking out this project! If you have any questions or suggestions, please don't hesitate to reach out.

Note: This project is based on the explanation provided in the YouTube video of MarbleScience : [https://youtu.be/7ESK5SaP-bc](https://youtu.be/7ESK5SaP-bc). Make sure to check it out for a detailed explanation of the Monte Carlo method.
 

