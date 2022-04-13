#include <unistd.h>
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <errno.h>
#include <sys/types.h>
#include <sys/wait.h>

int main()
{
	pid_t pid;
	int loop=100;

	if(-1 == (pid = fork()))
	{
			printf("Error happened in fork function!\n");
			return 0;
	}

	if(0 == pid)
	{
			loop++;
			printf("This is child process: %d,loop=%d\n", getpid(),loop);
	}
	else
	{
			loop++;
			printf("This is parent process: %d,loop=%d\n", getpid(),loop);
	}

	return 0;
}

