/*male*/
male(charles).
male(andrew).
male(edward).

/*female (Elizabeth is omitted for Approach 2)*/
female(ann).

/*elizabeth has four offspring*/
offspring(charles,elizabeth).
offspring(andrew,elizabeth).
offspring(edward,elizabeth).
offspring(ann,elizabeth).

/*List of elizabeth's children in order of birth*/
children([charles, ann, andrew, edward]).

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
isOlder(elizabeth, charles).
isOlder(charles,ann).
isOlder(ann,andrew).
isOlder(andrew,edward). 

/*A is older than C if A is older than B and B is older than C*/
olderThan(A,B) :- isOlder(A,B).
olderThan(A,C) :-
	isOlder(A,B),
	isOlder(B,C).

/*Order of precedence, prince come before princess and all order based on decreasing order of age*/
precedes(X,Y):-prince(X),princess(Y).
precedes(X,Y) :-prince(X), prince(Y), olderThan(X,Y).
precedes(X,Y) :-princess(X), princess(Y), olderThan(X,Y).


/* Approach 1: Establish Natural Order*/
insert(A,[B|C],[B|D]):-not(precedes(A,B)),!,insert(A,C,D).
insert(A,C,[A|C]).
succession_sort([A|B],SortList):-succession_sort(B,Tail),insert(A,Tail,SortList).
succession_sort([],[]).

/*Succession List*/
successionList(SuccessionList):-findall(Y,offspring(Y,_),ChildNodes),succession_sort(ChildNodes,SuccessionList).

/*Approach 2: Logical expression*/
successor(N):- ((male(K),not(female(N)),children(L), member(X, L), not(N=X), olderThan(N,X), (K=X)); (female(K), children(L), not(N=K), member(X, L), (K=X))) -> print(K),nl,successor(K).
