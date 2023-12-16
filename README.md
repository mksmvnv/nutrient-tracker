<!DOCTYPE html>
<html>
<head>
    <title>Eat and Visualize</title>
</head>
<body>

<h1>Eat and Visualize</h1>

<p>This is a simple daily macronutrient goal visualizer in the console.</p>

<img src="./assets/Figure_1.png" alt="eat-and-visualize">

<h2>Description</h2>

<p>The Eat and Visualize tracker reads your gender, age, height, weight and active level. Next, it builds your goal values (daily intake of calories, proteins, fats and carbohydrates). In the tracker menu, you can add the name of the food, calorie content, protein, fat and carbohydrate content and, based on this data, visualize the indicators in plots. The pie plot contain the percentages of proteins, fats and carbohydrates. Difference in macronutrient intake compared to goal data in bar plot. Percentage of completion of the daily requirement in pie plot. And plot for achieving daily targets throughout the day, depending on the food consumed.</p>

<h2>Prerequisites</h2>

<p>To run this code, you need to have the following installed:</p>

<ul>
    <li>Python 3.12.1</li>
    <li>Matplotlib</li>
    <li>NumPy</li>
</ul>

<pre>
pip install matplotlib numpy
</pre>

<h2>How to Run</h2>

<ol>
    <li>Clone this repository to your local machine.</li>
    <li>Navigate to the project directory.</li>
    <li>Run the following command to execute the code:</li>
</ol>

<pre>
python main.py
</pre>

<p>Fill in the data in the console one by one, completing the entry with the Enter command. When you are in the main menu:</p>

<ul>
    <li>Press <strong>1</strong> to add food.</li>
    <li>Press <strong>2</strong> to visualizing goal plots.</li>
    <li>Press <strong>3</strong> to exit the program.</li>
</ul>

<p>If you want to add a new food to your daily list, you can close the visualization window and press 1. And after adding, you can press 2 again and the visualization will update. But if you close the console completely, your result will be deleted.</p>

<h2>License</h2>

<p>The project is licensed under the <a href="https://opensource.org/licenses/MIT">MIT License</a>.</p>

</body>
</html>
