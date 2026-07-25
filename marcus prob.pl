% Facts
man(marcus).
pompeian(marcus).
ruler(caesar).
tried(marcus, caesar).

% Rules
roman(X) :- pompeian(X).
person(X) :- man(X).
hates(X, caesar) :- tried(X, caesar).
