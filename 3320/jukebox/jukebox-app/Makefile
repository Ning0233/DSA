CC = gcc
CFLAGS = -Wall -Wextra -std=c11
SRC = src/jukebox.c
OBJ = $(SRC:.c=.o)
EXEC = jukebox

all: $(EXEC)

$(EXEC): $(OBJ)
	$(CC) $(OBJ) -o $(EXEC)

%.o: %.c
	$(CC) $(CFLAGS) -c $< -o $@

clean:
	rm -f $(OBJ) $(EXEC)