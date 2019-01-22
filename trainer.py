"""Module for training network using sets."""

import training_input
import training_scores

from network import network
from network import utility
import network_manager

INPUT = training_input.training_input
OUTPUT = training_scores.training_scores


TRAIN_SET_IN = []
TRAIN_SET_OUT = []

TEST_SET_IN = []
TEST_SET_OUT = []

PROPORTION = 0.822
COUNTER = 0.0

for i, inputs in enumerate(INPUT):
    COUNTER += PROPORTION
    if COUNTER >= 1.0:
        COUNTER -= 1.0
        TRAIN_SET_IN.append(inputs)
        TRAIN_SET_OUT.append(OUTPUT[i])
    else:
        TEST_SET_IN.append(inputs)
        TEST_SET_OUT.append(OUTPUT[i])

print(len(TRAIN_SET_IN))
print(len(TRAIN_SET_OUT))
print(len(TEST_SET_IN))
print(len(TEST_SET_OUT))


#FILE_NAME = input("Type name of file with network:\n")
#NETWORK = network_manager.load_network(FILE_NAME)

NETWORK = network_manager.create_random_network(-0.1, 0.5)

utility.full_learning(NETWORK, TRAIN_SET_IN, TRAIN_SET_OUT, 0.018, 30)

FILE_NAME = input("Type name of file with network:\n")

utility.save_to_file(NETWORK, FILE_NAME)
#utility.load_from_file(NETWORK, FILE_NAME)

ACCEPTABLE_COST = 0.0003
TESTS_TO_PASS = len(TEST_SET_OUT)
TESTS_PASSED = 0
TESTS_ALMOST_PASSED = 0 # Cost is acceptable, but result is reverse :()
TESTS_COST_P = 0
TESTS_COST_F = 0
COST = 0.0

for i, _ in enumerate(TEST_SET_IN):
    GOT_OUTPUT = NETWORK.get_calculation(TEST_SET_IN[i])
    # After calculation we can get the cost.
    WANTED_OUTPUT = TEST_SET_OUT[i]
    COST = NETWORK.calculate_cost(WANTED_OUTPUT)
    if COST <= ACCEPTABLE_COST:
        if(
                (
                    (
                        GOT_OUTPUT[0] >= GOT_OUTPUT[1]
                        and WANTED_OUTPUT[0] >= WANTED_OUTPUT[1]
                    )
                    or
                    (
                        GOT_OUTPUT[0] < GOT_OUTPUT[1]
                        and WANTED_OUTPUT[0] < WANTED_OUTPUT[1]
                    )
                )
            ):
            TESTS_PASSED += 1
        else:
            TESTS_ALMOST_PASSED += 1
    else:
        if(
                (
                    (
                        GOT_OUTPUT[0] >= GOT_OUTPUT[1]
                        and WANTED_OUTPUT[0] >= WANTED_OUTPUT[1]
                    )
                    or
                    (
                        GOT_OUTPUT[0] < GOT_OUTPUT[1]
                        and WANTED_OUTPUT[0] < WANTED_OUTPUT[1]
                    )
                )
            ):
            TESTS_COST_P += 1
        else:
            TESTS_COST_F += 1

print("Test:")
print("{:3d}, {:3d} / {:3d}, {:3d} / {:3d} / {:.5f} /{:.5f}".format(\
        TESTS_PASSED,\
        TESTS_ALMOST_PASSED,\
        TESTS_COST_P, \
        TESTS_COST_F,
        TESTS_TO_PASS, \
        TESTS_PASSED / TESTS_TO_PASS,\
        (TESTS_PASSED + TESTS_COST_P) / TESTS_TO_PASS))

print("Now, test on learnig set.")

TESTS_TO_PASS = len(TRAIN_SET_OUT)
TESTS_PASSED = 0
TESTS_ALMOST_PASSED = 0 # Cost is acceptable, but result is reverse :()
TESTS_COST_P = 0
TESTS_COST_F = 0
COST = 0.0

for i, _ in enumerate(TRAIN_SET_IN):
    GOT_OUTPUT = NETWORK.get_calculation(TRAIN_SET_IN[i])
    # After calculation we can get the cost.
    WANTED_OUTPUT = TRAIN_SET_OUT[i]
    COST = NETWORK.calculate_cost(WANTED_OUTPUT)
    if COST <= ACCEPTABLE_COST:
        if(
                (
                    (
                        GOT_OUTPUT[0] >= GOT_OUTPUT[1]
                        and WANTED_OUTPUT[0] >= WANTED_OUTPUT[1]
                    )
                    or
                    (
                        GOT_OUTPUT[0] < GOT_OUTPUT[1]
                        and WANTED_OUTPUT[0] < WANTED_OUTPUT[1]
                    )
                )
            ):
            TESTS_PASSED += 1
        else:
            TESTS_ALMOST_PASSED += 1
    else:
        if(
                (
                    (
                        GOT_OUTPUT[0] >= GOT_OUTPUT[1]
                        and WANTED_OUTPUT[0] >= WANTED_OUTPUT[1]
                    )
                    or
                    (
                        GOT_OUTPUT[0] < GOT_OUTPUT[1]
                        and WANTED_OUTPUT[0] < WANTED_OUTPUT[1]
                    )
                )
            ):
            TESTS_COST_P += 1
        else:
            TESTS_COST_F += 1


print("Test on learning set:")
print("{:3d}, {:3d} / {:3d}, {:3d} / {:3d} / {:.5f} /{:.5f}".format(\
        TESTS_PASSED,\
        TESTS_ALMOST_PASSED,\
        TESTS_COST_P, \
        TESTS_COST_F,
        TESTS_TO_PASS, \
        TESTS_PASSED / TESTS_TO_PASS,\
        (TESTS_PASSED + TESTS_COST_P) / TESTS_TO_PASS))
