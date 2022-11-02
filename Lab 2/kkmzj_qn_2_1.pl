/*male*/
male(charles).
male(andrew).
male(edward).

/*female*/
female(elizabeth).
female(ann).

/*elizabeth has four offspring*/
offspring(charles,elizabeth).
offspring(andrew,elizabeth).
offspring(edward,elizabeth).
offspring(ann,elizabeth).

/*elizabeth is queen*/
queen(elizabeth).

/*X is parent of Y if Y is offspring of X*/
parentOf(X,Y):-offspring(Y,X).

/*X is prince if X has is parent that is king or queen and X is male*/
prince(Y):-
	parentOf(X,Y),
	queen(X),
	male(Y).

/*X is princess if X has is parent that is king or queen and X is female*/
princess(Y):-
	parentOf(X,Y),
	queen(X),
	female(Y).


/*who is older*/
isOlder(charles,ann).
isOlder(ann,andrew).
isOlder(andrew,edward). 

/*A is older than B if A is older than C and C is older than B*/
olderThan(A,B) :- isOlder(A,B).
olderThan(A,B) :-
	isOlder(A,C),
	isOlder(C,B).

/*Order of precedence, prince come before princess and all order based on decreasing order of age*/
precedes(X,Y):-prince(X),princess(Y).
precedes(X,Y) :-prince(X), prince(Y), olderThan(X,Y).
precedes(X,Y) :-princess(X), princess(Y), olderThan(X,Y).


/*Succession Sort*/ 
insert(A,[B|C],[B|D]):-not(precedes(A,B)),!,insert(A,C,D).
insert(A,C,[A|C]).
succession_sort([A|B],SortList):-succession_sort(B,Tail),insert(A,Tail,SortList).
succession_sort([],[]).

/*Succession List*/
successionList(SuccessionList):-findall(Y,offspring(Y,_),ChildNodes),succession_sort(ChildNodes,SuccessionList).


