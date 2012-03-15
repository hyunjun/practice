//	http://www.careercup.com/question?id=13030673
#include <stdio.h>
#include <unistd.h>
int main()
{
	fork();
	fork() && fork() || fork();
	fork();

	printf("forked\n");
	return	0;
}
