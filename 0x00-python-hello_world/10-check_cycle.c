#include "lists.h"
/**
 * check_cycle- function to check if a linked list is cyclic
 * @list: head of the linked list
 * Return: 1 if cyclic and 0 otherwise
 */
int check_cycle(listint_t *list)
{
	listint_t *tmp1 = list->next;
	listint_t *tmp2 = list;

	while (tmp1 != NULL)
	{
		if (tmp1 == tmp2)
		{
			return (1);
		}
		tmp1 = list->next;
		list = tmp1;
	}
	return (0);
}
