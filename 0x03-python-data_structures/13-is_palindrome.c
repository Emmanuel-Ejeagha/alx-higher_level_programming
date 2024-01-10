#include "lists.h"

/**
 * is_palindrome - check if the list is a palindrome
 * @head: head of the list
 * Return: Always 1 if palindrome.
 */
int is_palindrome(listint_t **head)
{
	listint_t *list;
	int i = 0, j = 0, len = 0, palindome = 1;
	int p[1024];

	list = *head;
	if (*head == NULL || list->next == NULL)
		return (palindome);
	while (list != NULL)
		len++, list = list->next;
	list = *head;
	if (len % 2 == 0)
	{
		while (list != NULL)
		{
			if (i > len / 2 - 1)
				p[j] = list->n, j++;
			list = list->next, i++;
		}
	}
	else
	{
		while (list != NULL)
		{
			if (i > len / 2)
				p[j] = list->n, j++;
			list = list->next, i++;
		}
	}
	list = *head, i = 0;
	while (i <= len / 2 - 1)
	{
		if (list->n != p[len / 2 - 1 - i])
			palindome = 0;
		list = list->next, i++;
	}
return (palindome);
}
