#include "lists.h"
/**
 * is_palindrome - handle empty strings and call iterative checker
 * @head: list
 *
 * Return: 1 if palindrome, otherwise 0.
 */

int is_palindrome(listint_t **head)
{
	if (head == NULL || *head == NULL)
		return (1);
	return (check_palindrome(head, *head));
}

/**
 * check_palindrome - iterate through string while checking if palindrome
 * @head: start of list
 * @end: end of the list
 *
 * Return: 1 if palindrome, otherwise 0
 */

int check_palindrome(listint_t **head, listint_t *end)
{
	if (end == NULL)
		return (1);
	if (check_palindrome(head, end->next) && (*head)->n == end->n)
	{
		*head = (*head)->next;
		return (1);
	}
	return (0);
}
