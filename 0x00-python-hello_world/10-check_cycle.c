#include "lists.h"

/**
 * check_cycle - Checks if the list has a loop
 * @list: The list to check
 *
 * Return: Either 0 or 1
 */
int check_cycle(listint_t *list)
{
	listint_t *fast = list;
	listint_t *slow = list;

	while (fast != NULL && slow != NULL)
	{
		slow = slow->next;
		if (fast->next == NULL)
			return (0);
		fast = fast->next;
		fast = fast->next;

		if (fast == slow)
			return (1);
	}
	return (0);
}
