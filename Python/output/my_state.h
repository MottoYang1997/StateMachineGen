#ifndef __MY_STATE_H__
#define __MY_STATE_H__

typedef struct my_state_var
{
    void (* current_state)(struct my_state_var * var);

    /* State Machine Variables Begin */
     int var_a;
     float var_b;
     unsigned char var_c[10];
    /* State Machine Variables End */

} my_state_var_def;

extern my_state_var_def my_state_var;

#endif
