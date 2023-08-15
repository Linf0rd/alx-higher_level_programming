#include "lists.h"

/**
 * is_palindrome - Checks if a singly linked list is a palindrome.
 * @head: Double pointer to the head of the linked list.
 *
 * Return: 0 if not a palindrome, 1 if it is a palindrome.
 */

int is_palindrome(listint_t **head)
{
	listint_t *slow = *head, *fast = *head;
	list_t *prev = NULL, *temp = NULL;
	int palindrome = 1;

	if (*head == NULL || (*head)->next == NULL)
		return (palindrome);
	while (fast != NULL && fast->next != NULL)
	{
		fast = fast->next->next;
		temp = slow;
		slow = slow->next;
		temp->next = prev;
		prev = temp;
	}
	if (fast != NULL)
		slow = slow->next;
	while (slow != NULL)
	{
		if (prev->m != slow->n)
		{
			palindrome = 0;
			break;
		}
		prev = prev->next;
		slow = slow->next;
	}
	temp = NULL;
	fast = prev;
	while (fast != NULL)
	{
		slow = fast->next;
		fast->next = temp;
		temp = fast;
		fast = slow;
	}
	(*head)->next = temp;
	return (palindrome);
}
