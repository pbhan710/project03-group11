# project03-group11
Repository of code and supporting documentation for project.
(not done yet, will finish writing/editing in morning - ramya)

Contributers: Paul Han, Nivedha Raja, Corine Alida Daboiko, Krishna Musunuri, and Marquesia Atwater

## Before You Begin
Please download The Movies Dataset at Kaggle and store this in a "Data" sub-repository of the project. This data can be accessed via .csv files as well as through it's online API. This dataset includes contain metadata for 45,000 movies all listed in the Full MovieLens Dataset. For the purposes of this project we chose to only showcase data pertaining to the last decade. Data points include cast, crew, plot keywords, budget, revenue, posters, release dates, languages, production companies, countries, TMDB vote counts and vote averages. 
 
## Project Description
We were inspired to embark on this project upon learning that two of our group members are relatively uncultured when it comes to pop culture that stems from movies and films. With limited knowledge of recent popular movies and actors, we sought to create a website that would easily display the top 10 actors and directors from a database of relevant movies. We would also display a timeline detailing their career and filmography on the same page with the cooresponding actors and directors.

In order to incorporate all of these elements and given the nature of the file types we had access to, we decided to combine a multitude of web development tools including HTML, CSS, JavaScript, Jupyter Notebook, Python, Flask, SQLAlchemy, and SQL. We sought to accomplish the following wire frame with our project implementation: 

<p align="center">
    <img src = "https://github.com/pbhan710/project03-group11/blob/main/Wireframe_Code.png " width=50% height=50%>
 </p>

We also created a wireframe of what we hoped our website would resemble:

<p align="center">
    <img src = "https://github.com/pbhan710/project03-group11/blob/main/Wireframe.png " width=50% height=50%>
 </p>

## Back-End Programming

Whilst creating our website, we started by first understanding the API, which contained our data, and learning it's proper documentation. We then filtered our query results of what timeframe of movies we wanted access to.  Given that there were 45,000 movie data entries in our dataset, we narrowed down our data based on the following parameters: 
- Movies released within the time frame of January 2013 to January 2023 (Resulted in pages 1-500)
- Movies only released in English language
- Movies that adhered to a relatively high popularity rating (In other words, movies that were not relatively well-known were not considered)

We then requested the filtered data by making calls to TMDB's APIs to retrieve and store data into lists. Then at the end of the query, we verified the total number of movies. 

Once our data was filtered down based on these parameters, it was reduced to a dataset with _____ individual movie datapoints. We then used Jupyter Notebook and python to sort our results based on actors, directors, and movies, and load those into individual dataframes. These dataframes were then exported as three separate .csv files for easy upload into a SQL database. 

We used PGAdmin to connect to the local Postgres database and store movies, directors, and actors into the respective tables. Tables within the local Postgres database should already be created before attempting. In order to create a design for the data we wanted stored, we created schemas - a user schema and a reviews schema. This ensured that the user was not already stored in the database in addition to hashing the stored password after using a virtual field to check that the original password matched the password confirmation. The layout of our data within our SQL database resembles the following ERD diagram:

<p align = "center">
  <img src="https://github.com/pbhan710/project03-group11/blob/main/ERD.png ">
 </p>
   
Then we queried the information we wanted from our database using routes via SQLAlchemy in Flask. These routes returned jsonified versions of our results that were then read by our JavaScript file using the d3 library. 

The queried results would return information illustrating a top ten list of the top movies, directors, and actors from the dataset. Then after reading the jsonified results, we displayed this information on our website in HTML. Also occuring at the same time, a different JavaScript library, [TimeKnots](https://github.com/alangrafu/timeknots), organized the cooresponding actor or directors filmography on a timeline and displayed it next to them. 

Finally, our website is being run through our Flask app.py at the end. 

## How to Install and Run the Project

Provide a step-by-step description of how to get the development environment set and running.
Set up:  
- Create a Google Cloud Storage Bucket 
- Download json private key for a Service Account and have it available 
- Set an environment variable : export GOOGLE_APPLICATION_CREDENTIALS=path/to/your-key.json
 
### API Documentation Basics
Here are a few basic details to help better understand the structure of the API
#### URL's
- discover_base_url
    - Base URL of TMDB's Discover API to search movies by different types of data. This includes the API key.
- movie_base_url
    - Base URL of TMDB's Movie API to search details of a specific movie by ID.
- discover_target_url
    - Full URL of TMDB's Discover API which includes TMDB properties to filter movies by. 
    - Example URL: https://api.themoviedb.org/3/discover/movie?api_key=%7Bapi_key%7D&release_date.gte=2010-01-01&release_date.lte=2010-01-31%C2%AEion=us&with_release_type=2%7C3&vote_count.gte=1&sort_by=popularity.desc&page=1
- movie_target_url
-   Full URL of TMDB's Movie API which includes the TMDB movie. 
-   Example URL: https://api.themoviedb.org/3/movie/550?api_key=%7Bapi_key%7D
#### TMDB Properties
- release_date.gte={release_start_date}
    - Earliest date of movies' release dates to search for using TMDB's Discover API.
- release_date.lte={today}: Latest date of movies' release dates to search for using TMDB's Discover API.
#### Other
- today
    - Today's date.
#### Hard-Coded TMDB URL Properties:
- region=US: ISO 3166-1 code to filter movies' release dates by. Set specifically to US.
- with_release_type=2|3: Type of releases. 2|3 pulls movies with theatrical releases.
- vote_count.gte=1: Minimum number of votes by TMDB users on movies to search for in TMDB's Discover API. Set to 1 to exclude movies with 0 votes, reducing overall search results.
- sort_by=popularity.desc: Sort movies pulled through TMDB's Discover API by TMDB's popularity metric among TMDB users, descending.
- append_to_results=credits: Add to the result of an API call more details. This is used when making an API call to TMDB's Movie API to also add details on the cast/crew of the movie.



## How to Use the Project
Provide instructions and examples so users/contributors can use the project.
Users are able to query or request information from our Database.
For instance, if one would like to learn about the top 10  movies for 2013-01-01 to 2023-01-14, they can pull it from the movies_lst by using movie “id”or “title” and “popularity”.

### Challenges
Some of the challenges we faced and features we hope to implement in the future:
- Too many pages and API could not run using Jupyter Notebook (had to use Visual Code )
- While working on our Javascript using the Twitter Feed, we could not get a live feed. We have to search for Twitter documentation on it.

### Acknowledgements
This dataset is an ensemble of data collected from TMDB and GroupLens.

The Full MovieLens Dataset consisting of 26 million ratings and 750,000 tag applications from 270,000 users on all the 45,000 movies in this dataset can be accessed [here](https://www.kaggle.com/datasets/rounakbanik/the-movies-dataset)

The Movie Details, Credits and Keywords have been collected from the TMDB Open API. This product uses the TMDb API but is not endorsed or certified by TMDb. Their API also provides access to data on many additional movies, actors and actresses, crew members, and TV shows. You can try it for yourself here.

The Movie Links and Ratings have been obtained from the Official GroupLens website. The files are a part of the dataset available [here](https://www.kaggle.com/datasets/rounakbanik/the-movies-dataset)Other Sources


