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
    double amt = ((double (*)(struct Employee *))e->Vtable[1])(e);
    printf("I work for %f dollars per hour.", amt);
    return;
}

void Speak_Commission(struct Employee *e){
    struct CommissionEmployee *ce = (struct CommissionEmployee*) &e;
    printf("I work for %lf dollars in sales!", ce);
}

void *Vtable_Hourly[] = {
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
    struct HourlyEmployee *he = (struct HourlyEmployee*) e;
    printf("Age: %d\n",he->age);
    printf("HH = %lf\n", he->hourly_rate);
    double amt = he->hourly_rate * he->hours;//he->hourly_rate * he->hours
    printf("%lf\n",amt);
    return (amt);
}
double GetPay_Commission(struct Employee *e)
{
    struct CommissionEmployee *ce = (struct CommissionEmployee*) &e;
    double amt = (0.1 * ce->sales_amount) + 40000;
    return (amt);
}

double GetPay_Senior(struct Employee *e){
    struct SeniorEmployee *se = (struct SeniorEmployee*) &e;
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
void Construct_Commission(struct CommissionEmployee *ce){
    ce->age = 0;
    ce->sales_amount = 0;
    ce->Vt_Commission = Vtable_Commission;
}

void Construct_Senior(struct SeniorEmployee *se){
    se->age = 0;
    se->sales_amount = 0;
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
        //#if 0
        double payRate = 0;
        double hours = 0;
        printf("Please enter employee's age:\n");
        scanf("%d", &age);
        printf("Please enter employee's pay rate:\n");
        scanf("%lf", &payRate);
        printf("Please enter employee's hours:\n");
        scanf("%lf", &hours);
        struct HourlyEmployee *h = (struct HourlyEmployee*)malloc(sizeof(struct HourlyEmployee));
        Construct_Hourly(h, age, payRate, hours);
        printf("Age: %d, HR: %lf, Hrs: %lf\n", h->age, h->hourly_rate, h->hours);
        e = (struct Employee *)h;
        //#endif
        ((void (*)(struct Employee *))e->Vtable[0])(e);
    }
    if(user == 2){
        double sale_amt;
        printf("Please enter employee's age:\n");
        scanf("%d", &age);
        printf("Please enter employee's sale amount:\n");
        scanf("%d", &sale_amt);
    }
    if(user == 3){
        double sale_amt;
        printf("Please enter employee's age:\n");
        scanf("%d", &age);
        printf("Please enter employee's sale amount:\n");
        scanf("%d", &sale_amt);
    }
    return 0;
}
