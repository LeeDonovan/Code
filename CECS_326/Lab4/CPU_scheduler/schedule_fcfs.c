/**
 * FCFS scheduling
 */
 
#include <stdlib.h>
#include <stdio.h>

#include "task.h"
#include "list.h"
#include "cpu.h"
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

void schedule(){
    traverse(head);//list nodes
    while(head != NULL){
	run(head->task, head->task->burst);//go through node and print burst
	head = head->next;//go next node
	}
}