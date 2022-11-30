#include "lists.h"

/**
 * insert_node - insert node
 * @head: the head of the liked list
 * @number: the number to inserted
 *
 * Description: nserts a number into a sorted singly linked list
 *
 * Return: the address of thenew node or null if fail
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new;
	listint_t *current;
	listint_t *later;
	listint_t *temp;

	current = *head;
	later = *head;

	new = malloc(sizeof(listint_t));
	if (new  == NULL)
		return (NULL);

	new->n = number;
	new->next = NULL;

	while (current != NULL)
	{
		later = later->next;
		if (later->n > number)
			break;
		current = current->next;
	}
	temp = current->next;
	current->next = new;
	new->next = temp;

	return (new);
}
