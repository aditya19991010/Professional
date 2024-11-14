# https://numpy.org/devdocs/user/quickstart.html

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import sys


def numpyops():
    ### The basics

    ## An example
    a = np.arange(15)
    a = a.reshape(3, 5)
    print(a.shape)
    print(a.ndim)
    print(a.size)
    print(a.itemsize) # Length of one array element in bytes
    print(a.dtype.name)
    print(type(a))

    ## Array creation
    a = np.array([2, 3, 4])
    print(a.dtype)
    b = np.array([(1.5, 2, 3), (4, 5, 6)])
    print(b.dtype)

    # a = np.array(1, 2, 3, 4)  # WRONG
    # provide single sequence as an argument
    a = np.array([1, 2, 3, 4])  # RIGHT

    # array transforms sequences of sequences into two-dimensional arrays,
    # sequences of sequences of sequences into three-dimensional arrays, and so on.
    b = np.array([(1.5, 2, 3), (4, 5, 6)])
    print(b)
    c = np.array([[1, 2], [3, 4]], dtype=complex)
    print(c)

    # The function zeros creates an array full of zeros, the function ones creates an array full of ones,
    # and the function empty creates an array whose initial content is random and depends on the state of the memory.
    # By default, the dtype of the created array is float64, but it can be specified via the key word argument dtype.
    z = np.zeros((3, 4))
    print(z)
    x = np.ones((2, 3, 4), dtype=np.int16)
    print(x)
    print(x.ndim)
    y = np.empty((2, 3))
    print(y)

    # To create sequences of numbers, NumPy provides the arange function which is
    # analogous to the Python built-in range, but returns an array
    num_array = np.arange(10, 30, 5)
    print(num_array)
    float_array = np.arange(0, 2, 0.3)
    print(float_array)
    # When arange is used with floating point arguments, it is generally not possible to predict the number of
    # elements obtained, due to the finite floating point precision. For this reason, it is usually better to
    # use the function linspace that receives as an argument the number of elements that we want, instead of the step:
    n = np.linspace(0, 2, 9)
    print(n)
    x = np.linspace(0, 2 * np.pi, 100)
    f = np.sin(x)

    ### Printing Arrays
    # 1-d array
    a = np.arange(6)
    print(a)
    # 2-d array
    b = np.arange(12).reshape(4, 3)
    print(b)
    # 3-d array
    c = np.arange(24).reshape(2, 3, 4)
    print(c)
    # If an array is too large to be printed, NumPy automatically skips the
    # central part of the array and only prints the corners
    print(np.arange(10000).reshape(100, 100))
    # To disable this behaviour and force NumPy to print the entire array,
    # you can change the printing options using set_printoptions.
    np.set_printoptions(threshold=sys.maxsize)


    ### basic operations
    # arithmetic operators on arrays apply elementwise
    a = np.array([20, 30, 40, 50])
    b = np.arange(4)
    c = a - b
    d = b**2
    s = 10 * np.sin(a)

    A = np.array([[1, 1],
                  [0, 1]])
    B = np.array([[2, 0],
                  [3, 4]])
    C = A * B  # element wise
    print(C)
    D = A @ B # matrix multiplication
    D = A.dot(B)

    # Some operations, such as += and *=, act in place to modify an existing array rather than create a new one.
    rg = np.random.default_rng(1)
    a = np.ones((2, 3), dtype=int)
    b = rg.random((2, 3))
    a *= 3
    print(a)
    b += a
    print(b)
    # a += b  # b is not automatically converted to integer type -- ERROR
    # arrays of diff types
    a = np.ones(3, dtype=np.int32)
    b = np.linspace(0, np.pi, 3)
    print(b.dtype.name)
    c = a + b
    print(c)
    print(c.dtype.name)
    d = np.exp(c * 1j)
    print(d)
    print(d.dtype.name)
    # Many unary operations, such as computing the sum of all the elements in the array,
    # are implemented as methods of the ndarray class.
    a = rg.random((2, 3))
    print(a)
    print(a.sum())
    print(a.min())
    print(a.max())
    # By default, these operations apply to the array as though it were a list of numbers, regardless of its shape.
    # However, by specifying the axis parameter you can apply an operation along the specified axis of an array:
    b = np.arange(12).reshape(3, 4)
    print(b)
    print(b.sum(axis=0))  # sum column-wise
    print(b.min(axis=1))     # min of each row)
    print(b.cumsum(axis=1))  # cumulative sum along each row)

    # Universal Functions
    # NumPy provides familiar mathematical functions such as sin, cos, and exp.
    # In NumPy, these are called “universal functions” (ufunc).
    # Within NumPy, these functions operate elementwise on an array, producing an array as output.
    B = np.arange(3)
    print(B)
    print(np.exp(B)) # e^0, e^1, e^2
    print(np.sqrt(B))
    C = np.array([2., -1., 4.])
    print(np.add(B, C))
    #
    # all, any, apply_along_axis, argmax, argmin, argsort, average, bincount,
    # ceil, clip, conj, corrcoef, cov, cross, cumprod, cumsum, diff, dot, floor, inner, invert,
    # lexsort, max, maximum, mean, median, min, minimum, nonzero, outer, prod, re, round, sort, std,
    # sum, trace, transpose, var, vdot, vectorize, where

    ### Indexing, Slicing and Iterating
    # One-dimensional arrays can be indexed, sliced and iterated over, much like lists and other Python sequences.
    a = np.arange(10) ** 3  # 0^3, 1^3, 2^3, etc.
    print(a)
    print(a[2])
    print(a[2:5])
    # # equivalent to a[0:6:2] = 1000;
    # # from start to position 6, exclusive, set every 2nd element to 1000
    a[:6:2] = 1000
    print(a)
    print(a[::-1]) #  # reversed a
    for i in a:
        print(i ** (1 / 3.))

    def f(x, y):
        return 10 * x + y

    b = np.fromfunction(f, (5, 4), dtype=int)
    print(b)
    print(b[2, 3])
    ## each row in the second column of b
    print(b[0:5, 1] )
    print(b[:, 1]) # same as above
    # each column in the second and third row of b
    print(b[1:3, :])
    # When fewer indices are provided than the number of axes, the missing indices are considered complete slices:
    print(b[-1])   # the last row. Equivalent to b[-1, :])
    # The dots (...) represent as many colons as needed to produce a complete indexing tuple.
    # For example, if x is an array with 5 axes, then
    # x[1, 2, ...] is equivalent to x[1, 2, :, :, :],
    # x[..., 3] to x[:, :, :, :, 3]
    # x[4, ..., 5, :] to x[4, :, :, 5, :]
    c = np.array([[[0, 1, 2],  # a 3D array (two stacked 2D arrays)
                   [10, 12, 13]],
                  [[100, 101, 102],
                   [110, 112, 113]]])
    print(c.shape)
    print(c[1, ...])
    print(c[..., 2] )
    for row in b:
        print(row)
    # if one wants to perform an operation on each element in the array, one can use the flat attribute which is an
    # iterator over all the elements of the array
    for element in b.flat:
        print(element)

    ### shape manipulation
    # Changing the shape of an array
    a = np.floor(10 * rg.random((3, 4)))
    print(a)
    print(a.shape)
    # Note that the following three commands all return a modified array, but do not change the original array
    print(a.ravel())  # returns the array, flattened
    print(a.reshape(6, 2))
    print(a.T)   # returns the array, transposed
    print(a.T.shape)
    print(a.shape)
    print(a)
    print(a.resize((2, 6)))
    # If a dimension is given as -1 in a reshaping operation, the other dimensions are automatically calculated:
    print(a.reshape(3, -1))


    ### Stacking together different arrays
    a = np.floor(10 * rg.random((2, 2)))
    print(a)
    b = np.floor(10 * rg.random((2, 2)))
    print(b)
    print(np.vstack((a, b)))
    print(np.hstack((a, b)))
    # The function column_stack stacks 1D arrays as columns into a 2D array.
    # It is equivalent to hstack only for 2D arrays
    from numpy import newaxis
    np.column_stack((a, b))  # with 2D arrays
    a = np.array([4., 2.])
    b = np.array([3., 8.])
    c = np.column_stack((a, b))  # returns a 2D array
    print(c)
    d = np.hstack((a, b))
    print(d)
    e = a[:, newaxis]
    print(e)
    f = np.column_stack((a[:, newaxis], b[:, newaxis]))
    print(f)
    g = np.hstack((a[:, newaxis], b[:, newaxis]))  # the result is the same)
    print(g)
    # the function row_stack is equivalent to vstack for any input arrays. In fact, row_stack is an alias for vstack:
    print(np.column_stack is np.hstack)
    print(np.row_stack is np.vstack)

    ### Splitting one array into several smaller ones
    a = np.floor(10 * rg.random((2, 12)))
    print(a)
    h = np.hsplit(a, 3)
    print(h)



def matplotlibops():
    # matplotlib plot histogram
    rg = np.random.default_rng(1)
    mu, sigma = 2, 0.5
    v = rg.normal(mu, sigma, 10000)
    plt.hist(v, bins=50, density=True)
    plt.show()

    # box plot
    np.random.seed(seed=0)
    x = np.random.randn(1000)
    y = np.random.randn(100)
    z = np.random.randn(10)
    fig, ax = plt.subplots()
    ax.boxplot((x, y, z), vert=True, showmeans=True, meanline=True,
               labels=('x', 'y', 'z'), patch_artist=True,
               medianprops={'linewidth': 2, 'color': 'purple'},
               meanprops={'linewidth': 2, 'color': 'red'})
    plt.show()

    # histograms
    hist, bin_edges = np.histogram(x, bins=10)
    print(hist)
    print(bin_edges)
    fig, ax = plt.subplots()
    ax.hist(x, bin_edges, cumulative=False)
    ax.set_xlabel('x')
    ax.set_ylabel('Frequency')
    plt.show()

    # pie chart
    x, y, z = 128, 256, 1024
    fig, ax = plt.subplots()
    ax.pie((x, y, z), labels=('x', 'y', 'z'), autopct='%1.1f%%')
    plt.show()

    # bar chart
    x = np.arange(21)
    y = np.random.randint(21, size=21)
    err = np.random.randn(21)
    fig, ax = plt.subplots()
    ax.bar(x, y)
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    plt.show()

    # scatter plot
    import scipy
    x = np.arange(21)
    y = 5 + 2 * x + 2 * np.random.randn(21)
    slope, intercept, r, *__ = scipy.stats.linregress(x, y)
    line = f'Regression line: y={intercept:.2f}+{slope:.2f}x, r={r:.2f}'

    fig, ax = plt.subplots()
    ax.plot(x, y, linewidth=0, marker='s', label='Data points')
    ax.plot(x, intercept + slope * x, label=line)
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.legend(facecolor='white')
    plt.show()

# https://pandas.pydata.org/docs/getting_started/intro_tutorials/index.html
def pandasops():
    # A dataframe is a 2-D data structure that can store data of different types in columns
    # It is similar to a spreadsheet or SQL table
    # Each column in a dataframe is a series

    df = pd.DataFrame(
        {
            "Name": [
                "Braund, Mr. Owen Harris",
                "Allen, Mr. William Henry",
                "Bonnell, Miss. Elizabeth",
            ],
            "Age": [22, 35, 58],
            "Pincode": [76305, 43284, 98765],
            "Sex": ["male", "male", "female"],
        }
    )
    print(df)


    # Each column in a dataframe is a series
    print(df["Age"])

    # create a series from scratch
    newages = pd.Series([22, 35, 58], name="NewAge")
    print(newages)

    # get the maximum age of passengers
    print(df["Age"].max())

    # basic statistics about the dataframe
    # The describe() method provides a quick overview of the numerical data in a DataFrame.
    # As the Name and Sex columns are textual data, these are by default not taken into account by the describe() method.
    print(df.describe())

    # reading a file
    titanic = pd.read_csv("~/ibab-repo/titanic.csv")
    print(titanic)
    print(titanic.head(8))
    print(titanic.tail(8))
    print(titanic.dtypes)
    # save as xlsx
    import openpyxl
    titanic.to_excel("titanic.xlsx", sheet_name="passengers", index=False)

    # pandas supports many different file formats or data sources out of the box (csv, excel, sql, json, parquet, …),
    # each of them with the prefix read_*.
    titanic = pd.read_excel("titanic.xlsx", sheet_name="passengers")
    print(titanic)
    print(titanic.info())

    # selecting a subset of a dataframe
    print(titanic["Age"])
    print(titanic["Age"].shape)
    age_sex = titanic[["Age", "Sex"]]
    print(age_sex)
    print(age_sex.shape)

    # filter specific rows
    above_35 = titanic[titanic["Age"] > 35] # passengers older than 35 yrs
    class_23 = titanic[titanic["Pclass"].isin([2, 3])] # Titanic passengers from cabin class 2 and 3.
    # use of | and & operator
    class_23 = titanic[(titanic["Pclass"] == 2) | (titanic["Pclass"] == 3)] # same as above
    # passenger data for which the age is known
    age_no_na = titanic[titanic["Age"].notna()]
    print(age_no_na.shape)
    # selecting specific rows and columns
    # When using loc/iloc, the part before the comma is the rows you want, and the part after the comma is the columns you want to select.
    adult_names = titanic.loc[titanic["Age"] > 35, "Name"]
    # rows 10 till 25 and columns 3 to 5.
    print(titanic.iloc[9:25, 2:5])
    # assign the name anonymous to the first 3 elements of the fourth column
    titanic.iloc[0:3, 3] = "anonymous"

    ### plots in pandas
    import matplotlib.pyplot as plt
    # The usage of the index_col and parse_dates parameters of the read_csv function to define the
    # first (0th) column as index of the resulting DataFrame and convert the dates in the column to Timestamp
    # objects, respectively.
    air_quality = pd.read_csv("~/ibab-repo/air_quality_no2.csv", index_col=0, parse_dates=True)
    print(air_quality)
    # With a DataFrame, pandas creates by default one line plot for each of the columns with numeric data.
    air_quality.plot()
    plt.show()
    # plot only the columns of the data table with the data from Paris.
    air_quality["station_paris"].plot()
    plt.show()
    # scatter
    air_quality.plot.scatter(x="station_london", y="station_paris", alpha=0.5)
    plt.show()
    # ['area', 'bar', 'barh', 'box', 'density', 'hexbin', 'hist', 'kde', 'line', 'pie', 'scatter']
    # box plot
    air_quality.plot.box()
    plt.show()
    # each of the columns in a separate subplot. Separate subplots for each of the data columns are
    # supported by the subplots argument of the plot functions.
    xs = air_quality.plot.area(figsize=(12, 4), subplots=True)
    plt.show()

    ### create new columns derived from existing columns
    # To create a new column, use the [] brackets with the new column name at the left side of the assignment.
    # The calculation of the values is done element-wise. This means all values in the given column
    # are multiplied by the value 1.882 at once. You do not need to use a loop to iterate each of the rows!
    air_quality["london_mg_per_cubic"] = air_quality["station_london"] * 1.882
    print(air_quality.head())
    # ratio of the values in Paris versus Antwerp and save the result in a new column.
    air_quality["ratio_paris_antwerp"] = (air_quality["station_paris"] / air_quality["station_antwerp"])
    # rename the data columns to the corresponding station identifiers
    air_quality_renamed = air_quality.rename(columns={"station_antwerp": "BETR801",
                                                      "station_paris": "FR04014",
                                                      "station_london": "London Westminster"})
    print(air_quality_renamed.head())

    ### Summary statistics
    # average age of the Titanic passengers?
    print(titanic["Age"].mean())
    # Different statistics are available and can be applied to columns with numerical data.
    # Operations in general exclude missing data and operate across rows by default.
    # median age and ticket fare price of the Titanic passengers?
    print(titanic[["Age", "Fare"]].median())
    # diff stats
    print(titanic[["Age", "Fare"]].describe())
    print(titanic.agg({
                        "Age":["min", "max", "median", "skew"],
                        "Fare":["min", "max", "median", "mean"],
    })
    )

    ### groupby
    df = pd.DataFrame({'Animal': ['Falcon', 'Falcon', 'Parrot', 'Parrot'],
                       'Max Speed': [380., 370., 24., 26.]}
                      )
    m = df.groupby(['Animal']).mean()
    print(m)

    # average age for male versus female Titanic passengers?
    df_s = titanic[["Sex", "Age"]].groupby("Sex")
    print(df_s.mean())
    print(df_s.mean(numeric_only=True))
    print(df_s["Age"].mean())
    # mean ticket fare price for each of the sex and cabin class combinations?
    # Grouping can be done by multiple columns at the same time. Provide the column names
    # as a list to the groupby() method.
    df_sp = titanic.groupby(["Sex", "Pclass"])
    print(df_sp["Fare"].mean())

    ### Count number of records by category
    # number of passengers in each of the cabin classes?
    print(titanic["Pclass"].value_counts())

    ### reshape the layout of tables
    # sort the Titanic data according to the age of the passengers.
    titanic_sorted_age = titanic.sort_values(by="Age").head()
    print(titanic_sorted_age)

    # sort the Titanic data according to the cabin class and age in descending order.
    titanic_sorted_pclass_age = titanic.sort_values(by=['Pclass', 'Age'], ascending=False)
    print(titanic_sorted_pclass_age)

    ### combine data from multiple tables
    air_quality_no2 = pd.read_csv("~/ibab-repo/air_quality_no2_long.csv",parse_dates=True)
    air_quality_no2 = air_quality_no2[["date.utc", "location","parameter", "value"]]
    air_quality_pm25 = pd.read_csv("~/ibab-repo/air_quality_pm25_long.csv",parse_dates=True)
    air_quality_pm25 = air_quality_pm25[["date.utc", "location","parameter", "value"]]
    air_quality = pd.concat([air_quality_pm25, air_quality_no2], axis=0)
    print(air_quality)



    ### Join tables using a common identifier
    # merge
    df1 = pd.DataFrame({'a': ['foo', 'bar'], 'b': [1, 2]})
    df2 = pd.DataFrame({'a': ['foo', 'baz'], 'c': [3, 4]})
    df_inner = df1.merge(df2, how='inner', on='a')
    df_left = df1.merge(df2, how='left', on='a')
    df_right = df1.merge(df2, how='right', on='a')

    df1 = pd.DataFrame({'left': ['foo', 'bar']})
    df2 = pd.DataFrame({'right': [7, 8]})
    df_cross = df1.merge(df2, how='cross')



    stations_coord = pd.read_csv("~/ibab-repo/air_quality_stations.csv")
    print(stations_coord.head())
    print(air_quality.head())
    air_quality = pd.merge(air_quality, stations_coord, how="left", on="location")
    print(air_quality.head())

    ###
    air_quality_parameters = pd.read_csv("~/ibab-repo/air_quality_parameters.csv")
    print(air_quality_parameters.head())
    air_quality = pd.merge(air_quality, air_quality_parameters, how='left', left_on='parameter', right_on='id')
    print(air_quality)


def numpy_exercises():
    # credit: https://www.kaggle.com/code/themlphdstudent/learn-numpy-numpy-50-exercises-and-solution
    # Import numpy as np and see the version
    print(np.__version__)
    # How to create a 1D array?
    X = np.arange(10)
    # How to create a boolean array?
    np.ones((3, 3), dtype=bool)
    # How to extract items that satisfy a given condition from 1D array
    arr = np.arange(10)
    print(arr[arr % 2 == 1])
    # How to replace items that satisfy a condition with another value in numpy array
    # Replace all odd numbers in arr with -1
    arr = np.arange(10)
    arr[arr % 2 == 1] = -1
    # How to replace items that satisfy a condition without affecting the original array
    arr = np.arange(10)
    out = arr.copy()
    out[out % 2 == 1] = -1
    # How to reshape an array?
    arr = np.arange(10)
    print(arr.reshape(2, 5))
    # How to stack two arrays vertically?
    a = np.arange(10).reshape(2, -1)
    b = np.repeat(1, 10).reshape(2, -1)
    np.vstack([a, b])
    # How to stack two arrays horizontally?
    a = np.arange(10).reshape(2, -1)
    b = np.repeat(1, 10).reshape(2, -1)
    print(np.hstack([a,b]))
    # How to get the common items between two python numpy arrays?
    a = np.array([1, 2, 3, 2, 3, 4, 3, 4, 5, 6])
    b = np.array([7, 2, 10, 2, 7, 4, 9, 4, 9, 8])
    print(np.intersect1d(a, b))
    # How to remove from one array those items that exist in another
    a = np.array([1, 2, 3, 4, 5])
    b = np.array([5, 6, 7, 8, 9])
    print(np.setdiff1d(a, b))
    # How to get the positions where elements of two arrays match?
    a = np.array([1, 2, 3, 2, 3, 4, 3, 4, 5, 6])
    b = np.array([7, 2, 10, 2, 7, 4, 9, 4, 9, 8])
    print(np.where(a == b))
    # How to extract all numbers between a given range from a numpy array?
    a = np.array([2, 6, 1, 9, 10, 3, 27])
    print(a[(a >= 5) & (a <= 10)])
    #
    #  How to make a python function that handles scalars to work on numpy arrays?
    def maxx(x, y):
        """Get the maximum of two items"""
        if x >= y:
            return x
        else:
            return y

    def pair_max(x, y):
        # using zip
        maximum = [maxx(a,b) for a,b in zip(x,y)]
        return np.array(maximum)

    a = np.array([5, 7, 9, 8, 6, 4, 5])
    b = np.array([6, 3, 4, 8, 9, 7, 1])
    print(pair_max(a, b))

    # How to swap two columns in a 2d numpy array?
    arr = np.arange(9).reshape(3, 3)
    print(arr)
    new_arr = arr[:, [1, 0, 2]]
    print(new_arr)

    # How to swap two rows in a 2d numpy array?
    arr = np.arange(9).reshape(3, 3)
    new_arr = arr[[1,0,2], :]

    # How to reverse the rows of a 2D array?
    arr = np.arange(9).reshape(3, 3)
    print(arr)
    new_arr = arr[::-1, :]
    print(new_arr)

    # How to create a 2D array containing random floats between 5 and 10?¶
    rand_arr = np.random.uniform(5, 10, size=(5, 3))
    print(rand_arr)

    # How to print only 3 decimal places in python numpy array?
    rand_arr = np.random.random((5, 3))
    np.set_printoptions(precision=3)
    print(rand_arr)

    # How to pretty print a numpy array by suppressing the scientific notation (like 1e10)?
    np.random.seed(100)
    rand_arr = np.random.random([3, 3]) / 1e3
    np.set_printoptions(suppress=False)
    print(rand_arr)
    np.set_printoptions(suppress=True)
    print(rand_arr)

    # compute mean, median and standard deviation of a numpy array
    # How to normalize an array so the values range exactly between 0 and 1?  # (data - min)/(max - min)
    # How to filter a numpy array based on two or more conditions?
    iris_data = np.genfromtxt('~/ibab-repo/Iris.csv', delimiter=',', dtype='float', usecols=[1, 2, 3, 4],
                              skip_header=1)
    iris_data[(iris_data[:, 2] > 1.5) & (iris_data[:, 0] < 5.0)]

    # How to find the correlation between two columns of a numpy array?
    diabetes_data = np.genfromtxt('.~/ibab-repo/diabetes.csv',
                                  delimiter=',', dtype='float', usecols=[0, 1, 2, 3, 4, 5, 6, 7], skip_header=1)

    print(np.corrcoef(diabetes_data[:, 1], diabetes_data[:, 5]))

    print('\n')
    # you can get correlation by getting value at index [0,1] or [1,0]
    print(np.corrcoef(diabetes_data[:, 1], diabetes_data[:, 5])[0, 1])

    # How to find if a given array has any null values?
    # question: Find out if iris_2d has any missing values.
    diabetes_data = np.genfromtxt('../input/pima-indians-diabetes-database/diabetes.csv',
                                  delimiter=',', dtype='float', usecols=[0, 1, 2, 3, 4, 5, 6, 7], skip_header=1)

    np.isnan(diabetes_data).any()

    # How to replace all missing values with 0 in a numpy array?
    wine_quality = np.genfromtxt('~/ibab-repo/winequality-red.csv',
                                 delimiter=',', dtype='float', usecols=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
                                 skip_header=1)

    wine_quality[np.random.randint(len(wine_quality), size=20), np.random.randint(11, size=20)] = np.nan

    print("Does dataset have any Nan value:", np.isnan(wine_quality).any())

    wine_quality[np.isnan(wine_quality)] = 0

    print("Does dataset have any Nan value:", np.isnan(wine_quality).any())

    # How to find the count of unique values in a numpy array?
    mushroom = np.genfromtxt('../input/mushroom-classification/mushrooms.csv',
                             delimiter=',', dtype=object, usecols=[0], skip_header=1)
    # mushroom
    np.unique(mushroom, return_counts=True)

def pandas_exercises():
    import datetime

    df_data = pd.read_json("~/ibab-repo/ODI-Batting_Cricket_Analytics.json")
    print(df_data.shape)

    # What is the year range when all matches were played?
    df_match_date = pd.to_datetime(df_data['MatchDate'], dayfirst=True)
    print(f"Starting year {df_match_date.min()} , Ending year {df_match_date.max()}")

    # How many matches does India play?
    df_data_india = df_data[df_data["Country"] == "India"]
    num_matches = len(df_data_india)
    print("Number of India matches = ", num_matches)

    # How many matches does India play after year 2000?
    df_match_date = pd.to_datetime(df_data['MatchDate'], dayfirst=True)
    date_2000 = pd.to_datetime('1/1/2000')
    df_data_india_2000 = df_data[(df_data["Country"] == "India")  & (df_match_date > date_2000)]
    num_matches = len(df_data_india_2000)
    print("Number of India matches after the Year 2000 = ", num_matches)

    # who is the top scorer for India in the year 2010
    df_match_date = pd.to_datetime(df_data['MatchDate'], dayfirst=True)
    start_date = pd.to_datetime('1/1/2010')
    end_date = pd.to_datetime('1/1/2011')
    df_matches = df_data[(df_data["Country"] == "India") & (df_match_date > start_date ) & (df_match_date < end_date)]
    num_matches = len(df_matches)
    print("Number of India matches = ", num_matches)
    df_player_scores = df_matches.groupby(["Player"])["Runs"].sum()
    print(f"Player {df_player_scores.idxmax()}, Total Runs {df_player_scores.max()}")

    # List the top 5 scorers in the year 2010
    df_match_date = pd.to_datetime(df_data['MatchDate'], dayfirst=True)
    start_date = pd.to_datetime('1/1/2010')
    end_date = pd.to_datetime('1/1/2011')
    df_matches = df_data[(df_match_date > start_date ) & (df_match_date < end_date)]
    num_matches = len(df_matches)
    print("Number of matches = ", num_matches)
    df_player_scores = df_matches.groupby(["Player"])["Runs"].sum()
    s_sorted = df_player_scores.sort_values(ascending=False)
    print("Top 5 players")
    print(s_sorted.head())

    # check

    # What is the average score of each Indian player played in the year 2010
    df_match_date = pd.to_datetime(df_data['MatchDate'], dayfirst=True)
    start_date = pd.to_datetime('1/1/2010')
    end_date = pd.to_datetime('1/1/2011')
    df_matches = df_data[(df_data["Country"] == "India") & (df_match_date > start_date ) & (df_match_date < end_date)]
    num_matches = len(df_matches)
    print("Number of India matches = ", num_matches)
    df_player_scores = df_matches.groupby(["Player"])["Runs"].mean()
    print(df_player_scores)

    # how many matches India played against each country in the year 2010
    df_match_date = pd.to_datetime(df_data['MatchDate'], dayfirst=True)
    start_date = pd.to_datetime('1/1/2010')
    end_date = pd.to_datetime('1/1/2011')
    df_matches = df_data[(df_data["Country"] == "India") & (df_match_date > start_date) & (df_match_date < end_date)]
    df_india_matches = df_matches.groupby(["Versus"])
    print(df_india_matches['Versus'].value_counts())

def stats():
    # credit: https://scipy-lectures.org/packages/statistics/index.html
    # The MRI Scans were performed at the same facility for all 40 subjects. The scans
    # consisted of 18 horizontal MR images. The computer counted all pixels with
    # non-zero gray scale in each of the 18 images and the total count served as an
    # index for brain size.
    # 1.Gender: Male or Female
    # 2.FSIQ: Full Scale IQ scores based on the four Wechsler (1981) subtests
    # 3.VIQ: Verbal IQ scores based on the four Wechsler (1981) subtests
    # 4.PIQ: Performance IQ scores based on the four Wechsler (1981) subtests
    # 5.Weight: body weight in pounds
    # 6.Height: height in inches
    # 7.MRI_Count: total pixel Count from the 18 MRI scans
    df_data = pd.read_csv('~/ibab-repo/brain_size.csv', sep=';', na_values=".")
    print(df_data)

    # What is the mean value for VIQ for the full population?
    m = df_data["VIQ"].mean()
    print(m)

    # How many males/females were included in this study?
    gender_group = df_data.groupby('Gender')
    print(gender_group.count())

    # How many males/females were included in this study?
    gender_group = df_data.groupby('Gender')
    print(gender_group["VIQ"].mean())

    # What is the average value of MRI counts expressed in log units, for males and females?
    print(np.log2(gender_group["MRI_Count"].mean()))

    # plots - pd.plotting is using matplotlib behind the scene
    pd.plotting.scatter_matrix(df_data[['Weight', 'Height', 'MRI_Count']])
    plt.show()
    pd.plotting.scatter_matrix(df_data[['PIQ', 'VIQ', 'FSIQ']])
    plt.show()

    # Plot the scatter matrix for males only, and for females only.
    # Do you think that the 2 sub-populations correspond to gender?
    df_data_male = df_data[df_data["Gender"] == "Male"]
    pd.plotting.scatter_matrix(df_data_male[['Weight', 'Height', 'MRI_Count']])
    plt.show()
    pd.plotting.scatter_matrix(df_data_male[['PIQ', 'VIQ', 'FSIQ']])
    plt.show()

    from scipy import stats
    # Hypothesis testing - null hypothesis - no difference hypothesis - if p < 0.05 reject null hypothesis
    # This is a test for the null hypothesis that the expected value (mean) of a
    # sample of independent observations a is equal to the given population mean, popmean.
    print(stats.ttest_1samp(df_data['VIQ'], 0) )

    # mean VIQ in the male and female populations were different. Are they significant?
    # null hypothesis = not significant
    female_viq = df_data[df_data['Gender'] == 'Female']['VIQ']
    male_viq = df_data[df_data['Gender'] == 'Male']['VIQ']
    # Calculate the T-test for the means of two independent samples of scores.
    print(stats.ttest_ind(female_viq, male_viq) )

    # PIQ, VIQ, and FSIQ give 3 measures of IQ. Let us test if FISQ and PIQ
    # are significantly different. We can use a 2 sample test:
    print(stats.ttest_ind(df_data['FSIQ'], df_data['PIQ']))

    # correlation coeff
    x = df_data["VIQ"]
    y = df_data["PIQ"]
    import scipy
    r, p = scipy.stats.pearsonr(x, y)
    print(r, p)
    corr_matrix = np.corrcoef(x, y)
    print(corr_matrix)
    print(scipy.stats.linregress(x, y))





def main():
    # numpyops()
    pandasops()
    # numpy_exercises()

    # pandas_exercises()
    # stats()
    # matplotlibops()




# Construct to not include whole program in other includes
if __name__ == "__main__":
    main()