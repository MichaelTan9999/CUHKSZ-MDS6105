## Example 9

| $p$  | $q$  | $r$  | $p\vee\neg q$ | $q\vee\neg r$ | $r\vee\neg p$ | $p\vee q\vee r$ | $\neg p\vee\neg q\vee\neg r$ |
| ---- | ---- | ---- | ------------- | ------------- | ------------- | --------------- | ---------------------------- |
| T    | T    | T    | T             | T             | T             | T               | F                            |
| T    | T    | F    | T             | T             | F             | T               | T                            |
| T    | F    | T    | T             | F             | T             | T               | T                            |
| T    | F    | F    | T             | T             | F             | T               | T                            |
| F    | T    | T    | F             | T             | T             | T               | T                            |
| F    | T    | F    | F             | T             | T             | T               | T                            |
| F    | F    | T    | T             | F             | T             | T               | T                            |
| F    | F    | F    | T             | T             | T             | F               | T                            |

| $(p\vee\neg q)\wedge(q\vee\neg r)\wedge(r\vee\neg p)$ | $(p\vee q\vee r)\wedge(\neg p\vee\neg q\vee\neg r)$ | $(p\vee\neg q)\wedge(q\vee\neg r)\wedge(r\vee\neg p)\wedge(p\vee q\vee r)\wedge(\neg p\vee\neg q\vee\neg r)$ |
| ----------------------------------------------------- | --------------------------------------------------- | ------------------------------------------------------------ |
| T                                                     | F                                                   | F                                                            |
| F                                                     | T                                                   | F                                                            |
| F                                                     | T                                                   | F                                                            |
| F                                                     | T                                                   | F                                                            |
| F                                                     | T                                                   | F                                                            |
| F                                                     | T                                                   | F                                                            |
| F                                                     | T                                                   | F                                                            |
| T                                                     | F                                                   | F                                                            |

## Question 58

| $p$  | $q$  | $r$  | $p\vee\neg q$ | $\neg p\vee q$ | $q\vee r$ | $q\vee\neg r$ | $\neg q\vee\neg r$ |
| ---- | ---- | ---- | ------------- | -------------- | --------- | ------------- | ------------------ |
| T    | T    | T    | T             | T              | T         | T             | F                  |
| T    | T    | F    | T             | T              | T         | T             | T                  |
| T    | F    | T    | T             | F              | T         | F             | T                  |
| T    | F    | F    | T             | F              | F         | T             | T                  |
| F    | T    | T    | F             | T              | T         | T             | F                  |
| F    | T    | F    | F             | T              | T         | T             | T                  |
| F    | F    | T    | T             | T              | T         | F             | T                  |
| F    | F    | F    | T             | T              | F         | T             | T                  |

## Question 59

| $p$  | $q$  | $r$  | $s$  | $\neg p$ | $\neg q$ | $\neg r$ | $\neg s$ |
| ---- | ---- | ---- | ---- | -------- | -------- | -------- | -------- |
| T    | T    | T    | T    | F        | F        | F        | F        |
| T    | T    | T    | F    | F        | F        | F        | T        |
| T    | T    | F    | T    | F        | F        | T        | F        |
| T    | T    | F    | F    | F        | F        | T        | T        |
| T    | F    | T    | T    | F        | T        | F        | F        |
| T    | F    | T    | F    | F        | T        | F        | T        |
| T    | F    | F    | T    | F        | T        | T        | F        |
| T    | F    | F    | F    | F        | T        | T        | T        |
| F    | T    | T    | T    | T        | F        | F        | F        |
| F    | T    | T    | F    | T        | F        | F        | T        |
| F    | T    | F    | T    | T        | F        | T        | F        |
| F    | T    | F    | F    | T        | F        | T        | T        |
| F    | F    | T    | T    | T        | T        | F        | F        |
| F    | F    | T    | F    | T        | T        | F        | T        |
| F    | F    | F    | T    | T        | T        | T        | F        |
| F    | F    | F    | F    | T        | T        | T        | T        |

| $p\vee\neg q\vee s$ | $\neg p\vee\neg r\vee s$ | $\neg p\vee\neg r\vee\neg s$ | $\neg p\vee q\vee\neg s$ | $q\vee r\vee\neg s$ | $q\vee\neg r\vee\neg s$ | $\neg p\vee\neg q\vee\neg s$ | $p\vee r\vee s$ | $p\vee r\vee \neg s$ |
| ------------------- | ------------------------ | ---------------------------- | ------------------------ | ------------------- | ----------------------- | ---------------------------- | --------------- | -------------------- |
| T                   | T                        | F                            | T                        | T                   | T                       | F                            | T               | T                    |
| T                   | F                        | T                            | T                        | T                   | T                       | T                            | T               | T                    |
| T                   | T                        | T                            | T                        | T                   | T                       | F                            | T               | T                    |
| T                   | T                        | T                            | T                        | T                   | T                       | T                            | T               | T                    |
| T                   | T                        | F                            | T                        | T                   | F                       | T                            | T               | T                    |
| T                   | F                        | T                            | F                        | T                   | T                       | T                            | T               | T                    |
| T                   | F                        | T                            | T                        | F                   | T                       | T                            | T               | T                    |
| T                   | T                        | T                            | F                        | T                   | T                       | T                            | T               | T                    |
| T                   | T                        | T                            | T                        | T                   | T                       | T                            | T               | T                    |
| F                   | T                        | T                            | T                        | T                   | T                       | T                            | T               | T                    |
| T                   | T                        | T                            | T                        | T                   | T                       | T                            | T               | F                    |
| F                   | T                        | T                            | T                        | T                   | T                       | T                            | F               | T                    |
| T                   | T                        | T                            | T                        | T                   | F                       | T                            | T               | T                    |
| T                   | T                        | T                            | T                        | T                   | T                       | T                            | T               | T                    |
| T                   | T                        | T                            | T                        | F                   | T                       | T                            | T               | F                    |
| T                   | T                        | T                            | T                        | T                   | T                       | T                            | F               | T                    |

## Question 60

A proposition is a tautology, if the proposition is always true, which means that the proposition is equivalent to True. In return the negation of a tautology is the negation of true, which is False.

A proposition is an unsatisfiable compound, if the proposition is always false, which means that the proposition is equivalent to False. In return the negation of an unsatisfiable compound is the negation of False, which is True.

## Question 61

### a)

| $p$  | $q$  | $p\vee\neg q$ | $\neg p\vee q$ | $\neg p\vee\neg q$ | $(p\vee\neg q)\wedge(\neg p\vee q)\wedge(\neg p\vee\neg q)$ |
| ---- | ---- | ------------- | -------------- | ------------------ | ----------------------------------------------------------- |
| T    | T    | T             | T              | F                  | F                                                           |
| T    | F    | T             | F              | T                  | F                                                           |
| F    | T    | F             | T              | T                  | F                                                           |
| F    | F    | T             | T              | T                  | T                                                           |

### b)

| $p$  | $q$  | $p\rightarrow q$ | $p\rightarrow\neg q$ | $\neg p\rightarrow q$ | $\neg p\rightarrow\neg q$ | $(p\rightarrow q)\wedge(p\rightarrow\neg q)\wedge(\neg p\rightarrow q)\wedge(\neg p\rightarrow\neg q)$ |
| ---- | ---- | ---------------- | -------------------- | --------------------- | ------------------------- | ------------------------------------------------------------ |
| T    | T    | T                | F                    | T                     | T                         | F                                                            |
| T    | F    | F                | T                    | T                     | T                         | F                                                            |
| F    | T    | T                | T                    | T                     | F                         | F                                                            |
| F    | F    | T                | T                    | F                     | T                         | F                                                            |

### c)

| $p$  | $q$  | $p\leftrightarrow q$ | $\neg p\leftrightarrow q$ | $(p\leftrightarrow q)\wedge(\neg p\leftrightarrow q)$ |
| ---- | ---- | -------------------- | ------------------------- | ----------------------------------------------------- |
| T    | T    | T                    | F                         | F                                                     |
| T    | F    | F                    | T                         | F                                                     |
| F    | T    | F                    | T                         | F                                                     |
| F    | F    | T                    | F                         | F                                                     |

## Question 62

### a)

| $p$  | $q$  | $r$  | $s$  | $\neg p$ | $\neg q$ | $\neg r$ | $\neg s$ |
| ---- | ---- | ---- | ---- | -------- | -------- | -------- | -------- |
| T    | T    | T    | T    | F        | F        | F        | F        |
| T    | T    | T    | F    | F        | F        | F        | T        |
| T    | T    | F    | T    | F        | F        | T        | F        |
| T    | T    | F    | F    | F        | F        | T        | T        |
| T    | F    | T    | T    | F        | T        | F        | F        |
| T    | F    | T    | F    | F        | T        | F        | T        |
| T    | F    | F    | T    | F        | T        | T        | F        |
| T    | F    | F    | F    | F        | T        | T        | T        |
| F    | T    | T    | T    | T        | F        | F        | F        |
| F    | T    | T    | F    | T        | F        | F        | T        |
| F    | T    | F    | T    | T        | F        | T        | F        |
| F    | T    | F    | F    | T        | F        | T        | T        |
| F    | F    | T    | T    | T        | T        | F        | F        |
| F    | F    | T    | F    | T        | T        | F        | T        |
| F    | F    | F    | T    | T        | T        | T        | F        |
| F    | F    | F    | F    | T        | T        | T        | T        |

| $p\vee q\vee\neg r$ | $p\vee\neg q\vee\neg s$ | $p\vee\neg r\vee\neg s$ | $\neg p\vee\neg  q\vee\neg s$ | $p\vee q\vee\neg s$ | $(p\vee q\vee\neg r)\wedge(p\vee\neg q\vee\neg s)\wedge(p\vee\neg r\vee\neg s)\wedge(\neg p\vee\neg  q\vee\neg s)\wedge(p\vee q\vee\neg s)$ |
| ------------------- | ----------------------- | ----------------------- | ----------------------------- | ------------------- | ------------------------------------------------------------ |
| T                   | T                       | F                       | F                             | T                   | F                                                            |
| T                   | T                       | T                       | T                             | T                   | T                                                            |
| T                   | T                       | T                       | F                             | T                   | F                                                            |
| T                   | T                       | T                       | T                             | T                   | T                                                            |
| T                   | T                       | F                       | T                             | T                   | F                                                            |
| T                   | T                       | T                       | T                             | T                   | T                                                            |
| T                   | T                       | T                       | T                             | T                   | T                                                            |
| T                   | T                       | T                       | T                             | T                   | T                                                            |
| T                   | F                       | T                       | T                             | T                   | F                                                            |
| T                   | T                       | T                       | T                             | T                   | T                                                            |
| T                   | F                       | T                       | T                             | T                   | F                                                            |
| T                   | T                       | T                       | T                             | T                   | T                                                            |
| F                   | T                       | T                       | T                             | F                   | F                                                            |
| F                   | T                       | T                       | T                             | T                   | F                                                            |
| T                   | T                       | T                       | T                             | F                   | F                                                            |
| T                   | T                       | T                       | T                             | T                   | T                                                            |

### b)

| $\neg p\vee\neg q\vee r$ | $\neg p\vee q\vee\neg s$ | $p\vee\neg q\vee\neg s$ | $\neg p\vee\neg  r\vee\neg s$ | $p\vee q\vee\neg r$ | $p\vee\neg r\vee\neg s$ | $(\neg p\vee\neg q\vee r)\wedge(\neg p\vee q\vee\neg s)\wedge(p\vee\neg q\vee\neg s)\wedge(\neg p\vee\neg  r\vee\neg s)\wedge(p\vee q\vee\neg r)\wedge(p\vee\neg r\vee\neg s)$ |
| ------------------------ | ------------------------ | ----------------------- | ----------------------------- | ------------------- | ----------------------- | ------------------------------------------------------------ |
| T                        | T                        | T                       | F                             | T                   | T                       | F                                                            |
| T                        | T                        | T                       | T                             | T                   | T                       | T                                                            |
| F                        | T                        | T                       | T                             | T                   | T                       | F                                                            |
| F                        | T                        | T                       | T                             | T                   | T                       | F                                                            |
| T                        | F                        | T                       | F                             | T                   | T                       | F                                                            |
| T                        | T                        | T                       | T                             | T                   | T                       | T                                                            |
| T                        | F                        | T                       | T                             | T                   | T                       | F                                                            |
| T                        | T                        | T                       | T                             | T                   | T                       | T                                                            |
| T                        | T                        | F                       | T                             | T                   | F                       | F                                                            |
| T                        | T                        | T                       | T                             | T                   | T                       | T                                                            |
| T                        | T                        | F                       | T                             | T                   | T                       | F                                                            |
| T                        | T                        | T                       | T                             | T                   | T                       | T                                                            |
| T                        | T                        | T                       | T                             | F                   | F                       | F                                                            |
| T                        | T                        | T                       | T                             | F                   | T                       | F                                                            |
| T                        | T                        | T                       | T                             | T                   | T                       | T                                                            |
| T                        | T                        | T                       | T                             | T                   | T                       | T                                                            |

### c)

| $p\vee q\vee r$ | $p\vee\neg q\vee\neg s$ | $q\vee\neg r\vee s$ | $\neg p\vee  r\vee s$ | $\neg p\vee q\vee\neg s$ | $p\vee\neg q\vee\neg r$ | $\neg p\vee\neg q\vee s$ | $\neg p\vee\neg r\vee\neg s$ | $(p\vee q\vee r)\wedge(p\vee\neg q\vee\neg s)\wedge(q\vee\neg r\vee s)\wedge(\neg p\vee  r\vee s)\wedge(\neg p\vee  r\vee s)\wedge(p\vee\neg q\vee\neg r)\wedge(\neg p\vee\neg q\vee s)\wedge(\neg p\vee\neg r\vee\neg s)$ |
| --------------- | ----------------------- | ------------------- | --------------------- | ------------------------ | ----------------------- | ------------------------ | ---------------------------- | ------------------------------------------------------------ |
| T               | T                       | T                   | T                     | T                        | T                       | T                        | F                            | F                                                            |
| T               | T                       | T                   | T                     | T                        | T                       | F                        | T                            | F                                                            |
| T               | T                       | T                   | T                     | T                        | T                       | T                        | T                            | T                                                            |
| T               | T                       | T                   | F                     | T                        | T                       | F                        | T                            | F                                                            |
| T               | T                       | T                   | T                     | F                        | T                       | T                        | F                            | F                                                            |
| T               | T                       | F                   | T                     | T                        | T                       | T                        | T                            | F                                                            |
| T               | T                       | T                   | T                     | F                        | T                       | T                        | T                            | F                                                            |
| T               | T                       | T                   | F                     | T                        | T                       | T                        | T                            | F                                                            |
| T               | F                       | T                   | T                     | T                        | F                       | T                        | T                            | F                                                            |
| T               | T                       | T                   | T                     | T                        | F                       | T                        | T                            | F                                                            |
| T               | F                       | T                   | T                     | T                        | T                       | T                        | T                            | F                                                            |
| T               | T                       | T                   | T                     | T                        | T                       | T                        | T                            | T                                                            |
| T               | T                       | T                   | T                     | T                        | T                       | T                        | T                            | T                                                            |
| T               | T                       | F                   | T                     | T                        | T                       | T                        | T                            | F                                                            |
| F               | T                       | T                   | T                     | T                        | T                       | T                        | T                            | F                                                            |
| F               | T                       | T                   | T                     | T                        | T                       | T                        | T                            | F                                                            |
