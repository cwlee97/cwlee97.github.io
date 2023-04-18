---
layout: single
title: Probability and Statistics
categories: Autonomous_Driving_course
---

# State Estimation
로봇이 스스로 현재 자신의 위치를 알아낼 수 없다. 그래서 우리는 로봇의 위치를 Planning 할 때, Error구간 내에 존재하는 로봇의 위치를 알아낸다.

# Probability Theory

## Axiom
$P(A)$ : A가 참일 경우 확률을 표현하는 방법<br><br>
$0{\leq}P(A)\leq1$<br><br>
$P(true) = 1$<br><br>
$P(false) = 0$<br><br>
$P(A{\cup}B) = P(A) + P(B) - P(A{\cap}B)$<br><br>
$P(A{\cup}A') = P(A) + P(A') - P(A{\cap}A')$<br><br>
$A' = not A$<br><br>

## Discrete random variable
$X = random\;variable$<br><br>
$X' = \{x_1, x_2, x_3, ... x_n\}$<br><br>
$P(X=x_i) = P(x_i)$<br><br>

## Continuous random variable
$Pr(x\in[a, b]) = \int\limits_a^bp(x)dx$<br><br>

## Joint and Conditional probability
$P(X=x\;and\;Y=y)=P(x, y)$<br><br>
if X and Y are independent, then $P(x, y) = P(x)P(y)$<br><br>
P(x|y) is the probability of X given Y<br>
$P(x, y) = P(x | y)P(y)$<br>
$P(x|y) = \frac{P(x, y)}{P(y)}$<br><br>
if X and Y are independent, then $P(x|y) = P(x)$