Part 1 - Identify logic and robustness

1. If we use negative numbers with the payment function, the money will be deducted to the receiver and added to the caller
2. The function doesnt check if the caller has enough the money 
3. The program crash

Part 2 - Identify security vulnerability
1. Theses 2 functions dont check who is the caller. Anyone can use them, that s dangerous
2. Same for the request_refund => Anyone can ask for any amount of refund
3. Because the code doesnt use it. Logs are useful to track who did what, so it has to be use
4. Because the transaction is made before checking if the money is available. The receiver receives the money before 

Part 3 - 
