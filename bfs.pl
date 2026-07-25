% Graph
edge(a,b).
edge(a,c).
edge(b,d).
edge(b,e).
edge(c,f).
edge(c,g).

% Goal node
goal(g).

% Best First Search
best_first(Node) :-
    goal(Node),
    write('Goal Found: '), write(Node).

best_first(Node) :-
    edge(Node,Next),
    best_first(Next).
