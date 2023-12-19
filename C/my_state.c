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

#include "my_state.h"

/* State Definition Begin */
void my_state_A(my_state_var_def * var);
void my_state_B(my_state_var_def * var);
/* State Definition End */

/* State Variable Begin */
my_state_var_def my_state_var = {my_state_A};
/* State Variable End */

/* State Implementation Begin */
void my_state_A(my_state_var_def * var)
{

    /* State Transition Begin */
    if(1)
    {
        var->current_state = my_state_B;
        return;
    }
    /* State Transition End */
}

void my_state_B(my_state_var_def * var)
{

    /* State Transition Begin */
    if(1)
    {
        var->current_state = my_state_A;
        return;
    }
    /* State Transition End */
}

/* State Implementation End */
