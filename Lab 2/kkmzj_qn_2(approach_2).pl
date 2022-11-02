parent(elizabeth, charles).
parent(elizabeth, ann).
parent(elizabeth, andrew).
parent(elizabeth, edward).
male(charles).
male(andrew).
male(edward).
female(ann).
children([charles, ann, andrew, edward]).

older_than(elizabeth, charles).
older_than(charles, ann).
older_than(ann, andrew).
older_than(andrew, edward).
olderThan(X,Y):- older_than(X,Y).
olderThan(X,Z):- older_than(X,Y), older_than(Y,Z).

successor(N):- (((male(K), not(female(N)),children(L), member(X, L), not(N=X), olderThan(N,X), (K=X))); ((female(K), children(L), not(N=K), member(X, L), (K=X)))) -> print(K),nl,successor(K).

successorGenderEquality(N):- (children(L), member(X, L), not(N=X), olderThan(N,X), (K=X)) -> print(K),nl,successorGenderEquality(K).