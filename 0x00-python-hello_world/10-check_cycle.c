#include "lists.h"

/**
 * check_cycle - This function checks if a linked list is circular or not
 * @list: linked list to check
 * Return: 1 (linked list is circular) 0 (no loop detected)
 */
int check_cycle(listint_t *list)
{
	listint_t *slow = list;
	listint_t *fast = list->next;
        
	if (list == NULL || list->next == NULL)
		return (0);

	while (fast != NULL && fast->next != NULL)
	{
		if (slow == fast)
			return (1);

		slow = slow->next;
		fast = fast->next->next;
	}
	return 0;
}
