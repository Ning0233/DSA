# Jukebox Application

This project is a simple jukebox application that allows users to select and play songs while displaying their lyrics with a delay between lines. The application is designed to be user-friendly and provides a formatted table of available songs.

## Project Structure

```
jukebox-app
├── src
│   ├── jukebox.c          # Main logic for the jukebox application
│   ├── songs
│   │   ├── song1.txt      # Lyrics for the first song
│   │   ├── song2.txt      # Lyrics for the second song
│   │   └── song3.txt      # Lyrics for the third song
├── Makefile                # Build instructions for the project
└── README.md               # Documentation for the project
```

## Features

- Displays a formatted table of songs including artist, song title, and album name.
- Allows users to select songs to play.
- Reads lyrics from text files and displays them with a delay between lines.

## How to Build and Run

1. Clone the repository or download the project files.
2. Navigate to the project directory.
3. Run the following command to build the application:

   ```
   make
   ```

4. After building, run the application with:

   ```
   ./jukebox
   ```

## Additional Information

- The lyrics for each song are stored in separate text files located in the `src/songs` directory.
- You can add more songs by creating new text files in the `src/songs` directory and updating the `jukebox.c` file accordingly.

Enjoy your music!