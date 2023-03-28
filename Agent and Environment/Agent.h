#ifndef AGENT_H
#define AGENT_H
#include "Direction.h"

class Agent {
private:
    const float alpha = 0.1f;
    const float gamma = 0.9f;
    const float epsilon = 0.9f;
    float qTable[6][2] = {0};
public:
    int GetBestAction(int position);

    int GetAction(int position);

    void DisplayStates();

    void Update(int position, int action, int reward, int newPosition, int isDone);
};

#endif
