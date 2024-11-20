### DATA DUPLICATION
We will duplicate the dataset with dask in this file. Before of that I try to do it with PySpark. But because of many reason (there was so variable to set) I falled. Afterward with my seniors advice, I tried to dublicate dataset with Dask.

Here important to care on channels of modules. Because I got so many errors. When I made sure to set the same channel between the installed modules, the errors stopped.
***
### REQUIREMENTS:
```Python
import dask.dataframe as dd
import pandas as pd
```
***
### SOME ERRORS:
```AttributeError: module 'pyarrow.lib' has no attribute 'Bool8Type'``` 

1. Pandas and Dask was installed by PyPI and I thought the reason of inconsistency was withstand the different of channels. And I deleted both and installed with Conda (Because I was in the Conda environment).

```AttributeError: module 'pyarrow.lib' has no attribute 'Bool8Type'```

2. Unfortunately, I kept getting error `pyarrow.lib`. Afterward, I tried to delete PyArrow and install conda-forge version (Because PyArrow channel was PyPI also).

```
TypeError: Cannot convert numpy.ndarray to numpy.ndarray
TypeError: An error occurred while calling the read_csv method registered to the pandas backend.
Original Message: Cannot convert numpy.ndarray to numpy.ndarray
TypeError: An error occurred while calling the read_csv method registered to the pandas backend.
Original Message: An error occurred while calling the read_csv method registered to the pandas backend.
Original Message: Cannot convert numpy.ndarray to numpy.ndarray
```

3. And I tried to update Numpy, Pandas, Dask and PyArrow in one command: `conda update numpy pandas dask pyarrow`

```
TypeError: Cannot convert numpy.ndarray to numpy.ndarray
TypeError: An error occurred while calling the read_csv method registered to the pandas backend.
Original Message: Cannot convert numpy.ndarray to numpy.ndarray
TypeError: An error occurred while calling the read_csv method registered to the pandas backend.
Original Message: An error occurred while calling the read_csv method registered to the pandas backend.
Original Message: Cannot convert numpy.ndarray to numpy.ndarray
```

4. In this step, I become aware of Numpy channel (was PyPI). And I tried to do same thing on Numpy. I uninstalled PyPI version and installed conda-forge version.
> Here I saw some interesting points. For example: After I uninstall Numpy, directly uninstalled Pandas, Dask and PyArrow.

5. Because of uninstalling Dask, I installed it again: `conda install dask`

And worked.