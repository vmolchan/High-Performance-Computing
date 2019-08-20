# Homework Assignment 14

When parallel tasks are independent from each other, they are called *embarrassingly parallel*.  While there are several ways to approach these problems, including batch schedulers, we can also write simple MPI programs to complete these tasks.

In [Homework Assignment 9](https://github.com/PGE383-HPC-Fall2018/assignment9) we wrote a `Plotter` class that would process a data file, converting the raw data to true stress and strain, compute the toughness, and produce a plot.  If we had multiple data files, we could use this class to process them in parallel on a multi-processor machine.  In the assignment that follows, we will only do test this for two data files, but of course, the real utility of writing a parallel program would only be realized if we had many more to process.

Your assignment is to complete the Python script [assignment14.py](assignment14.py).  When the script is executed with the following command:

```bash
mpiexec -np 2 python assignment14.py
```

the script should process the two data files `data_0.dat` and `data_1.dat` in parallel using the `Plotter` class and associated functions from [Homework Assignment 9](https://github.com/PGE383-HPC-Fall2018/assignment9) producing plots `plot_0.png` and `plot_1.png`.  I am including my solution to [Homework Assignment 9](https://github.com/PGE383-HPC-Fall2018/assignment9) for reference and/or use if you'd like.

## Testing

If you would like to check to see if your solution is correct, run the following commands at the Terminal command line in sequence:

```bash
mpiexec -np 2 python assignment14.py
```

```bash
python test.py
```
