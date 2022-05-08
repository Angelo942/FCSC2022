CFLAGS  += -Wall -Wextra -Wformat -Wformat-security -Werror
CFLAGS  += -fstack-protector-strong
LDFLAGS += -z now -z relro

rpg:
	gcc $(CFLAGS) rpg.c -o rpg $(LDFLAGS)

clean:
	rm *.o rpg
