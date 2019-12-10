#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * insert_node - Inserts a number into a list
 * @head: The start of the sorted, singly linked list
 * @number: The number to add to the list
 *
 * Return: The address of the new node or NULL
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new;
	listint_t *prev = *head;
	listint_t *current = (*head)->next;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);

	if (*head == NULL)
		*head = new;
	else
	{
		while (current != NULL)
		{
			if (current->n > number)
			{
				new->next = current;
				prev->next = new;
				break;
			}
			else
			{
				prev = prev->next;
				current = current->next;
			}
			new->n = number;
		}
	}

	return (new);
}
