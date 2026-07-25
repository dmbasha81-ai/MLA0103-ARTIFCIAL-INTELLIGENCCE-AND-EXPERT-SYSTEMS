% Facts
fact(fever).
fact(cough).

% Rules
disease(flu) :-
    fact(fever),
    fact(cough).

diagnosis :-
    disease(X),
    write('Possible Disease: '),
    write(X).
