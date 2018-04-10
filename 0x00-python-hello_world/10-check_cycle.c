#include "lists.h"

/**
 * check_cycle - check if list loops on self
 * @list: list
 *
 * Return: 1 if loop is found, otherwise 0.
 */

int check_cycle(listint_t *list)
{
	listint_t *turtle = list, *hare = list;

	while (turtle != NULL && hare != NULL && hare->next != NULL)
	{
		turtle = turtle->next;
		hare = hare->next->next;
		if (turtle == hare)
			return (1);
	}
	return (0);
}
