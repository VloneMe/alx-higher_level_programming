#include "lists.h"

/**
 * insert_node - This function inserts a number into a sorted singly linked list.
 * @head: A pointerlist head
 * @number: A number to be stored in the new node
 * Return: pointer to the new node
 */
listint_t *insert_node(listint_t **head, int number)
{
        listint_t *run_node;
        listint_t *new_node;

        run_node = *head;

        new_node = malloc(sizeof(listint_t));
        if (new_node == NULL)
                return (NULL);
        new_node->n = number;

        if (*head == NULL || (*head)->n > number)
        {
                new_node->next = *head;
                *head = new_node;
                return (new_node);
        }

        while (run_node->next != NULL)
        {
                if ((run_node->next)->n >= number)
                {
                        new_node->next = run_node->next;
                        run_node->next = new_node;
                        return (new_node);
                }
                run_node = run_node->next;
        }

        new_node->next = NULL;
        run_node->next = new_node;
        return (new_node);
}
