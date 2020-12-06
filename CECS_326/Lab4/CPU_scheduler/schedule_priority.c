/*
 * Priority scheduling
 */
#include <stdlib.h>
#include <stdio.h>
#include <stddef.h>

#include "task.h"
#include "list.h"
#include "cpu.h"

/*
 * Your code and design here:
 */
int TID = 1;
//Your code and design here
struct node *head = NULL;
void add(char *name, int priority, int burst);

void add(char *name, int priority, int burst){
    Task *addTask = malloc(sizeof(Task));//allocate space for Task
    addTask->name = name;//add name
    addTask->tid = TID;//add ID
    addTask->priority = priority;//add priority
    addTask->burst = burst;//add burst
    TID++;

    if(head == NULL){
        head = (struct node*)malloc(sizeof(struct node));//allocate space for top of empty node
        head->task = addTask;
        head->next = NULL;
        
    }
    else{
        insert(&head, addTask);//insert new task created 
        
    }
}

int max(struct node *head){
    int max = 0;//set min 
    struct node *temp = head;//use temp to store an extra head of node
    while(temp != NULL){
        if(max < temp->task->priority){//run through temp to find max priority
            max = temp->task->priority;//if found then max is now max priority
        }
        temp = temp->next;
    }
    if(max == 0){
        return -1;
    }
    while(head != NULL){
        if(head->task->priority == max){//match head priority with max 
            run(head->task, head->task->burst);//print head task if matched
            head->task->priority = 0;//priority then set to 0 to find new max in nodes
        }
        head = head->next;
    }
    return max;
}


void schedule(){
    for(int i = 0; i < TID-1; i++){//loop through node list to print out all nodes starting with max
        max(head);
    }
}