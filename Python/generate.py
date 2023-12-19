"""
    State Machine Generator  
        Python implementation of a State Machine Generator
    Copyright (C) 2023 YimingYang

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.
"""


import argparse


def parse_input():
    parser = argparse.ArgumentParser(description="C State Machine Generator")
    # Example Call "python generate.py -s state_def.csv -v var_def.csv -o my_state"
    parser.add_argument("-s", "--state", type=str, default="state_def.csv", help="state definition csv file")
    parser.add_argument("-v", "--var", type=str, default="var_def.csv", help="variable definition csv file")
    parser.add_argument("-n", "--name", type=str, default="my_state", help="state machine name")
    parser.add_argument("-d", "--debugging", type=int, default="0", help="debugging flag, 0 = disabled")

    return parser.parse_args()


def clean_str(x: str) -> str:
    return x.replace('\n', "").replace('\t', "").replace(' ', "")


def clean_str_keep_inner_spaces(x: str) -> str:
    return x.replace('\n', "").replace('\t', "").lstrip().rstrip()


def read_var_type_dict(var_filename) -> dict[str, str]:
    var_type_dict = {}
    with open(var_filename) as file:
        input = file.readlines()
    # input format: ["A, int\n", "B, float\n", ""]
    for var in input:
        try:
            new_var = clean_str_keep_inner_spaces(var).split(',')
            var_type_dict[new_var[0]] = new_var[1]
        except:
            continue
    return var_type_dict


def read_state_dict(state_filename) -> dict[str, list]:
    state_dict = {}
    with open(state_filename) as file:
        states = clean_str(file.readline()).split(',')[1::]
        for state in states:
            try:
                state_dict[state] = {}
                for i, transition in enumerate(clean_str(file.readline()).split(',')[1::]):
                    state_dict[state][states[i]] = transition
            except ValueError or IndexError:
                continue
    return state_dict


def generate_main(var_type_dict, state_dict, name: str):
    lines = \
"""#include "%s.h"

void main()
{
    while(1)
    {
        %s_var.current_state(&%s_var);
    }
}

""" % (name, name, name)

    file = open("./output/main.c", 'w')
    file.write(lines)
    file.close()


def generate_header(var_type_dict, state_dict, name: str):
    lines = \
"""#ifndef __%s_H__
#define __%s_H__

typedef struct %s_var
{
    void (* current_state)(struct %s_var * var);

    /* State Machine Variables Begin */
""" % (name.upper(), name.upper(), name, name)

    for var in var_type_dict:
        lines += "    %s %s;\n" % (var_type_dict[var], var)

    lines += \
"""    /* State Machine Variables End */

} %s_var_def;

extern %s_var_def %s_var;

#endif
""" % (name, name, name)

    file = open(f"./output/{name}.h", 'w')
    file.write(lines)
    file.close()


def generate_source(var_type_dict: dict, state_dict: dict, name: str):
    lines = \
"""#include "%s.h"

/* State Definition Begin */
""" % (name)
    
    for state in state_dict:
        lines += "void %s_%s(%s_var_def * var);\n" % (name, state, name)

    lines += \
"""/* State Definition End */

/* State Variable Begin */
%s_var_def %s_var = {%s_%s};
/* State Variable End */

/* State Implementation Begin */
""" % (name, name, name, list(state_dict.keys())[0])

    for state in state_dict:
        lines += """void %s_%s(%s_var_def * var)
{
""" % (name, state, name)

        if state_dict[state][state] != "":
            lines += "    /* %s */\n" % (state_dict[state][state])

        lines += """
    /* State Transition Begin */"""

        for destnation in state_dict[state]:
            condition = state_dict[state][destnation]
            if condition != "" and state != destnation:
                lines += """
    if(/* %s */ 0)
    {
        var->current_state = %s_%s;
        return;
    }
    """ % (condition, name, destnation)
        lines += \
    """/* State Transition End */
}

"""

    lines += "/* State Implementation End */\n"

    file = open(f"./output/{name}.c", 'w')
    file.write(lines)
    file.close()


args = parse_input()
var_type_dict = read_var_type_dict(args.var)
state_dict = read_state_dict(args.state)

if(args.debugging != 0):
    print(var_type_dict)
    print(state_dict)

generate_main(var_type_dict, state_dict, args.name)
generate_header(var_type_dict, state_dict, args.name)
generate_source(var_type_dict, state_dict, args.name)
