import sqlite3 as lite
import pandas as pd

while(1):
    con=lite.connect('user.db',timeout=1)

# Select all rows and print the result set one row at a time
with con:
    
    cur = con.cursor()
    cur.execute("DROP TABLE IF EXISTS cities_copy")
    cur.execute("DROP TABLE IF EXISTS weather_copy")
    cur.execute("CREATE TABLE weather_copy (City text, Year integer, Warm_Month text, Cold_Month text, Average_Temp integer)")
    cur.execute("CREATE TABLE cities_copy (name text, state text)")
    cur.execute("INSERT INTO cities_copy VALUES('Washington', 'DC')")
    cur.execute("INSERT INTO cities_copy VALUES('Houston', 'TX')")
    cur.execute("INSERT INTO weather_copy VALUES('Washington', 2013, 'July', 'January', 62)")
    cur.execute("INSERT INTO weather_copy VALUES('Houston', 2013, 'July', 'January', 76)")
    #cur.execute("SELECT * FROM cities")

with con:

    cur = con.cursor()
    cur.execute("SELECT * FROM cities_copy INNER JOIN weather_copy on name=city")

    rows = cur.fetchall()
    cols = [desc[0] for desc in cur.description] # to get column names
    df = pd.DataFrame(rows, columns=cols) # this puts the output of select statement in a pandas dataframe.
    #for row in rows:
    print "The cities that are warmest in July are {} ".format(df['name'].to_json())
        
