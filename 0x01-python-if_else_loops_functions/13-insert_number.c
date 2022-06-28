#include "lists.h"
/**
 * insert_node - function to add a node in a sorted linked
 * in ascending other
 * @head: pointer to the first node of list
 * @number: number to be added
 * Return: pointer to new node
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *tmp1 = malloc(sizeof(listint_t));
	listint_t *tmp2 = *head;

	if (tmp1 == NULL)
	{
		free(tmp1);
		return (NULL);
	}
	tmp1->n = number;
	tmp1->next = *head;
	if (tmp1->n < tmp1->next->n || *head == NULL)
	{
		*head = tmp1;
		return (tmp1);
	}
	while ((tmp1->n != tmp1->next->n || tmp1->n < tmp1->next->n) && tmp1->next->next->n < tmp1->n)
	{
		if (tmp1->next->next == NULL)
		{
			tmp2->next = tmp1;
			return (tmp1);
		}
		tmp1->next = tmp1->next->next;
		tmp2 = tmp2->next;
	}
	tmp1->next = tmp1->next->next;
	tmp2->next = tmp1;
	return (tmp1);
	}
}
