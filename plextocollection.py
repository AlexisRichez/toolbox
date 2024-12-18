from plexapi.server import PlexServer
import os

# Configuration
PLEX_URL = "http://localhost:32400"  # Replace with your Plex Server IP
PLEX_TOKEN = "tuLE9Z-xpzjtpcswb-xT"  # Replace with your Plex Token
LIBRARY_NAME = "Cartoons"
FOLDER_PATH = "/media/NAS/cartoons/Tom And Jerry"  # Replace with your folder path
COLLECTION_NAME = "Tom And Jerry"  # Desired collection name

# Connect to Plex server
plex = PlexServer(PLEX_URL, PLEX_TOKEN)

# Access the library
library = plex.library.section(LIBRARY_NAME)

# List media in the folder
files_in_folder = [f for f in os.listdir(FOLDER_PATH) if os.path.isfile(os.path.join(FOLDER_PATH, f))]

# Iterate through media in the Plex library
for item in library.all():
    if item.media:
        # Check if the file is in the target folder
        for media in item.media:
            for part in media.parts:
                if part.file.startswith(FOLDER_PATH):  # Match folder path
                    print(f"Adding '{item.title}' to collection '{COLLECTION_NAME}'")
                    item.addCollection(COLLECTION_NAME)
