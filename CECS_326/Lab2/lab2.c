#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <pthread.h>
#include <semaphore.h>

int num_students;
int office_capacity;
int current_student_id;

sem_t OfficeSpots;
sem_t StudentCanAskQuestion;
sem_t ProfessorCanSpeak;
sem_t StudentCanSpeak;

void * Professor();
void * Student(void *id);

void AnswerStart(int student_id);
void AnswerDone(int student_id);
void EnterOffice(int id);
void LeaveOffice(int id);
void QuestionStart(int id);
void QuestionDone(int id);

int main(int argc, char *argv[])
{
   // Input Validation
   if (argc <= 2)
   {
       printf("Error: Please specify a number of students and office capacity.\n");
       return 0;
   }

   num_students = atoi(argv[1]);
   office_capacity = 2;
   if (!num_students)
   {
       printf("Argument is not valid.\n");
       return 0;
   }
   printf("num_students: %d, capacity: %d\n", num_students, office_capacity);

   sem_init(&OfficeSpots, 0, office_capacity);
   sem_init(&StudentCanAskQuestion, 0, 1);
   sem_init(&ProfessorCanSpeak, 0, 0);
   sem_init(&StudentCanSpeak, 0, 0);

   pthread_t professor_thread;
   pthread_create(&professor_thread, NULL, Professor, NULL);

   int student_num;
   pthread_t student_threads[num_students];
   int student_ids[num_students];

   for (student_num = 0; student_num < num_students; student_num++) {
       student_ids[student_num] = student_num;
       pthread_create(&student_threads[student_num], NULL, Student, (void *)&student_ids[student_num]);
   }

   for (student_num = 0; student_num < num_students; student_num++) {
       pthread_join(student_threads[student_num], NULL);
   }

   printf("Simulation completed. No more students left.\n");

   return 0;
}

void * Professor() {
   while(1) {
       sem_post(&StudentCanSpeak);
       sem_wait(&ProfessorCanSpeak);
       AnswerStart(current_student_id);
       AnswerDone(current_student_id);
       sem_post(&StudentCanSpeak);
   }
}

void * Student(void *id) {
   int student_id = *((int *) id);
   int n_questions = (student_id % 4) + 1;
   int quest;

   sem_wait(&OfficeSpots); // Wait for a spot in the office
   EnterOffice(student_id);

   for(quest = 0; quest < n_questions; quest++) {
       sem_wait(&StudentCanAskQuestion); // Wait for turn
       current_student_id = student_id;
       sem_wait(&StudentCanSpeak);
       QuestionStart(student_id);
       sem_post(&ProfessorCanSpeak); // Let professor answer

       sem_wait(&StudentCanSpeak);
       QuestionDone(student_id);

       sem_post(&StudentCanAskQuestion); // Let another student ask
   }

   sem_post(&OfficeSpots); // Let another student in the office
   LeaveOffice(student_id);   
}

// Professor Actions
void AnswerStart(int student_id) {
   printf("Professor starts to answer question for student %d.\n", student_id);
}
void AnswerDone(int student_id) {
   printf("Professor is done with answer for student %d.\n", student_id);
}

// Student Actions
void EnterOffice(int id) {
   printf("Student %d enters the office.\n", id);
}
void LeaveOffice(int id) {
   printf("Student %d leaves the office.\n", id);
}
void QuestionStart(int id) {
   printf("Student %d asks a question.\n", id);
}
void QuestionDone(int id) {
   printf("Student %d is satisfied.\n", id);
}