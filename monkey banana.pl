% Monkey can get the banana if it climbs on the box
can_get_banana :-
    monkey(atdoor),
    box(window),
    move(monkey, atdoor, window),
    push(box, window, center),
    climb,
    grasp.

% Facts
monkey(atdoor).
box(window).

% Actions
move(monkey, X, Y) :-
    write('Monkey moves from '), write(X),
    write(' to '), write(Y), nl.

push(box, X, Y) :-
    write('Monkey pushes box from '), write(X),
    write(' to '), write(Y), nl.

climb :-
    write('Monkey climbs on the box'), nl.

grasp :-
    write('Monkey grasps the banana'), nl.
