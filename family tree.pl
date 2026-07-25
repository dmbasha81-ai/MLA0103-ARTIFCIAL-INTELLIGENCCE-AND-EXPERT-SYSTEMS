% Gender
female(pam).
female(liz).
female(ann).
female(pat).

male(tom).
male(bob).
male(jim).

% Parent relationships
parent(tom, bob).
parent(pam, bob).

parent(tom, liz).
parent(pam, liz).

parent(bob, ann).
parent(pat, ann).

parent(bob, jim).
parent(pat, jim).

% Mother
mother(X,Y) :-
    parent(X,Y),
    female(X).

% Father
father(X,Y) :-
    parent(X,Y),
    male(X).

% Grandfather
grandfather(X,Y) :-
    parent(X,Z),
    parent(Z,Y),
    male(X).

% Grandmother
grandmother(X,Y) :-
    parent(X,Z),
    parent(Z,Y),
    female(X).

% Sister
sister(X,Y) :-
    parent(P,X),
    parent(P,Y),
    female(X),
    X \= Y.

% Brother
brother(X,Y) :-
    parent(P,X),
    parent(P,Y),
    male(X),
    X \= Y.
