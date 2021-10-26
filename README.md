# Teradata Database for Python
This package is a Teradata wrapper for [sqlalchemy](https://www.sqlalchemy.org/). This allows an easy integration from Python with Teradata.

## Installing the package using PIP
This python package can be installed through pip. Check if your machine is configured to install through the command line/terminal by:
1. Open command line/terminal
2. Enter the following:
```
python -m pip --version
```
If the version number displays, this package may be installed through command line.
If not, recommendation is to [add python to PATH](https://datatofish.com/add-python-to-windows-path/).
<br/>
To install the package, type the following within command line/terminal:
```
python -m pip install git+https://dev.azure.com/AmericanGreetings/Analytics/_git/teradata_database
```

## Using the package to connect to Teradata
This package may be imported into your script through the following:
```
from teradata_database import TeradataDatabase
```
Once imported, create a variable to hold the connection that supplies the host, username, and password to establish the connection. Replace with your credentials:
```
db = TeradataDatabase("<host>", "<username>", "<password>")
```
The database connection can utilize the *with* statement if desired:
```
with db as conn:
    results = conn.engine.execute("<SQL STATEMENT>").fetchall()
```
Or use without *with*:
```
sql = '<SQL STATEMENT>'

results = db.engine.execute(sql).fetchall()
```

### Using with pandas
This package may be used with pandas to fetch results in dataframe format. To do so, use the following:
```
import pandas as pd

with db as conn:
    df = pd.read_sql("<SQL STATEMENT>", conn.engine)
```

### Using with dask
This package may also be used with dask dataframe. To do so, reference the following as an example. Dask needs the URI for the connection so it is slightly different than interactions above:
```
import dask.dataframe as dd

ddf = dd.read_sql_table("<SCHEMA>.<TABLE>", uri=db.uri)
```