#include "unif01.h"
#include "bbattery.h"
#include <stdio.h>
#include <stdlib.h>

static FILE *fp = NULL;

// This function will be used by TestU01 to get values in (0,1)
double file_rng() {
    static double val;

    if (fscanf(fp, "%lf", &val) != 1) {
        fprintf(stderr, "End of file or invalid value\n");
        exit(EXIT_FAILURE);
    }

    // Optional: sanity check
    if (val <= 0.0 || val >= 1.0) {
        fprintf(stderr, "Invalid value: %f (must be in (0,1))\n", val);
        exit(EXIT_FAILURE);
    }

    return val;
}

int main(int argc, char *argv[]) {
    // Run a test battery
    bbattery_SmallCrushFile(argv[1]);

    return 0;
}
