 #ifndef LIST_H
  2 #define LIST_H
  3
  4 #include <stdio.h>
  5
  6 /**
  7  * struct listint_s - singly linked list
  8  * @n: integer
  9  * @next: points to the next node
 10  *
 11  * Description: singly linked list node
 12  *
 13  */
 14 typedef struct listint_s
 15 {
 16         int n;
 17         struct listint_s *next;
 18 }listint_t;
 19
 20 size_t print_listint(const listint_t *h);
 21 listint_t *add_nodeint(listint_t **head, const int n);
 22 void free_listint(listint_t *head);
 23 int check_cycle(listint_t *list);
 24
 25 #endif /* LISTS_H */
