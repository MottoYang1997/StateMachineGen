/*
    State Machine Generator  
        Simplistic C Implementation of a state machine
    Copyright (C) 2023 YimingYang

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.
*/

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
