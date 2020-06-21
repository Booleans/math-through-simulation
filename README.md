# Math Through Simulation

Thanks to the law of large numbers, certain math problems can be solved through simulation. For example:

```
There are four people on the ground floor of a building that has five levels not including the ground floor. 
They all get into the same elevator. If each person is equally likely to get on any floor and they leave independently 
of each other, what is the probability that no two passengers will get off at the same floor?
```

With the help of (Python) code you can simply simulate this scenario occurring millions times and look at what proportion of the time no two passengers get off on the same floor. This will be very close to the precise result of the closed-form solution. 

### Purpose

The purpose of this is so that my students and I can double-check the solutions we've calculated by-hand for various probability problems. These problems are sometimes for data science interview prep and other times just for fun. Additionally, these problems help me practice with and learn new techniques using NumPy.

When possible, I try to write my simulations using NumPy, as opposed to pure Python. NumPy code runs much faster and as a result, many more simultions can be run, allowing for more precise results. I encourage my students to do the same and this repository allows them to compare their code with mine.

![NumPy Logo](https://upload.wikimedia.org/wikipedia/commons/thumb/1/1a/NumPy_logo.svg/2000px-NumPy_logo.svg.png)
