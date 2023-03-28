#include "Environment.h"
#include <iostream>

Environment::Environment() {
    for (auto &in: map)
        in = 0;
    map[acceptingState] = 1;
    position = 0;
}

int Environment::Step(int action) {
    if (action == LEFT && position != lowestPosition) {
        position--;
    }
    if (action == RIGHT && position != highestPosition - 1) {
        position++;
    }
    return position;
}

std::vector<direction> Environment::GetPossibleActions(int state) {
    std::vector<direction> vector;
    if(state == lowestPosition) {
        vector.push_back(RIGHT);
    } else if(state == highestPosition - 1) {
        vector.push_back(LEFT);
    } else {
        vector.push_back(LEFT);
        vector.push_back(RIGHT);
    }
    return vector;
}

std::vector<direction> Environment::GetPossibleActions() {
    std::vector<direction> vector = {LEFT, RIGHT};
    return vector;
}

void Environment::DisplayMap() {
    for (int pos = 0; pos < sizeof(map) / sizeof(map[0]); ++pos) {
        if(pos == position) std::cout << 'P';
        else if(pos == acceptingState) std::cout << 'E';
        else std::cout << '_';
    }
    std::cout << std::endl;
}