#include "Agent.h"
#include <iostream>

int Agent::GetBestAction(int position) {
    float left = qTable[position][LEFT];
    float right = qTable[position][RIGHT];

    if (right == left) return rand() % 2;
    if (right > left) return RIGHT;
    return LEFT;
}

int Agent::GetAction(int position) {
    float random = (float) rand() / ((float) RAND_MAX);
    if (random <= epsilon) return rand() % 2;
    return GetBestAction(position);
}

void Agent::DisplayStates() {
    printf("State |  Left  | Right\n");
    for (int state = 0; state < 6; ++state) {
        printf("%3d   | %.4f | %.4f\n", state, qTable[state][LEFT], qTable[state][RIGHT]);
    }
}

void Agent::Update(int position, int action, int reward, int newPosition, int isDone) {
    if (isDone) {
        qTable[position][action] += alpha * ((float) reward - qTable[position][action]);
    } else {
        qTable[position][action] += alpha * ((float) reward + gamma * qTable[newPosition][GetBestAction(newPosition)] -
                                             qTable[position][action]);
    }
}