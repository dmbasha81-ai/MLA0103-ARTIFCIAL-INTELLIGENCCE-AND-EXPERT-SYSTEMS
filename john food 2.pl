% Facts
food(apple).
food(vegetable).

eats(anil, peanuts).
alive(anil).

eats(harry, X) :- eats(anil, X).

% Rule
food(X) :- eats(_, X).

likes(john, X) :- food(X).

likes(john, peanuts).
