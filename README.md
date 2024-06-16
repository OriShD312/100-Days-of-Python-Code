This repository is a culmination of most of the projects I have created during my 100 Days of Code course from Udemy.

Each day of the course introduced a new challenge that required us to use the tools we learned from previous days with a combination of online research to overcome.

Day 45:
- intro to Beautiful Soup.
- use bs4 to web scrape the top 100 movies of all time.

Day 56:
- create a website using the Flask framework + learn to copy web templates and customize them to create a Name Card webpage that includes links to your social media.

Day 57:
- learn to use Jinja, a part of the Flask framework, to create more complex webpages using Python instead of JavaScript.

Day 58:
- learn about Bootstrap, a CSS framework that contains multiple classes that allow for easier HMTL elements customization.
- create a website that utilizes certain Bootstrap elements for a fictional app.

day 59:
- use the tools from the previous days to improve the blog project from day 57.
- add a sticky header.
- make a functional about and contact pages.
- restructure the code to use Jinja for all the passing and loading of parameters to the HTML.

Day 60:
- learn how to create a use Flask and HTML forms using Jinja.
- learn about POST and GET methods for updating and interacting with web pages.
- use smtplib library to send an email from the contact page.

Day 61:
- learn about WTForms, an easier way to create and generate forms between Python and HTML.

Day 62:
- create a website that uses WTForms to allow users to add their favorite coffee shops with parameters for WiFi, Coffee and Outlet rating.

Day 63:
- first introduction to SQLite, the most popular database tool used all over the world. Uses very specific string commands that are prone to typos.
- introduction to SQLAlchemy, an ORM (Object Relational Mapping) library that uses Python code to interact with SQLite. This minimizes typos since the compiler is able to actually read the code and spot errors.
- the introduction of these tools taught us how to save entries beyond the initial run of the server that we are hosting.
- the project was to create a virtual library. The website would allow users to add and rate the books they'be read, the homepage will then display all the books added to the library and sort them by rating.

Day 64:
- the project of this day was similar to the one where we allowed users to add the books they read (day 63), this time the library contains movies instead.
- this project required us to use the combination of the tools from the previous days:
  - Bootstrap for info cards to display each movie entry.
  - SQLite to save the entries for future visits.
  - WTForms to fill in the info about the movie and also to edit certain entries. There is also an option to delete entries from the database in case the user wishes to.
  - Jinja to pass through parameters from Python to HTML for displaying the movie info.
  - use an API to fetch possible movies that answer to the title inputted by the user to make they are adding the actual movie they meant for.

Day 65 mainly focused on good and bad practices of User Experience (UX), the project was to create a template for a website using Canva based on those practices

Day 66:
- taught how to build our own API using RESTful routing. This was a very similar experience to creating a website since we still used the Flask framework.
- unlike a website, we did not load HTML pages, we simply returned results according to users requests.
- our API included the following actions:
  - GET random entry
  - GET all entries
  - GET entry based on location sent by user
  - POST new entry to database
  - PATCH to update one of the parameters of an existing entry
  - DELETE an entry from the database
- we learned about Postman, a website/app that allows us to create scenarios to test our API. One of it's many advantages is that it allows us to create documentation for our API in the app and then post it to their website.

Day 67:
- we tranlated the knowledge of the REST API from the previous day to update our blog, this allowed users to see current blog posts (GET), create new blog posts (POST), edit existing posts (PUT) and finally delete posts (DELETE).

Day 68:
- we leanred about authentication, salting and hashing of passwords to create a more secure database where our users data is more protected from unwanted guests.
- using the Wekzeug library we used a method to hash and salt user passwords when they signed up and also used their built-in method to check a users password when they login compared to what is in the database.
- we used Flask's Flash messages to write messages to users when they entered incorrect credentials.

Day 69:
- we made the final update to our blog project by adding a user, blog, and comment databases.
- the very first user in the database was automatically assigned as the admin for the website, this made them the only person able to create/edit/delete blog posts.
- we used the One-to-Many relation to connect between the users, blog posts, and comments. This allowed us to keep tracking of who posted which comment on which blog post.
- the main challenge for me was understanding how to esablish and use the relationships between all these databases.

Day 70:
- introduction to Git and GitHub for version control.
- Git is a tool used to create snapshots of our work, these snapshots are points in time we can return to in case our code became suddenly broken and we are unsure why
- Git can be used by a single person to keep track of their work but it is more popularly used as a tool to support multiple people working on the same project.
- GitHub is one of the platforms that allow users to host their work in private of public places called repositories. Public repositories can be worked on by multiple people who each contribute their part or wish to make changes to the original code for their own use.
- the beauty of Git is not only in allowing us to create snapshots, it also allows us to create multiple branhces where us or other people can make experiments on the original code without breaking the main repository.

Day 71:
- after learning about Git and GitHub, we used a service that allows us to connect a repository we created and host our own website using their servers.

Day 72:
- this was the first of many days where we learned to use the Google Collab platform. This is similar to using an IDE with the added benefit being that multiple people can work on the same file together and also being able to run specific cells of code.
- using the pandas library in order to load and manipulate csv files to try and make deductions based on available data by finding new and interesting connections between columns and entries that might not be as obvious as before we started.
- the very first step we focused on was cleaning the data from incomplete and duplicate entries.
- then we learned how to access specific entries using pandas data frame methods such as 'loc', 'idxmax', 'idxmin' and so on.
- next was how to make operations between columns in the data frame such as subtracting between two and how to insert new columns.
- used groupby to find interesting connections between columns, in the example of this day, we used it to find the average amount of graduates per field: STEM, HASS, Business.

Day 73:
- a continuation of day 72, we learned how to convert strings to datetime objects using a built-in method of pandas.
- used the pivot method to reshape our data frame and create a new table where a certain column is now used as an index to separate entries instead. This creates a new way to look at the data possibly leading to new conclusions.
- used the plotly library to display graphs of the data creating a visual represntation and making it easier to understand.
- customized the graph to make it more readable and to emphasize certain elemnts.
- used the rolling and mean method to smooth the graph making it clearer and with less extreme results that might not represent the bigger picture or might distract from a forming trend.

Day 74:
- used groupby together with count to aggregate and sum data
- learned about the value_counts method which is very useful to find prominent repetitions of a specific column entry.
- learned about the agg method that is used to run an operation on all entries of a column.
- used rename to change/update column names.
- created a plot with 2 lines that share a single axis while having their other axis adjusted to their scale, for example, one column has values between 1-100 while the other has 100,000-1,000,000.
- created a scatter plot and bar chart using the Matplotlib library.
- used the merge method to combine databases based on a shared column, finding overlaps between data frames.

Day 75:
- used the describe method to quickly analyze our data frame for NaN values.
- used the resample method to make 2 different data frames that use different dating methods hold comparable time series data. One dataframe held days and the other months, we used this method to make both data frames monthly.
- used matplotlib.dates to add ticks to our axis making it clearer where each entry point is.
- customizing the graph by changing: dpi (resolution), line styles, markers, axis limits, labels, line width, colors and showing a grid over the graph.

Day 76:
- how to pull a random sample.
- how to find and remove duplicates.
- converting strings to a numeric object that allows for mathematical operations.
- using plotly to generate pie, box, scatter, bar and donut (a pie with a hole) charts.

Day 77:
- creating n-dimensional arrays (ndarrays) with numpy.
- analysing shape of ndarrays.
- how to select parts of an array using slicing.
- how to perform linear algebra operations with scalars such as addition and multiplication.
- matrix multiplication.
- how an ndarray can be translated to an image using imshow.

Day 78:
- how to use nested loops to remove unwanted characters from multiple columns. We had columns with a $ symbol and a comma to separate each thousand ($1,000,000) and we wanted to transform the column to an numeric object.
- using the query method to filter specific results out of our data frame.
- using the Seaborn library to create bubble charts (scatter plot) that show an entry's contribution based on the size of its bubble.
- customizing the bubble chart.
- creating a combination of a bubble chart with a linear regression line using the regplot method from Seaborn.
- learning how to use the scikit library's linear regression module to generate our own linear regression line and displaying it, the added benefit being able to show the coefficients, intercept point and the score of the regression (how well it fits the data).

Day 79:
- we worked on a csv file with multiple columns that contained data on Nobel prize winners.
- columns: year, category, prize, motivation, prize_share, laureate_type, full_name, birth_date, birth_city, birth_country, birth_country_current, sex, organization_name, organization_city, organization_country, ISO.
- another more in depth dive to value_counts, groupby, merge, sort_values and agg methods from pandas.
- using plotly.express's Choropleth to display data on a map of the world.
- creating plotly.express's Sunburst graph that displays data in a beatiful way with multiple layers of connection between columns.
- using Seaborn's lmplot to show multiple regression lines using the row, hue and lowess parameters.
- notice the different conclusions that can be reached when looking at the data using different plots such as box plots compared to time series plots.
- using histogram to visualise the distribution of data and gain a more statistic oriented point of view.

Day 80:
- worked on a csv file containing data collected by Dr. Semmelweis regarding mortality rate in pregnancies in the 1800s and how they were affected by his introduced handwashing policy.
- yearly csv columns: year, births, deaths, clinic.
- monthly csv columns: date, births, deaths.
- used histograms to see distribution of data.
- how to plot multiple histograms on top of each other even when they contain data of different lengths.
- used Kernel Density Estimates (KDEs) to visualise a smoother form of a histogram. Improved the KDE by specifying boundries.
- used scipy.stats library's ttest_ind to calculate the p-value and t stat of the handwashing experiment run by Dr. Semmelweis.

Day 81:
- worked with csv file containing data about housing prices in the 1970s in the Boston area.
- columns: CRIM, ZN, INDUS, CHAS, NOX, RM, AGE, DIS, RAD, TAX, PTRATIO, B, LSTAT, PRICE.
- learned to use Seaborn's pairplot to make an initial assessment about relationships in the data.
- learned how to use the train_test_split method from the sklearn library to create data sets for training and testing.
- learned how to run a multivariable linear regression model and evaluate its performance using the data sets created.
- learned to use logic to determine connection between a feature and its calculated coefficient, i.e., if a feature is meant to contribute in a positive way to the target value, make sure it has a positive sign.
- used residuals (distances of calculated values from the true values) to find patterns that might hint at an issue with our regression model.
- learned how using a log on the data might improve the regression model. This is just one of many possible manipulations to data that can be applied, the advantage is that it dramatically shrinks the distance between the minimal and maximal values.
- finally, applied the regression model using our own values to predict a house price.

Day 82:
- we were tasked with creating a text to Morse code translater.
- the task was for a simple CMD line program, I personally decided to use tkinter to create GUI that will make it more accessible to users who are not used to using CMD.
- I applied the use of threading to allow for continued use of the application while it performs the translation. This means that a user can type their word or sentence, start the translation and while it is running start typing a new sentence.
- I used a Windows library that produces sound based on set frequency and duration.
- I applied the rules stated in the wikipedia page for Morse code in terms of length of dits, dahs, the delay between letters and the delay between words.
- I created a json file that contains all letters A-Z and all digits 0-9 with their corresponding Morse code translation and then used their patterns to translate to dits and dahs accordingly.
- the program displays the current letter being translated along with its Morse code represntation.

Day 83:
- the task was to create a portfolio website, I intend to complete this after I have completed a few other projects that I can proudly display in it.

Day 84:
- the task was to create a Tic Tac Toe game in CMD that allowed users to compete.
- I completed the task using tkinter again, I did struggle a bit with finding the most optimal way to check for winners but I managed to find a solution I am happy with.
- I did make the game a bit more customizable by giving the option to set a board bigger than 3x3, making games longer and more challenging.

Day 85:
- the task is to create an image watermarking desktop app that has GUI.
- I started this task but still haven't finished.
- I decided to also add a background removal feature that I found can be easily implemented using an existing Python library.
- my biggest challenge was using the FontDialog widget from ttkbootstrap, it appears to have a bug in it that causes a change to font whether a user presses OK, Cancel or even simply closes the FontDialog window.
- this issue forced me to finally turn to the course Discord channel where I found much needed and very kind help, I also finally created a StackOverflow account and even posted my own question!
- I am very happy with the current progress of this day even though the task is yet to be completed.
