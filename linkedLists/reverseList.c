
struct Node {
	int data;
	struct Node *next;
};

struct Node *head;

struct Node* ReverseIterative(struct Node *head) {

	struct Node *current, *prev, *next;
	temp = head;
	while(temp !=NULL) {
		next = current -> next;
		current -> next = prev;
		prev = current;
		current = next;
	}
	head = prev;
	return head;

}

void ReversePrint(struct Node* p) {
	if (p = NULL) {
		return;
	}
	ReversePrint(p->next);
	printf("%d", p->data);
}

void ReverseRecursion(struct Node *p) {
	if (p-> next = NULL) {
		head = p;
		return;
	}
	Reverse(p->next);
	struct Node *q = p -> next;
	q -> next = p;
	p -> next = NULL;

}