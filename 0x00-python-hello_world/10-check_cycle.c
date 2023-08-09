 #include "lists.h"
  2
  3 /**
  4  * check_cycle - function checks if a singly linked list has a cycl
    e in it.
  5  * @list: pointer to the beginning of the node
  6  * Return: 0 if no cycle, 1 if there is a cycle
  7  */
  8 int check_cycle(listint_t *list)
  9 {
 10         listint_t *current, *check;
 11
 12         if (list == NULL || list->next == NULL)
 13                 return (0);
 14         current = list;
 15         check = current->next;
 16
 17         while (current != NULL && check->next != NULL
 18                 && check->next->next != NULL)
 19         {
 20                 if (current == check)
 21                         return (1);
 22                 current = current->next;
 23                 check = check->next->next;
 24         }
 25         return (0);
 26 }
