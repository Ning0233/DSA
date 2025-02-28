#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>
#include <unistd.h>

#define NUM_SONGS 5

typedef struct {
    char artist[50];
    char song[50];
    char album[50];
    char filename[50];
} Song;

void print_menu(Song songs[]) {
    printf("%-30s %-30s %-30s\n", "Artist", "Song", "Album");
    printf("---------------------------------------------------------------\n");
    for (int i = 0; i < NUM_SONGS; i++) {
        printf("%-30s %-30s %-30s\n", songs[i].artist, songs[i].song, songs[i].album);
    }
}

void play_song(const char *filename) {
    FILE *file = fopen(filename, "r");
    if (file == NULL) {
        perror("fopen");
        return;
    }

    char line[256];
    while (fgets(line, sizeof(line), file)) {
        printf("%s", line);
        sleep(1);
    }

    fclose(file);
}

int main() {
    Song songs[NUM_SONGS] = {
        {"1: Aimyon", "Till I Know What Love0", "Falling into your eyes Record", "src/songs/song1.txt"},
        {"2: Djerv", "Rebel Heart", "Arcane League of Legends: Season 2", "src/songs/song2.txt"},
        {"3: Leslie Odom", "Alexander Hamilton", "Hamilton", "src/songs/song3.txt"},
        {"4: Lin-Manuel Miranda", "Aaron Burr, Sir", "Hamilton", "src/songs/song4.txt"},
        {"5: Lin-Manuel Miranda", "My Shot", "Hamilton", "src/songs/song5.txt"}
    };

    while (1) {
        print_menu(songs);
        printf("Enter the number of the song to play (1-%d) or 0 to quit: ", NUM_SONGS);
        int choice;
        scanf("%d", &choice);

        if (choice == 0) {
            break;
        } else if (choice > 0 && choice <= NUM_SONGS) {
            play_song(songs[choice - 1].filename);
        } else {
            printf("Invalid choice. Please try again.\n");
        }
    }

    return 0;
}