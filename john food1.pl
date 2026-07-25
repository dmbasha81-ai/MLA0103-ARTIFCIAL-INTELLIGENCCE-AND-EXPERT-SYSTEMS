% Facts
food(apple).
food(chicken).
food(peanuts).

% Rule
likes(john, X) :-
    food(X).
