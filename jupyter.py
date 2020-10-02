#To run Jupyter (later in the course), you need to open an "Anaconda Prompt" 
#(from Start Menu) and type >jupyter notebook

# Markdown cell type

#creating heads with #:
# this is a markdown cell
## this is heading two
### this is heading three

#creting bullets with *:
# * blue fish
# * green fish 

# **to render the text bold**
# *to render the text italic*

# you can create equations using LaTeX equations.
# LateX is a document editing language,
# which has a syntax for many text components for scientific writing
# $\int_0^\infy x^{-\alpha}$

# What if you really would like to save
# a non-executable version of the Notebook
# and keep it in your archives?
# download as html or 

# Kernel is the whole notebook (Jupyter file in new tab)
# the cells are the subparts of the Kernel
# (where we run our codes)


# we can use Unix code in the Python Kernel:
#just need to start with "!"

#Pandas 

# https://courses.edx.org/courses/course-v1:UCSanDiegoX+DSE200x+1T2020/courseware/6712a4facbe14a36a7a2449ea18f7a55/eb8f1bc97beb4bdfa289840749791f68/?child=first

# Video: Live Code, Why Pandas 

# difference between functions: 
# dataFrame.pop("three")  -> return the "three" column
# del dataFrame("three") -> only deletes it, no return
#--> 	You can store a popped column.

# pandas: Data Ingestion

#One of the most popular data formats
#is comma separated values, or shortly csv.

#JSON, or java script object notation,
#is a format for structuring data
#and it's commonly used for communication
#within web applications.

#Html, is a hyper text markup language,
#and it's a file format used as the basis of every webpage.

#Sequel, or SQL, stands for structured query language.
#SQL is used to communicate with a database using queries
#to insert, delete, and select data of interest.

# ps: we can use UNIX notation in the Jupyter Kernel (Python)

#♣DataFrame functions:
#d.head()
#d.head(15)
#d.index
#d.columns
# d.iloc[[0,11,2000]] #returns values associated with list of indexes (rows)

#Pandas: Descriptive Statistics
#your favorite statistical operation,
#like max, min, mode, and median, (mean, std, any, all, count, clip, rank, round)
#and you'll find that function in Pandas.
#

#pd.DataFrame.corr()
#So as you would remember a negative correlation score,
#here means those features in our data sets
#are inversely correlated, so one go up one goes down,"

#Video: Pandas, Data Cleaning

# pd function to fill NaN:
#data.fillna("method=ffil") #replace NaN by the previous value
#data.fillna("method=backfil") #replace NaN by the next value

#data.dropna()
#will drop any row or column with a missing value in the DataFrame.
#data.dropna(axis=0) #dropping rows #col direction (passing through rows) 
#data.dropna(axis=1) #dropping cols #row direction (passing through cols) 

#data.interpolate()
#The default for interpolate function is a linear interpolation, meaning 
#that the method tries to fit the NaN values to occur over line using linear polynomials,

# So if you want Jupyter to plot the graphs
# inside the notebooks we'll have to tell Jupyter
# to plot inline as we see here:

# %matplotlib inline










