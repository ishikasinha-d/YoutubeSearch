# YoutubeSearch

# About the Project
An API to fetch latest videos sorted in reverse chronological order of their publishing date-time from YouTube for a given tag/search query in a paginated response.

![Screenshot (84)](https://user-images.githubusercontent.com/69107978/142735730-87be496d-34f9-4b9a-bef3-4efbf6ad24d0.png)


# Basic Requirements:
- Server should call the YouTube API continuously in background (async) with some interval (say 10 seconds) for fetching the latest videos for a predefined search query and should store the data of videos (specifically these fields - Video title, description, publishing datetime, thumbnails URLs and any other fields you require) in a database with proper indexes.
- A GET API which returns the stored video data in a paginated response sorted in descending order of published datetime.
- A basic search API to search the stored videos using their title and description.

# To run the server
- Clone the repository
- Use requirements.txt file to create environment (Platform: Windows) using: 
  
  `conda create --name <env> --file <this file>`
 
 - create .env file and write the following information inside 
 
   `API_KEY=<your api>`
   
   `MONGO_URI=<your connection string>`
  
  To get the API:
  1. Create a project on google cloud platform
  2. Enable YOUTUBE DATA API
  3. Create API Credentials 

  To get connection string:
  1. Create account on MongoDB Atlas
  2. Create a Project-> MongoDB cluster
  3. Create a user and collection
  4. Click on connect to get the string. Put your username, user's password and database in the connection string.

- Run the flask app using: 

`flask run`

  
