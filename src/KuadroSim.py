import numpy as np
import math
import cmath


class KuadroSim(object):

    def __init__(self, n_qubits: int = 0, file: str = None) -> None:
        """

        :param file: the TFC file path
        :param n_qubits: the number of qubits of the circuit
        """
        if file is not None:
            self._operator = self.__tfc2op(file)
            self._n = int(math.sqrt(len(self._operator)))
        else:
            assert n_qubits > 0, "the number of qubits is not less than 1"
            self._n = n_qubits
            self._operator = np.eye(2 ** self._n)

        self._state = np.zeros(2 ** self._n)
        self._state[0] = 1

    def input(self, inp: int) -> None:
        """

        :param inp: the decimal value of binary input eg. |q2q1q0> => |011> -> 3 = inp
        """
        assert inp < 2 ** self._n, "input is not valid"
        self._state = np.zeros(2 ** self._n)
        self._state[inp] = 1

    def __isLogic(self, op: [] = None) -> bool:
        if op is None:
            op = self._operator
        return np.array_equal(op, op.astype(bool))

    def __common(self, matrix: [], wire: int) -> None:
        """

        :param matrix: the matrix of gate
        :param wire: the idx of qubit that be applied gate
        """
        assert self.__wire_check(wire), "wire idx is not valid"
        left = np.eye(2 ** (self._n - wire - int(math.sqrt(matrix.shape[0]))))
        right = np.eye(2 ** wire)
        t_mul = np.kron(np.kron(left, matrix), right)
        self._operator = np.matmul(t_mul, self._operator)

    def hadamard(self, wire: int) -> None:
        """

        :param wire: the idx of qubit that be applied gate
        """
        matrix = 1 / math.sqrt(2) * np.array([
            [1, 1],
            [1, -1]
        ])
        self.__common(matrix, wire)

    def pauliX(self, wire: int) -> None:
        """

        :param wire: the idx of qubit that be applied gate
        """
        matrix = np.array([
            [0, 1],
            [1, 0]
        ])
        self.__common(matrix, wire)

    def pauliY(self, wire: int) -> None:
        """

        :param wire: the idx of qubit that be applied gate
        """
        matrix = np.array([
            [0, complex(0, -1)],
            [complex(0, 1), 0]
        ])
        self.__common(matrix, wire)

    def pauliZ(self, wire: int) -> None:
        """

        :param wire: the idx of qubit that be applied gate
        """

        matrix = np.array([[1, 0], [0, -1]])
        self.__common(matrix, wire)

    def S(self, wire: int) -> None:
        """

        :param wire: the idx of qubit that be applied gate
        """
        matrix = np.array([
            [1, 0],
            [0, complex(0, 1)]
        ])
        self.__common(matrix, wire)

    def SDag(self, wire: int) -> None:
        """

        :param wire: the idx of qubit that be applied gate
        """
        matrix = np.array([
            [1, 0],
            [0, (-1) * complex(0, 1)]
        ])
        self.__common(matrix, wire)

    def T(self, wire: int) -> None:
        """

        :param wire: the idx of qubit that be applied gate
        """
        matrix = np.array([
            [1, 0],
            [0, cmath.exp(complex(0, 1) * math.pi / 4)]
        ])
        self.__common(matrix, wire)

    def TDag(self, wire: int) -> None:
        """

        :param wire: the idx of qubit that be applied gate
        """
        matrix = np.array([
            [1, 0],
            [0, cmath.exp((-1) * complex(0, 1) * math.pi / 4)]
        ])
        self.__common(matrix, wire)

    def RX(self, wire: int, angle: float) -> None:
        """

        :param wire: the idx of qubit that be applied gate
        :param angle: the rotation angle (radian)
        """
        matrix = np.array([
            [math.cos(angle / 2), (-1) * complex(0, 1) * math.sin(angle / 2)],
            [(-1) * complex(0, 1) * math.sin(angle / 2), math.cos(angle / 2)]
        ])
        self.__common(matrix, wire)

    def RY(self, wire: int, angle: float) -> None:
        """

        :param wire: the idx of qubit that be applied gate
        :param angle: the rotation angle (radian)
        """
        matrix = np.array([
            [math.cos(angle / 2), (-1) * math.sin(angle / 2)],
            [math.sin(angle / 2), math.cos(angle / 2)]
        ])
        self.__common(matrix, wire)

    def RZ(self, wire: int, angle: float) -> None:
        """

        :param wire: the idx of qubit that be applied gate
        :param angle: the rotation angle (radian)
        """
        matrix = np.array([
            [cmath.exp((-1) * complex(0, 1) * angle / 2), 0],
            [0, cmath.exp(complex(0, 1) * angle / 2)]
        ])
        self.__common(matrix, wire)

    def X90(self, wire: int) -> None:
        """

        :param wire: the idx of qubit that be applied gate
        """
        self.RX(wire, math.pi / 2)

    def mX90(self, wire: int) -> None:
        """

        :param wire: the idx of qubit that be applied gate
        """
        self.RX(wire, (-1) * math.pi / 2)

    def Y90(self, wire: int) -> None:
        """

        :param wire: the idx of qubit that be applied gate
        """
        self.RY(wire, math.pi / 2)

    def mY90(self, wire: int) -> None:
        """

        :param wire: the idx of qubit that be applied gate
        """
        self.RY(wire, (-1) * math.pi / 2)

    def CZ(self, wire: int) -> None:
        """

        :param wire: the idx of qubit that be applied gate
        """
        matrix = np.array([
            [1, 0, 0, 0],
            [0, 1, 0, 0],
            [0, 0, 1, 0],
            [0, 0, 0, -1]
        ])
        self.__common(matrix, wire)

    def cnot(self, wire: int) -> None:
        """

        :param wire: the idx of qubit that be applied gate
        """
        matrix = np.array([
            [1, 0, 0, 0],
            [0, 1, 0, 0],
            [0, 0, 0, 1],
            [0, 0, 1, 0]
        ])
        self.__common(matrix, wire)

    def swap(self, wire: int) -> None:
        """

        :param wire: the idx of qubit that be applied gate
        """
        matrix = np.array([
            [1, 0, 0, 0],
            [0, 0, 1, 0],
            [0, 1, 0, 0],
            [0, 0, 0, 1]
        ])
        self.__common(matrix, wire)

    def CR(self, wire: int, angle: float) -> None:
        """

        :param wire: the idx of qubit that be applied gate
        :param angle: the rotation angle (radian)
        """
        matrix = np.array([
            [1, 0, 0, 0],
            [0, 1, 0, 0],
            [0, 0, 1, 0],
            [0, 0, 0, cmath.exp(complex(0, 1) * angle)]
        ])
        self.__common(matrix, wire)

    def CRk(self, wire: int, k: int) -> None:
        """

        :param wire: the idx of qubit that be applied gate
        :param k: exponent
        """
        self.CR(wire, math.pi / (2 ** k))

    def toffoli(self, wire: int) -> None:
        """

        :param wire: the idx of qubit that be applied gate
        """
        matrix = np.array([
            [1, 0, 0, 0, 0, 0, 0, 0],
            [0, 1, 0, 0, 0, 0, 0, 0],
            [0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 1, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0],
            [0, 0, 0, 0, 0, 1, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 1],
            [0, 0, 0, 0, 0, 0, 1, 0]
        ])
        self.__common(matrix, wire)

    def mct(self, target: int, controls: [int]) -> None:
        assert self.__wire_check(target), "target idx is not valid"
        for _ in range(len(controls)):
            assert self.__wire_check(controls[_]), "control idx is not valid"
        m = 0
        for _ in range(len(controls)):
            m += 2 ** (controls[_])
        d = lambda i: 2 ** target if (2 ** target) & i == 0 else -(2 ** target)
        matrix = np.array([([0] * 2 ** self._n)] * 2 ** self._n)
        for i in range(2 ** self._n):
            for j in range(2 ** self._n):
                matrix[i][j] = 1 if (i & m == m and j == d(i) + i) or (i & m != m and j == i) else 0
        self._operator = np.matmul(matrix, self._operator)

    def custom(self, op: [], wire: int = 0) -> None:
        """

        :param op: the operator matrix of the gate
        :param wire: the idx of qubit that be applied gate
        """
        assert (len(op) == len(op[0])) and (len(op) <= len(self._operator) and (
                    math.log2(len(self._operator)) <= self._n - wire)), "operator matrix is not valid"
        self.__common(op, wire)

    def module(self, file: str, wire: int = 0) -> None:
        """

        :param file: the TFC file path
        :param wire: the idx of qubit that be applied gate
        """
        self.custom(self.__tfc2op(file), wire)

    def __tfc2op(self, file):
        try:
            file = open(file, 'r')
            lines = []
            num_qubits = 0
            var = []
            for line in file.readlines():
                if line.startswith(".v"):
                    var = [l.strip() for l in line.replace('.v', '').replace('\n', '').split(',')]
                    num_qubits = len(var)
                elif line.startswith('t') or line.startswith('f'):
                    lines.append(line.replace('\n', ''))

            simulator = KuadroSim(num_qubits)
            for line in lines:
                if line.startswith('t'):
                    num_ct = int(line.split(' ')[0].replace('t', ''))
                    ops = [l.strip() for l in line.replace('t' + str(num_ct), '').replace('\n', '').split(',')]
                    if num_ct != len(ops):
                        print('tX not equal')
                    if num_ct == 0:
                        print('t0 error')
                        exit()
                    elif num_ct == 1:
                        simulator.pauliX(var.index(ops[0]))
                    elif num_ct == 2:
                        simulator.mct(var.index(ops[1]), [var.index(ops[0])])
                    else:
                        controls = [var.index(op) for op in ops[0:num_ct - 1]]
                        target = var.index(ops[-1])
                        simulator.mct(target, controls)

                elif line.startswith('f'):
                    print('fredkin gate is not using -now-.')
                    exit()
                else:
                    print('error')
                    exit()
            file.close()
            return simulator.operator
        except FileNotFoundError:
            print('File does not exist')
            exit()
        except Exception as e:
            print('An error occurred')
            print(e)
            exit()

    def __wire_check(self, wire):
        return wire < self._n

    @property
    def measure(self) -> [complex]:
        """
        This function is returned the measures of the qubits in circuit
        :return: the measures of the qubits
        """
        return np.matmul(self._operator, self._state)

    def measure_q(self, wire: int) -> complex:
        """

        :param wire: the idx of the qubit that to be measured
        :return: the probability of the qubit being one
        """
        assert self.__wire_check(wire), "wire idx is not valid"
        one_probability = 0.0
        measure = self.measure
        len_m = len(measure)
        for _ in range(len_m):
            if bin(_)[-1-wire] == "1":
                one_probability += round(measure[_] ** 2, 5)
        return one_probability

    @property
    def truthTable(self) -> [int]:
        assert self.__isLogic, "circuit is not logic"
        truth_table = np.zeros(2 ** self._n)
        output = []
        for i in range(2 ** self._n):
            self.input(i)
            output = self.measure
            for _ in range(len(output)):
                if output[_] == 1:
                    truth_table[i] = _
                    break
        return truth_table

    def show_truthTable(self) -> None:
        truth_table = self.truthTable
        formatStr = '{0:0' + str(self._n) + 'b}'
        for i in range(len(truth_table)):
            print(formatStr.format(i), end="   ==>   ")
            print(formatStr.format(int(truth_table[i])))

    @property
    def num_qubits(self) -> int:
        return self._n

    @property
    def state(self) -> []:
        return self._state

    @property
    def operator(self) -> []:
        return self._operator
