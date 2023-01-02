#include "lists.h"
/*
 * is_palindrome- checks if a singly linked list is a palindrome
 *
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *temp, *temp2;
	size_t num;

	if (*head != NULL)
	{
		temp = *head;
	}
	while (temp->next != NULL)
	{
		num++;
		temp = temp->next;
	}
	if ((num + 1) % 2 == 0)
	{
		temp2 = *head;
		for (i = 0; i <= ((num + 1) /2); i++)
		{
			if (
		}
	}

}
