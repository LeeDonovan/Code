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
pthread_mutex_t professor_wake;
pthread_mutex_t bool_lock;


pthread_cond_t quest_cond;
pthread_cond_t answer_cond;
pthread_cond_t office_cond;
pthread_cond_t professor_wait;

int capacity;
int occupancy = 0;
int num_students;
static __thread int student_counter;
int current_student;
bool question = false;
bool answer = false;
bool flag = true;
//initialize 
void EnterOffice();
void LeaveOffice();
void *StudentID(void * arg);
void QuestionStart();
void QuestionDone();
void *Professor();
void AnswerStart();
void AnswerDone();



void AnswerStart(){//Answer Start
	pthread_mutex_lock(&answer_mutex);
	while(!question){//checks to see if there is a question being asked by a student
		printf("Professor is waiting for a question.\n");
		pthread_cond_wait(&quest_cond, &answer_mutex);//waits for signal from QuestionStart() to begin answering student's question
	}
	printf("Professor starts to answer question for Student %d.\n", current_student);
	
}

void AnswerDone(){//Answer Done
	printf("Professor is done answering for Student %d.\n", current_student);
	pthread_mutex_lock(&bool_lock);//locks boolean variables so they don't interfere with other threads
	question = false;
	answer = true;
	pthread_mutex_unlock(&bool_lock);
	pthread_cond_signal(&answer_cond);
	pthread_mutex_unlock(&answer_mutex);
}

void QuestionStart(){//Question Start
 	pthread_mutex_lock(&question_mutex);
	pthread_mutex_lock(&bool_lock);// makes sure that the booleans don't get touched with other threads being ran
	current_student = student_counter;
	question = true;
	answer = false;
	pthread_mutex_unlock(&bool_lock);
	
	pthread_cond_signal(&quest_cond);//signals to the wait condition in AnswerDone() to start the next question to be asked
	printf("Student %d ask a question.\n",student_counter);

	while(!answer){//checks to see if professor can answer a question
		printf("Student %d is waiting for an answer.\n", student_counter);
		pthread_cond_wait(&answer_cond, &question_mutex);
	}

}
	

void QuestionDone(){
	printf("Student %d is satisfied.\n",student_counter);
	pthread_mutex_unlock(&question_mutex);//unlocks from QuestionStart()
}

void EnterOffice(){//Enter Office
	pthread_mutex_lock(&office_mutex);//makes sure only one thread is ran 
	printf("Occupancy is %d.\n", occupancy);
	while(occupancy >= capacity){//checks to see if office cap is full
		printf("Student %d must wait before entering.\n", student_counter);
		pthread_cond_wait(&office_cond, &office_mutex);//waits for signal that tells this condition that there is room
	}	
	printf("Student %d walks into the office.\n", student_counter);
	occupancy++;
	printf("Occupancy has increased\n");
	pthread_mutex_unlock(&office_mutex);
	
}

void LeaveOffice() {//Leave Office
	pthread_mutex_lock(&leave_mutex);
	printf("Student %d leaves the office.\n",student_counter);
	occupancy--;//decreases occupancy for next thread to come in
	
	pthread_cond_signal(&office_cond);//signals to EnterOffice() so next student could walk in 
	pthread_mutex_unlock(&leave_mutex);
}

void *StudentID(void * arg){//Student ID
	//usleep(5);
	int stud_id =(intptr_t) arg;
	int stud_questions = (stud_id % 4) + 1;//creates the number of questions a student will have to ask
	student_counter = stud_id; // holds the student id that is currently being ran in the thread
	EnterOffice();
	usleep(((rand() % 5) + 1 * 10000));// have students come in at different times
	for(int i = 0; i < stud_questions; i++){
		QuestionStart();
		QuestionDone();
	}
	LeaveOffice();
	pthread_exit(NULL);
}


void *Professor(){//Professor
	
	while(true){
		AnswerStart();
		AnswerDone();
	}
	pthread_exit(NULL);
}


///////////////// Main ///////////////////////////////////////////////////////////
int main(int argc, char *argv[]){//accepts 1 cmd line for # of students
	int i;
	int num_students;
	pthread_mutex_init(&office_mutex, NULL);
	pthread_mutex_init(&leave_mutex, NULL);
	pthread_mutex_init(&question_mutex, NULL);
	pthread_mutex_init(&answer_mutex, NULL);
	pthread_mutex_init(&professor_wake, NULL);
	pthread_mutex_init(&bool_lock, NULL);

	pthread_cond_init(&quest_cond, NULL);
	pthread_cond_init(&answer_cond, NULL);
	pthread_cond_init(&office_cond, NULL);
	pthread_cond_init(&professor_wait, NULL);

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


		pthread_t array[num_students];//creating a unique data type that holds student threads
		pthread_t professor_thread; //create thread for professor
		
		pthread_create(&professor_thread, NULL, Professor,NULL);
		
		for(i = 0; i < num_students; i++){
			pthread_create(&array[i], NULL, StudentID,(void *)(intptr_t) i );//loop that creates student threads 
		}

		for ( i = 0; i < num_students; i++){
			pthread_join(array[i], NULL);
		}//joins multiple threads by waiting for current thread to finish 
		pthread_kill(&professor_thread, 0);
		pthread_kill(&array, 0);
	}
	//destroys mutex
	pthread_mutex_destroy(&office_mutex);
	pthread_mutex_destroy(&leave_mutex);
	pthread_mutex_destroy(&question_mutex);
	pthread_mutex_destroy(&answer_mutex);
	pthread_mutex_destroy(&professor_wake);
	pthread_mutex_destroy(&bool_lock);
	//destroys condtions
	pthread_cond_destroy(&quest_cond);
	pthread_cond_destroy(&answer_cond);
	pthread_cond_destroy(&office_cond);
	pthread_cond_destroy(&professor_wait);
	
	return 0;
}