# Homework Assignment 15

In [Homework Assignment 8](https://github.com/PGE383-HPC-Fall2018/assignment8) we wrote a `Toughness` class that computes a materials toughness given stress/strain data in file.  In this assignment, we will make the integration (i.e. toughness computation) a parallel task.  You should complete the new `ParallelToughness` class, specifically the function `compute_toughness()` shown in [assignment14.py](assignment14.py).  

I have included a solution to [Homework Assignment 8](https://github.com/PGE383-HPC-Spring2018/assignment8) which includes the class `StressStrainConverter` to read in the data file and create the class attributes `true_stress` and `true_strain`.  You should distribute the data contained in these attributes as evenly as possibly over the `size` of the MPI computation, then perform the integration on the parallel data subsets using `scipy.integrate.trapz` locally on each processor.  Finally, use a parallel reduction to sum up each of the parallel contributions to the rank `0` processor.

Your code should be parallel consistent, i.e. it should produce the exact same answer independent of the number of processors you specify.

## Testing

If you would like to check to see if your solution is correct, run the following commands at the Terminal command line:

```bash
mpiexec -np 2 test.py 
mpiexec -np 3 test.py 
```
