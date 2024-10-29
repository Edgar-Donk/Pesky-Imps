=======
General
=======

The While Loop
==============

When iterating we generally have no real idea of how long it will last, so
a **do** loop with its set number of iterations doesn't cut the mustard. 
Instead use a while loop with the ending condition(s) stated. Avoid **while True:**
or the slightly faster **while 1:** with controlling **if** clauses, while
and its conditions easily takes care of the situation. The only slight
problem is to ensure that the loop conditions will run, so the starting
conditions should satisfy the first run of the while loop.

Remember that the while conditions are satisfied as the iterations progress,
and once the target value is achieved the loop is ended. Compare the 
conditional part of the **if** statement and the equivalent **while** loop::

    for x in (mylist):
        .......
        do something
        .......
        if myint > 9:
            break

    while myint < 11:
        ........
        do something
        ........

The condition has the opposite sense, the if statement prevents the myint
from exceeding the limit whereas while allows myint to increase up to the
limit. In both snippets when myint reaches 10 the loop will end.

When setting the condition remember that unless the loop fulfills the 
condition it will not end, it is safer to add a counter to the condition
that stops the loop after a number of iterations with an **and** operator
between the two conditions::

    myint = 5
    step = 0    # our counter
    while myint < 11 and step < 19:
        ........
        do something
        ........
        step += 1   # the counter increases by 1 at the end of the loop

The loop now stops whenever either of the two components in the loop is 
satisfied. As both condition components are True at initialisation the loop
continues to run until one of the conditions is False. 

PrettyTable
===========

This module was used extensively in the iterations to produce a tabular
display of the relevant variables and their progressive changes. First import
the module then setup the table before an interpolation function is called,
after the initialisation and before the main loop save the initialisation
conditions. At the loop end save the variable values::

    from prettytable import PrettyTable
    
    def myfunc(a, b, ...z):
        ........
        myint = 5
        step = 0
        pt.add_row([step, myint, a, ... ,None,... z])
        while myint < 11 and step < 19:
            ........
            do something
            ........
            step += 1
            pt.add_row([step, myint, a, ... z])
        return step, myint, ...
    
    pt = PrettyTable(['step', 'myint', 'a', ... , 'z'])
    a = ...
    ...
    z = ...
    step, myint, ... = myfunc(a,b,...z)
    print(pt)
    print('other stuff', ...)

The table setup::

    pt = PrettyTable(['step', 'myint', 'a', ... , 'z'])

gives the table column names corresponding to the variable names to be
monitored. The first::

    pt.add_row([step, myint, a, ... ,None,... z])

add_row command corresponds to the initialisation data, if any column has
not yet been computed insert **None** into that column, so we maintain a
place holder. The next add_row command is the main information gathering
part, it is placed after the counter has been increased at the end of the
loop. All the columns should have information.

PrettyTable is versatile so read its `documents <https://github.com/jazzband/prettytable>`_ 
to see what else it can do.

Those Pesky Imps
================

Just in case you were wondering what the skipper has been hopping mad about - 
it's those implicit equations.