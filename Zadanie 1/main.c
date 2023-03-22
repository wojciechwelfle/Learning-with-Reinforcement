#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#define END 5
#define RIGHT 1
#define LEFT 0

int GetBestAction(int position, float array[6][2]) {
    float right = array[position][RIGHT];
    float left = array[position][LEFT];

    if (right == left) return rand() % 2;
    if (right > left) return RIGHT;
    return LEFT;
}

int GetAction(float epsilon, int position, float array[6][2]) {
    float random = (float) rand() / ((float) RAND_MAX);
    if (random <= epsilon) return rand() % 2;
    return GetBestAction(position, array);
}

int Step(int position, int action) {
    if (action == RIGHT) return position + 1;
    else if (position == 0) return position;
    else return position - 1;
}

void DisplayArray(float array[6][2]) {
    printf("State|Left|Right\n");
    for (int state = 0; state < 6; ++state) {
        printf("%3d  |%.3f|%.3f\n", state, array[state][LEFT], array[state][RIGHT]);
    }
}

int main() {
    srand(time(NULL));
    int position;
    int reward;
    float array[6][2] = {0};
    float alpha = 0.1f;
    float gamma = 0.9f;
    float epsilon = 0.9f;

    for (int i = 0; i < 50; ++i) {
        position = 0;
        while (position != END) {
            int action = GetAction(epsilon, position, array);
            int newPosition = Step(position, action);

            if (newPosition == END) reward = 1;
            else reward = 0;

            array[position][action] +=
                    alpha * ((float) reward + gamma * array[newPosition][GetBestAction(newPosition, array)] -
                             array[position][action]);
            position = newPosition;
        }
    }

    DisplayArray(array);
    return 0;
}
