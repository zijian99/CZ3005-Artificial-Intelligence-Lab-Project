
/*sumsum is company*/
company(sumsum).
	
/*appy is company*/
company(appy).

/*sumsum is competitor of appy*/
competitor(sumsum,appy).
/*competitor(Y,X):-
	competitor(X,Y).*/

/*if company is competitor then they are rival*/
rival(X,Y):-
	competitor(X,Y).

/*rival and competitor with each other*/
/*rival(Y,X):-
	rival(X,Y).*/



/*sumsum develop galactica-s3*/
develop(sumsum,galactica-s3).

/*stevey is boss*/
boss(stevey).

/*stevey works in works in appy */
works(stevey,appy).

/*stevey steal galactica-s3*/
steal(stevey,galactica-s3).

/*galactica-s3 is smart phone tech*/
smartphonetech(galactica-s3).

/*X is a business if it is a smart phone tech*/
business(X):-
	smartphonetech(X).

/*X is unethical if X steals something from rival company*/
unethical(X):-
	boss(X),
	steal(X,Y),
	business(Y),
	develop(A,Y),
	works(X,B),
	(rival(A,B);rival(B,A)).
