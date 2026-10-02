#week 2- day 4: environment variables and configuration

#imported the os module to access environment variables and the load_dotenv function from the dotenv package to load environment variables from a .env file.
import os
from dotenv import load_dotenv

# Load environment variables from a .env file
load_dotenv()

# Define configuration variables using environment variables
OpenAI_API_KEY = os.getenv("OPENAI_API_KEY")
Database_URL = os.getenv("DATABASE_URL")


if __name__ == "__main__":          #this line checks if the script is being run directly (not imported as a module) and executes the code block below it.
    print("OpenAI API Key:", OpenAI_API_KEY)
    print("Database URL:", Database_URL)