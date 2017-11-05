// Problem 1: What are the first and last values' outputs?

int num = 21;
while (num < 33) {
  System.out.println(num);
  num++;
}

//    num
// ---------
//     21
//     22
//     23
//     24
//     ..
//     32

// Answer: 21, 32





// Problem 2: What are the first and last values' outputs?

int num = 21;
while (num < 33) {
  System.out.println(num);
  num++;
}

//    num
// ---------
//     22
//     23
//     24
//     25
//     ..
//     32





// Problem 3: What does this do? Would this work if num was a double?

int num = 13475;
while (num != 0) {
  num = num / 10;
  System.out.println(num);
}

//    num
// ---------
//    1347
//    134
//    13
//    1
//    0

// Answer: No, the program would not work if num was a double.





// Problem 3: What is output to the screen by the following code:

int n = 3;
while (n < 7) {
    n++;
    System.out.print (n + " ");
}

//    num
// ---------
//     4
//     5
//     6
//     7

// Answer: 4 5 6 7





// Problem 4: What is output to the screen by the following code:

int n = 10;
while (5 < n) {
    n--;
    System.out.print (n + " ");
}

//    num
// ---------
//     9
//     8
//     7
//     6
//     5
// Answer: 9 8 7 6 5





// Problem 5: What are the first and last values printed by:

int n = 5;
while (n < 32) {
    n += 5;
    System.out.print (n + " ");
}

//    num
// ---------
//     10
//     15
//     20
//     25
//     30
//     35

// Answer: 10 35
