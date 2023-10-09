#include "lists.h"

/**
  * is_palindrome - checks if a singly linked list is a palindrome
  * 
  * @head: the double pointer to the beginning of the list
  *
  * Return: 0 if not a palindrome, 1 if it is
  */
int is_palindrome(listint_t **head)
{
	listint_t *length;
	listint_t *reversed_head;
	unsigned int count;

	if (head == NULL || *head == NULL)
		return (1);
	length = *head;
	for (count = 0; length != NULL; count++)
		length = length->next;
	if (count == 1)
		return (1); /*List of 1 is palindrome*/
	reversed_head = reverse_list(*head, count);
	if (is_pal(*head, reversed_head) == 1)
		return (1);
	else
		return (0);
}

/**
  * reverse_list - reverses palindrome for comparison
  *
  * @head: the pointer to the beginning of the list
  * @count: how big the list is
  *
  * Return: the beginning of the newly reversed list
  */
listint_t *reverse_list(listint_t *head, unsigned int count)
{
    listint_t *prev = NULL;
    listint_t *current = head;
    listint_t *next = NULL;

    /*Reverse the first 'count' nodes*/
    for (unsigned int i = 0; i < count; i++)
    {
        next = current->next;
        current->next = prev;
        prev = current;
        current = next;
    }
    head->next = current;

    return prev;
}

/**
  * is_pal - checks if a list is a palindrome
  * @head: the beginning of the first half of the list
  * @reversed_head: the beginning of the reversed list
  * Return: 1 if palindrome, 0 if not
  */
int is_pal(listint_t *head, listint_t *reversed_head)
{
	while (reversed_head != NULL)
	{
		if (head->n != reversed_head->n)
			return (0);
		head = head->next;
		reversed_head = reversed_head->next;
	}
	return (1);
}
