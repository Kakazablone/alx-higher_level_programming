#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * is_palindrome - tests if linked list is palindrome.
 *
 * @head: head pointer
 *
 * Return: 0 if it is and 1 if it's not.
 */

int is_palindrome(listint_t **head)
{
        listint_t *slow = *head;
        listint_t *fast = *head;
        int list_array[2048];

        int i = 0;

        if (*head == NULL || (*head)->next == NULL)
                return (1);

        while (fast != NULL && fast->next != NULL)
        {
                list_array[i] = slow->n;
                slow = slow->next;
                fast = fast->next->next;
                i++;
        }
        if (fast != NULL)
        {
                slow = slow->next;
        }
        for (i = i - 1; i >= 0; i--)
        {
                if (list_array[i] != slow->n)
                {
                        return (0);
                }
                slow = slow->next;
        }
        return (1);
}
