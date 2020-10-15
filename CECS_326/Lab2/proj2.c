#include <pthread.h>
#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>
#include <stdint.h>
#include <stdbool.h>

pthread_mutex_t office_mutex;
pthread_mutex_t leave_mutex;
pthread_mutex_t question_mutex;
pthread_mutex_t answer_mutex;

pthread_barrier_t barrier;

pthread_cond_t question_cond;
pthread_cond_t answer_cond;
pthread_cond_t office_cond;
pthread_cond_t professor_wait;

int capacity;
int occupancy = 0;
int num_students;
int student_counter;
bool question = false;
bool answer = false;
void *EnterOffice();
void LeaveOffice();
void *StudentID(void * arg);
void QuestionStart();
void QuestionDone();
void *Professor();
void AnswerStart();
void AnswerDone();


//pthread_cond_signal(&pthread_cond)//wakes up the wait condition

void AnswerStart(){//Answer Start
	pthread_mutex_lock(&answer_mutex);
	while(!question){
		printf("Professor is waiting for Student %d question.\n", student_counter);
		pthread_cond_wait(&question_cond, &answer_mutex);
	}
	printf("Professor starts to answer question for Student %d.\n", student_counter);
}

void AnswerDone(){//Answer Done
	printf("Professor is done answering for Student %d.\n", student_counter);
	question = false;
	pthread_cond_signal(&answer_cond);
	pthread_mutex_unlock(&answer_mutex);
}

void QuestionStart(){//Question Start
 	pthread_mutex_lock(&question_mutex);
 	while(!answer){
		printf("Student %d is waiting to ask a question.\n", student_counter);
		pthread_cond_wait(&answer_cond, &question_mutex);
	}
	printf("Student %d ask a question.\n",student_counter);
	question = true;
	answer = false;
	pthread_cond_signal(&question_cond);
}

void QuestionDone(){
	printf("Student %d is satisfied.\n",student_counter);
	question = false;
	pthread_mutex_unlock (&question_mutex);
}

void *EnterOffice(){//Enter Office
	pthread_mutex_lock(&office_mutex);
	while(occupancy >= capacity){
		printf("Student %d must wait before entering.\n", student_counter);
		pthread_cond_wait(&office_cond, &office_mutex);
	}	
	printf("Student %d walks into the office.\n", student_counter);
	occupancy++;
	
	pthread_cond_signal(&professor_wait);
	pthread_mutex_unlock(&office_mutex);
	
}

void LeaveOffice() {//Leave Office
	pthread_mutex_lock(&leave_mutex);
	printf("Student %d leaves the office.\n",student_counter);
	occupancy--;
	
	pthread_cond_signal(&office_cond);
	pthread_mutex_unlock(&leave_mutex);
}

void *StudentID(void * arg){//Student ID
	int stud_id =(intptr_t) arg;
	int stud_questions = (stud_id % 4) + 1;
	student_counter = stud_id;
	EnterOffice();
	usleep(((rand() % 5) + 1 * 10000));
	for(int i = 0; i < stud_questions; i++){
		QuestionStart();
		QuestionDone();
	}
	LeaveOffice();
	
}



void *Professor(){//Professor
	AnswerStart();
	AnswerDone();
}


///////////////// Main ///////////////////////////////////////////////////////////
int main(int argc, char *argv[]){//accepts 1 cmd line for # of students
	int i;
	int num_students;
	if(argc <= 2){//checks to see if only one parameter was taken
		printf("Please enter only one parameter for the command line");
		return(0);
	}
	else{
		num_students = atoi(argv[1]);//converts string to int
		capacity = atoi(argv[2]);
		if(num_students < 1 || capacity < 1){//checks to see if a positive number was inputted
			printf("Enter a positive whole number...");
			return 0;
		}
		//Creates a barrier to make threads wait for eachother
		if(pthread_barrier_init(&barrier, NULL, num_students)){
			printf("Barrier not created...");
			return -1;
		}

		pthread_t array[num_students];//creating a unique data type for threads
		pthread_t professor_thread; //create thread for professor
		
		pthread_create(&professor_thread, NULL, Professor,NULL);
		
		for(i = 0; i < num_students; i++){
			pthread_create(&array[i], NULL, StudentID,(void *)(intptr_t) i );//loop that creates threads 
		}

		for ( i = 0; i < num_students; i++){
			pthread_join(array[i], NULL);
		}//joins multiple threads by waiting for current thread to finish 
		
		
	}
	
	return 0;
}