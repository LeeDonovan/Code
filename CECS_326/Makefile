CC = gcc

make: main.c
	$(CC) main.c -pthread -o NoSync
	$(CC) main.c -pthread -DPTHREAD_SYNC -o WithSync