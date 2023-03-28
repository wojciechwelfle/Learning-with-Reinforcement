#ifndef ENVIRONMENT_H
#define ENVIRONMENT_H

#include <vector>
#include "Agent.h"
#include "Direction.h"

class Environment {
private:
    const static int lowestPosition = 0;
    const static int highestPosition = 6;
    int map[Environment::highestPosition];
    const int startPosition = 0;
    const int acceptingState = 5;
    int position;
    int reward;
public:
    Environment();

    int Step(int action);

    static std::vector<direction> GetPossibleActions();

    static std::vector<direction> GetPossibleActions(int state);

    [[nodiscard]] int GetPosition() const {
        return position;
    }

    void SetToInitialPosition() {
        position = startPosition;
    }

    int GetReward() {
        return map[position];
    }

    [[nodiscard]] bool isEndPosition() const {
        return position == acceptingState;
    }

    void DisplayMap();
};


#endif