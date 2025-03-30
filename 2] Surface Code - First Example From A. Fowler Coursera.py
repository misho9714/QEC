import stim
print(stim.__version__)

circuit = stim.Circuit("""

R 0 1 2 3 4

X_ERROR(0.001) 0 1 2 3 4
CX 0 1 2 3
DEPOLARIZE2(0.001) 0 1 2 3
DEPOLARIZE1(0.001) 4
CX 2 1 4 3
DEPOLARIZE1(0.001) 0
DEPOLARIZE2(0.001) 2 1 4 3
X_ERROR(0.001) 1 3
M 1 3
DEPOLARIZE1(0.001) 0 2 4
DETECTOR(1, 0) rec[-2]
DETECTOR(3, 0) rec[-1]

REPEAT 5 {
    R 1 3
    X_ERROR(0.001) 1 3
    DEPOLARIZE1(0.001) 0 2 4
    CX 0 1 2 3
    DEPOLARIZE2(0.001) 0 1 2 3
    DEPOLARIZE1(0.001) 4
    CX 2 1 4 3
    DEPOLARIZE1(0.001) 0
    DEPOLARIZE2(0.001) 2 1 4 3
    X_ERROR(0.001) 1 3
    M 1 3
    DEPOLARIZE1(0.001) 0 2 4
    SHIFT_COORDS(0, 1)
    DETECTOR(1, 0) rec[-2] rec[-4]
    DETECTOR(3, 0) rec[-1] rec[-3]
}

X_ERROR(0.001) 0 2 4
M 0 2 4
SHIFT_COORDS(0, 1)
DETECTOR(1, 0) rec[-2] rec[-3] rec[-5]
DETECTOR(3, 0) rec[-1] rec[-2] rec[-4]
OBSERVABLE_INCLUDE(0) rec[-1]

""")
