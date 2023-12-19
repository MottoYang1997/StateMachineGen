#include "my_state.h"

/* State Definition Begin */
void my_state_A(my_state_var_def * var);
void my_state_B(my_state_var_def * var);
void my_state_C(my_state_var_def * var);
void my_state_D(my_state_var_def * var);
/* State Definition End */

/* State Variable Begin */
my_state_var_def my_state_var = {my_state_A};
/* State Variable End */

/* State Implementation Begin */
void my_state_A(my_state_var_def * var)
{
    /* a */

    /* State Transition Begin */
    if(/* 1 */ 0)
    {
        var->current_state = my_state_B;
        return;
    }
    /* State Transition End */
}

void my_state_B(my_state_var_def * var)
{
    /* b */

    /* State Transition Begin */
    if(/* 1 */ 0)
    {
        var->current_state = my_state_C;
        return;
    }
    /* State Transition End */
}

void my_state_C(my_state_var_def * var)
{
    /* c */

    /* State Transition Begin */
    if(/* 1 */ 0)
    {
        var->current_state = my_state_D;
        return;
    }
    /* State Transition End */
}

void my_state_D(my_state_var_def * var)
{
    /* d */

    /* State Transition Begin */
    if(/* 1 */ 0)
    {
        var->current_state = my_state_A;
        return;
    }
    /* State Transition End */
}

/* State Implementation End */
