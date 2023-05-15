
# KuadroSim
[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/)

KuadroSim is an optimized and practical quantum circuit simulator. This simulator has most 
of the quantum gates found in other simulators. So, special quantum gate addition and TFC module addition functions are available in this simulator. Perform circuit design faster and more practical with KuadroSim.

## Installation
In order to install KuadroSim, download src/KuadroSim.py from this repo and and copy it to the folder where your code is. KuadroSim requires the numpy library, to install numpy, enter the following command in the command line.

```bash 
pip install numpy
```
or
```bash 
python -m pip install numpy
```

##  How To Use It
Get started by importing KuadroSim module into your code as follows:
```bash 
import KuadroSim
``` 
After then in order to create a quantum circuit, a KuadroSim is initialized by creating an object.

```bash 
sim = KuadroSim(number_of_qubits)
``` 
or
```bash 
sim = KuadroSim(TFC_file_path)
``` 

#### \_\_init\_\_(n_qubits = 0, file = None)
| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `n_qubits` | `int` | **Either/or required**. the number of qubits.|
| `file` | `str` | **Either/or required**. the TFC file path.|



After then circuit can be designed using the following methods:

#### input(inp)
sets the input of the qubits in the circuit.
| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `inp` | `int` | **Required**. the decimal value of binary input.|

#### hadamard(wire)
applies the hadamard gate to the qubit.
| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `wire` | `int` | **Required**. the idx of qubit that be applied gate.|

#### pauliX(wire)
applies the pauliX (NOT) gate to the qubit.
| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `wire` | `int` | **Required**. the idx of qubit that be applied gate.|

#### pauliY(wire)
applies the pauliY gate to the qubit.
| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `wire` | `int` | **Required**. the idx of qubit that be applied gate.|

#### pauliZ(wire)
applies the pauliZ gate to the qubit.
| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `wire` | `int` | **Required**. the idx of qubit that be applied gate.|

#### S(wire)
applies the S-gate to the qubit.
| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `wire` | `int` | **Required**. the idx of qubit that be applied gate.|

#### Sdag(wire)
applies the Sdag-gate to the qubit.
| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `wire` | `int` | **Required**. the idx of qubit that be applied gate.|

#### T(wire)
applies the T-gate to the qubit.
| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `wire` | `int` | **Required**. the idx of qubit that be applied gate.|

#### Tdag(wire)
applies the Tdag-gate to the qubit.
| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `wire` | `int` | **Required**. the idx of qubit that be applied gate.|

#### RX(wire, angle)
applies the RX-gate to the qubit.
| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `wire` | `int` | **Required**. the idx of qubit that be applied gate.|
| `angle` | `float` | **Required**. the rotation angle (radian)|

#### RY(wire, angle)
applies the RY-gate to the qubit.
| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `wire` | `int` | **Required**. the idx of qubit that be applied gate.|
| `angle` | `float` | **Required**. the rotation angle (radian)|

#### RZ(wire, angle)
applies the RZ-gate to the qubit.
| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `wire` | `int` | **Required**. the idx of qubit that be applied gate.|
| `angle` | `float` | **Required**. the rotation angle (radian)|

#### X90(wire)
applies the RX-gate with 90 degree to the qubit.
| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `wire` | `int` | **Required**. the idx of qubit that be applied gate.|

#### mX90(wire)
applies the RX-gate with -90 degree to the qubit.
| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `wire` | `int` | **Required**. the idx of qubit that be applied gate.|

#### Y90(wire)
applies the RY-gate with 90 degree to the qubit.
| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `wire` | `int` | **Required**. the idx of qubit that be applied gate.|

#### mY90(wire)
applies the RY-gate with -90 degree to the qubit.
| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `wire` | `int` | **Required**. the idx of qubit that be applied gate.|

#### CZ(wire)
applies the CZ-gate to the qubit.
| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `wire` | `int` | **Required**. the idx of qubit that be applied gate.|

#### cnot(wire)
applies the CNOT (Controlled NOT) gate to the qubit.
| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `wire` | `int` | **Required**. the idx of qubit that be applied gate.|

#### swap(wire)
applies the Swap gate to the qubit.
| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `wire` | `int` | **Required**. the idx of qubit that be applied gate.|

#### CR(wire, angle)
applies the CR-gate to the qubit.
| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `wire` | `int` | **Required**. the idx of qubit that be applied gate.|
| `angle` | `float` | **Required**. the rotation angle (radian)|

#### CRk(wire, k)
applies the CR-gate with k parameter to the qubit.
| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `wire` | `int` | **Required**. the idx of qubit that be applied gate.|
| `k` | `int` | **Required**. the exponent|

#### toffoli(wire)
applies the Toffoli (CCNOT) gate to the qubit.
| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `wire` | `int` | **Required**. the idx of qubit that be applied gate.|

#### mct(target, controls)
applies the MCT (Multi-Controlled Toffoli) gate to the qubits.
| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `target` | `int` | **Required**. the idx of target qubit that be applied gate.|
| `controls` | `[int]` | **Required**. the idx of control qubits that be applied gate.|

#### custom(op, wire)
applies the custom gate to the qubits.
| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `op` | `[]` | **Required**. the operator matrix of the gate.|
| `wire` | `int` | **Required**. the idx of qubit that be applied gate.|

#### module(file, wire)
applies the custom gate to the qubits.
| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `file` | `str` | **Required**. the TFC file path.|
| `wire` | `int` | **Required**. the idx of qubit that be applied gate.|

#### measure_q(wire)
returns the probability of the qubit being one.
| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `wire` | `int` | **Required**. the idx of the qubit that to be measured.|

#### @property measure()
returns the measures of the qubits in circuit.

#### @property truthTable()
returns the truth table of the circuit.

#### show_truthTable()
prints the truth table of the circuit.


  
## Example Usage

The implementation of the half adder circuit given in the image below in KuadroSim is given.

![Half adder](https://i.stack.imgur.com/p1TU8.png)

```bash 
#importing KuadroSim library
from KuadroSim import KuadroSim
# building 3-qubits circuit
sim = KuadroSim(3)
# qubits are |011>
sim.input(3)
print(sim.state)
sim.mct(2, [0, 1])
sim.cnot(0)
#the circuit performs 1+1
#the last qubit is carry qubit
result = sim.measure
print(result)
``` 


## Authors and Acknowledgment

- [Niyazi Furkan Bar](https://abs.firat.edu.tr/en/nfbar)
- [Mehmet Karakose](https://abs.firat.edu.tr/en/mkarakose)


This study was supported by the TUBITAK (The Scientific and Technological Research Council of Turkey) under Grant No: 121E439.

The project title is "[A Deep Learning Based Method for Automatic Generation of Optimum Quantum Computing Models](http://1001projesi_kuadro.firat.edu.tr/)"


  
## Katkı

Katkılara her zaman açığız!

Başlamak `Contributor.md'ye bakın.

Lütfen bu projenin `davranış kurallarına` uyun.

  