#include "lists.h"

/**
 * check_cycle - check cycle
 * @list: the list head
 *
 * Description: check if a linked list has a cycle
 *
 * Return: 0 if there is no cycle,1 if there is
 */

int check_cycle(listint_t *list)
{
	listint_t *tmp;

	tmp = malloc(sizeof(listint_t));
	if (tmp == NULL)
		return (1);
	tmp = list;
	while (list != NULL)
	{
		if (list->next == tmp)
		{
			tmp = NULL;
			free(tmp);
			return (1);
		}
		list = list->next;
	}
	tmp = NULL;
	free(tmp);
	return (0);
}
