#include <stdlib.h>
  2 #include <string.h>
  3 #include <stdio.h>
  4 #include "lists.h"
  5
  6 /**
  7  * main - check the code
  8  *
  9  * Return: Always 0.
 10  */
 11 int main(void)
 12 {
 13     listint_t *head;
 14     listint_t *current;
 15     listint_t *temp;
 16     int i;
 17
 18     head = NULL;
 19     add_nodeint(&head, 0);
 20     add_nodeint(&head, 1);
 21     add_nodeint(&head, 2);
 22     add_nodeint(&head, 3);
 23     add_nodeint(&head, 4);
 24     add_nodeint(&head, 98);
 25     add_nodeint(&head, 402);
 26     add_nodeint(&head, 1024);
 27     print_listint(head);
 28
 29     if (check_cycle(head) == 0)
 30         printf("Linked list has no cycle\n");
 31     else if (check_cycle(head) == 1)
 32         printf("Linked list has a cycle\n");
 33
 34     current = head;
 35     for (i = 0; i < 4; i++)
 36         current = current->next;
 37     temp = current->next;
 38     current->next = head;
 39
 40     if (check_cycle(head) == 0)
 41         printf("Linked list has no cycle\n");
 42     else if (check_cycle(head) == 1)
 43         printf("Linked list has a cycle\n");
 44
 45     current = head;
 46     for (i = 0; i < 4; i++)
 47         current = current->next;
 48     current->next = temp;
 49
 50     free_listint(head);
 51
 52     return (0);

