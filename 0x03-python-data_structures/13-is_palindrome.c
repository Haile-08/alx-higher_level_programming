#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * find_index - return a value at index
 * @head: the head
 * @n: the index value
 * Return: the value at index n
 */
int find_index(listint_t *head, int n)
{
	int  l;
	int val;

	l = 0;
	while (head->next != NULL && l > n)
	{
		l += 1;
		head = head->next;
	}
	val = head->n;
	return (val);
}

/**
 * is_palindrome - check if palindrome
 * @head: the head
 * Return: 0 if it not and 1 if it is
 */
int is_palindrome(listint_t **head)
{
	listint_t *ol;
	listint_t *lc;
	int len;
	int count;

	lc = *head;
	len = 0;
	while (lc->next != NULL)
	{
		len += 1;
		lc = lc->next;
	}
	if (len == 0)
		return (1);
	ol = *head;
	count = 0;
	while (ol->next != NULL)
	{
		if (find_index(*head, len) != find_index(*head, count))
			return (0);
		count = count + 1;
		len = len - 1;
		ol = ol->next;
	}
	return (1);
}
