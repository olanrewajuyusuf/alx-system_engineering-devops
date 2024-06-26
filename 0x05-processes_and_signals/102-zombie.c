#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

/**
 * infinite_while - Function to run an infinite loop
 *
 * Return: Always 0.
 */
int infinite_while(void)
{
while (1)
{
sleep(1);

return (0);
}

/**
 * main - Entry point
 *
 * Return: Always 0.
 */
int main(void)
{
pid_t child_pid;
int i;

for (i = 0; i < 5; i++)
{
child_pid = fork();
if (child_pid == -1)
{
perror("fork");
exit(1);

if (child_pid == 0)
{
printf("Zombie process created, PID: %d\n", getpid());
exit(0);
}
}

infinite_while();
return (0);
}
