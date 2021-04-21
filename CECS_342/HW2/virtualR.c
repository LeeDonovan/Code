#include <stdio.h>
#include <stdlib.h>

struct Employee;
double GetPay_Hourly(struct Employee *e);
double GetPay_Commission(struct Employee *e);
double GetPay_Senior(struct Employee *e);

struct Employee{
    void** Vtable;
    int age; 
};
struct HourlyEmployee{
    void** Vt_Hourly;
    int age;
    double hourly_rate;
    double hours;
};

struct CommissionEmployee{
    void** Vt_Commission;
    int age; 
    double sales_amount;
};

struct SeniorEmployee{
    void** Vt_Senior;
    int age; 
    double sales_amount;
};

void Speak_Hourly( struct Employee *e){
    struct HourlyEmployee *he = (struct HourlyEmployee*) e;
    double amt = ((double (*)(struct Employee *))e->Vtable[1])(e);
    printf("I am %d years old working %.2f dollars per hour with a total of %.2f hours making a total of %.2f dollars.",he->age, he->hourly_rate, he->hours, amt);
    return;
}

void Speak_Commission(struct Employee *e){
    struct CommissionEmployee *ce = (struct CommissionEmployee*) e;
    double amt = ((double (*)(struct Employee *))e->Vtable[1])(e);
    if (ce->age >=50){
        printf("I am a senior salesman who made %.2f dollars in sales and a total of %.2f dollars!",ce->sales_amount, amt);
    }
    else{
        printf("I am a Commission Employee who made %.2f in sales and a total of %.2f dollars!",ce->sales_amount, amt);
    }
    }

void *Vtable_Hourly[] = {//virtual tables
    Speak_Hourly,
    GetPay_Hourly
};
void *Vtable_Commission[] = {
    Speak_Commission,
    GetPay_Commission
};

void *Vtable_Senior[] = {
    Speak_Commission,
    GetPay_Senior
};


double GetPay_Hourly(struct Employee *e)
{
    struct HourlyEmployee *he = (struct HourlyEmployee*) e;//cast employee to hrly employee
    double amt = he->hourly_rate * he->hours;//he->hourly_rate * he->hours
    return (amt);
}
double GetPay_Commission(struct Employee *e)
{
    struct CommissionEmployee *ce = (struct CommissionEmployee*) e;
    double amt = (0.1 * ce->sales_amount) + 40000;
    return (amt);
}

double GetPay_Senior(struct Employee *e){
    struct SeniorEmployee *se = (struct SeniorEmployee*) e;
    double amt = (0.2 * se->sales_amount) + 50000;
    if(se->age >= 50){
        amt = amt + (.05 * se->sales_amount);
    }
    return amt;
}

void Construct_Hourly(struct HourlyEmployee *he, int age, double hr, double hrs){
    he->age = age;
    he->hourly_rate = hr;
    he->hours = hrs;
    he->Vt_Hourly = Vtable_Hourly;
}
void Construct_Commission(struct CommissionEmployee *ce,int age, double sale){
    ce->age = age;
    ce->sales_amount = sale;
    ce->Vt_Commission = Vtable_Commission;
}

void Construct_Senior(struct SeniorEmployee *se,int age, double sale){
    se->age = age;
    se->sales_amount = sale;
    se->Vt_Senior = Vtable_Senior;
}



int main(){
    struct Employee *e;
    int user;
    int age = 0;
    printf("Choose which employee you want:\n");
    printf("1. Hourly Employee\n");
    printf("2. Commission Employee\n");
    printf("3. Senior Salesman\n");
    scanf("%d", &user);
    if (user == 1){
        double payRate = 0;
        double hours = 0;
        printf("Please enter employee's age:\n");
        scanf("%d", &age);
        printf("Please enter employee's pay rate:\n");
        scanf("%lf", &payRate);
        printf("Please enter employee's hours:\n");
        scanf("%lf", &hours);
        struct HourlyEmployee *h = (struct HourlyEmployee*)malloc(sizeof(struct HourlyEmployee));//create new memory for Employee
        Construct_Hourly(h, age, payRate, hours);//start adding values
        e = (struct Employee *)h;//cast values
        ((void (*)(struct Employee *))e->Vtable[0])(e);//calls function
    }
    if(user == 2){
        double sale_amt;
        printf("Please enter employee's age:\n");
        scanf("%d", &age);
        printf("Please enter employee's sale amount:\n");
        scanf("%lf", &sale_amt);
        struct CommissionEmployee *ce = (struct CommissionEmployee*)malloc(sizeof(struct CommissionEmployee));
        Construct_Commission(ce,age,sale_amt);
        e = (struct Employee *)ce;
        ((void (*)(struct Employee *))e->Vtable[0])(e);


    }
    if(user == 3){
        double sale_amt;
        printf("Please enter employee's age:\n");
        scanf("%d", &age);
        printf("Please enter employee's sale amount:\n");
        scanf("%lf", &sale_amt);
        struct SeniorEmployee *se = (struct SeniorEmployee*)malloc(sizeof(struct SeniorEmployee));
        Construct_Senior(se ,age, sale_amt);
        e = (struct Employee *)se;
        ((void (*)(struct Employee *))e->Vtable[0])(e);
    }
    return 0;
}
