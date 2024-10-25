## Spotify Time Machine ⏳🎶
Ever wanted to go back in time and listen to the Billboard Hot 100 hits of a specific date? Well, now you can with Spotify Time Machine! This Python tool connects to the Spotify API, grabs the top songs from Billboard on a given date, and creates a custom playlist for your nostalgic journey.

## Features
Fetches the Billboard Hot 100 for any date you choose 📅
Finds each song on Spotify and creates a playlist with them 🎵
Customizes each playlist with the date and a unique description 💫
Getting Started
To run this project, make sure you have the following setup:

## Python 3.6+ - Download and install Python.
Spotify API credentials - Register an app on Spotify Developer and get a Client ID & Secret.
Spotipy Library - Install it with:
bash
Copy code
pip install spotipy beautifulsoup4 requests
Running the Project
After setting up your Spotify API credentials, replace CLIENT_ID and CLIENT_SECRET in the code with your values.

Run the script:

bash
Copy code
python spotify_time_machine.py
You'll be prompted to enter a date in YYYY-MM-DD format. The script will then create a Spotify playlist with the top 100 songs from Billboard for that day.

Example
text
Copy code
Enter the date you want to travel to (YYYY-MM-DD): 1985-07-13
The playlist will be automatically created in your Spotify account! 🎉

## Dependencies
Spotipy for Spotify API interaction
Requests for web scraping
BeautifulSoup4 to parse Billboard charts
Contributing
Feel free to fork and make pull requests if you want to enhance this time-traveling jukebox!

## License
This project is licensed under the MIT License.
