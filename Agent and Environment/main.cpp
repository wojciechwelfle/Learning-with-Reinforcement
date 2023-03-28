#include "Environment.h"
#include "Agent.h"
#include <thread>
#include <iostream>

using namespace std;

void LearnAgent(Agent *agent, Environment *env, int repeat);

int main() {
    auto *pEnvironment = new Environment;
    auto *pAgent = new Agent;
    int repeat = 10;

    LearnAgent(pAgent, pEnvironment, repeat);
    pAgent->DisplayStates();
    return 0;
}

void LearnAgent(Agent *agent, Environment *env, int repeat) {
    if (agent == nullptr || env == nullptr || repeat < 1) return;
    for (int i = 0; i < repeat; ++i) {
        std::cout << "\n#####START####\n" << std::endl;
        env->SetToInitialPosition();
        env->DisplayMap();
        while (!env->isEndPosition()) {
            int position = env->GetPosition();
            int action = agent->GetAction(position);
            int newPosition = env->Step(action);
            int reward = env->GetReward();
            agent->Update(position, action, reward, newPosition, env->isEndPosition());
            env->DisplayMap();
            std::this_thread::sleep_for(std::chrono::milliseconds(3));
        }
        std::cout << "\n######END#####" << std::endl;
        std::cout << "--------------";
    }
    std::cout << std::endl;
}