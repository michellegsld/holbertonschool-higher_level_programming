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
	listint_t *current = *head;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);

	new->n = number;

	if (*head == NULL)
	{
		new->next = *head;
		*head = new;
	}
	else if (current->next == NULL)
	{
		if (current->n > number)
		{
			new->next = current;
			*head = new;
		}
		else
		{
			current->next = new;
			new->next = NULL;
		}
	}
	else
	{
		while (current->next && current->next->n < number)
			current = current->next;
		new->next = current->next;
		current->next = new;
	}

	return (new);
}
