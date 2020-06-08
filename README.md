# Setup this repo
1. Create a parent folder for this repo. `mkdir template_trunk`
2. initialize it as a virtual environment. `virtualenv --python=python3 template_trunk`
3. navigate into parent `cd template_trunk`
4. clone the repo: `git clone git@github.com:ianliu-johnston/template.git`
5. navigate into repo: `cd template`
6. activate the virtual env: `source ../bin/activate`
7. link the activate script here. `ln -s ../bin/activate .`
8. install pip requirements: `pip install -r requirements.txt`
9. Setup pytest: `pip install -e .`
10. Setup precommit hooks

# Problems:
## Game of Life
From (leetcode)[https://leetcode.com/problems/game-of-life/]

## Dining Philosophers
Demonstartes parallel programming and avoiding deadlock using semaphores.
from (wikipedia/dining_philosophers_problem)[https://en.wikipedia.org/wiki/Dining_philosophers_problem]

## DiagonalDifference
Simple 2d matrix addition problem from (hackerrank.com)[https://www.hackerrank.com/challenges/diagonal-difference/problem]
