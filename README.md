# SeqU #

Extended implemenation of the Unix seq command

## usage ##

usage: sequ.py [-h] [--version] [-s STRING | -W]  
               [-f FORMAT | -p CHAR | -P | -w]  
               [FIRST] [INCREMENT] LAST  

Print numbers from FIRST to LAST, in steps of INCREMENT  

positional arguments:  
  FIRST                 The first number  
  INCREMENT             The step size  
  LAST                  The last number  

optional arguments:  
  -h, --help            show this help message and exit  
  --version             show program's version number and exit  
  -s STRING, --separator STRING  
                        use the STRING to separate numbers  
  -W, --words           Output the sequence as a single space-separeted line  
                        of words  
  -f FORMAT, --format FORMAT  
                        use python format style floating-point FORMAT  
  -p CHAR, --pad CHAR   equalize width by padding with the padding provided  
  -P, --pad-spaces      equalize width by padding with leading spaces  
  -w, --equal-width     equalize width by padding with leading zeroes  

## examples ##

```sh
$ ./sequ.py 0 5
0
1
2
3
4
5

$ ./sequ.py 0.0 5.0
0.0
1.0
2.0
3.0
4.0
5.0

$ ./sequ.py 1 2 10
1
3
5
7
9

$ ./sequ.py --equal-width 10.0 33 100
10.0
43.0
76.0

$ ./sequ.py --separator ':' 1 10
1:2:3:4:5:6:7:8:9:10

$ ./sequ.py --format ':3.1E' 100000 100000 300000.0
1.0E+05
2.0E+05
3.0E+05

$ ./sequ.py --words 10
1 2 3 4 5 6 7 8 9 10

$ ./sequ.py --pad-spaces 4.0
1.0
2.0
3.0
4.0

$ ./sequ.py --pad a 5.0 4 15
a5.0
a9.0
13.0

$ ./sequ.py --words --pad a 5.0 4 15
a5.0 a9.0 13.0
```
