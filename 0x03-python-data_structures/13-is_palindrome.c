#include <stdlib.h>
#include <stddef.h>
#include "lists.h"
/**
 * is_palindrome - checks if a
 * linked list is a palindrome
 * @head: a pointer to a pointer
 * containing the address of
 * the first node of the list
 * Return: 1(if a palindrome) and no otherwise
 */
int is_palindrome(listint_t **head)
{
	listint_t *tmp1 = *head;
	listint_t *tmp2 = NULL;
	int i = 0;
	int *ptr = NULL;
	
	if (*head == NULL)
		return (1);
	
	while (tmp1 != NULL)
	{
		i++;
		tmp1 = tmp1->next;
	}
	tmp1 = *head;
	ptr = calloc(i, sizeof(int));
	i = 0;
	/*fills the array with numbers from the list*/
	while (tmp1 != NULL)
	{
		ptr[i] = tmp1->n;
		i++;
		tmp1 = tmp1->next;
	}
	tmp1 = NULL;
	while (*head != NULL)
	{
		tmp2 = (*head)->next;
		(*head)->next = tmp1;
		tmp1 = *head;
		*head = tmp2;
	}
	*head = tmp1;
	i = 0;
	/*compare the array to the linked list reversed*/
	while (tmp1 != NULL)
	{
		if (ptr[i] != tmp1->n)
		{
			free(ptr);
			return (0);
		}
		i++;
		tmp1 = tmp1->next;
	}
	free(ptr);
	return (1);
}
