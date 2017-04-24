"""
Description:


Pac-Man got lucky today! Due to minor performance issue all his enemies have frozen. Too bad Pac-Man is not brave enough to face them right now, so he doesn't want any enemy to see him.

Given a gamefield of size N x N, Pac-Man's position(PM) and his enemies' positions(enemies), your task is to count the number of coins he can collect without being seen.

An enemy can see a Pac-Man if they are standing on the same row or column.

It is guaranteed that no enemy can see Pac-Man on the starting position. There is a coin on each empty square (i.e. where there is no Pac-Man or enemy).
Example

For N = 4, PM = [3, 0], enemies = [[1, 2]], the result should be 3.

Let O represent coins, P - Pac-Man and E - enemy.
OOOO
OOEO
OOOO
POOO


Pac-Man cannot cross row 1 and column 2.

He can only collect coins from points (2, 0), (2, 1) and (3, 1), like this:

x is the points that Pac-Man can collect the coins.
OOOO
OOEO
xxOO
PxOO


Input/Output

[input] integer N

The field size.
[input] integer array PM

Pac-Man's position (pair of integers)
[input] 2D integer array enemies

Enemies' positions (array of pairs)
[output] an integer

Number of coins Pac-Man can collect.
"""


def pac_man(n, pm, enemies):
    pm_x, pm_y = pm
    e_x_low = e_y_low = -1
    e_x_high = e_y_high = n

    for e in enemies:
        e_x, e_y = e

        if e_x_low < e_x < pm_x:
            e_x_low = e_x
        elif e_x_high > e_x > pm_x:
            e_x_high = e_x

        if e_y_low < e_y < pm_y:
            e_y_low = e_y
        elif e_y_high > e_y > pm_y:
            e_y_high = e_y

    return (e_x_high - (e_x_low + 1)) * (e_y_high - (e_y_low + 1)) - 1


"""
BEST ANSWER:


def pac_man(N, PM, enemies):
    dims = [[0,N], [0,N]]   # [[minX, maxX], [minY, maxY]]
    for pos in enemies:
        for i,x in enumerate(pos):
            if PM[i] > x: dims[i][0] = max(dims[i][0], x+1)
            else:         dims[i][1] = min(dims[i][1], x)
    return (dims[0][1]-dims[0][0]) * (dims[1][1]-dims[1][0]) - 1



def pac_man(N, PM, enemies):
  mnr, mxr, mnc, mxc = 0, N-1 , 0, N-1
  pr, pc = PM
  for r, c in enemies:
      mnr, mxr = (max(mnr, r + 1), mxr) if r < pr else (mnr, min(mxr, r - 1))
      mnc, mxc = (max(mnc, c + 1), mxc) if c < pc else (mnc, min(mxc, c - 1))
  return max((1 + mxr - mnr)*(1 + mxc - mnc) - 1, 0)



def pac_man(N, PM, enemies):
  up,down,left,right,x,y=0,N-1,0,N-1,PM[0],PM[1]
  for n in enemies:
    if(n[0]<x and n[0]+1>up): up=n[0]+1
    if(n[0]>x and n[0]-1<down): down=n[0]-1
    if(n[1]<y and n[1]+1>left): left=n[1]+1
    if(n[1]>y and n[1]-1<right): right=n[1]-1
  return (down-up+1)*(right-left+1)-1
"""
