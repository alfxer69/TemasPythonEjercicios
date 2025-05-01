import pennylane as qml
from pennylane import numpy as np

# 1. Definir dispositivo
dev = qml.device("default.qubit", wires=2)

# 2. Circuito cuántico
@qml.qnode(dev)
def qnn(params, x):
    qml.RY(x, wires=0)
    qml.RY(params[0], wires=0)
    qml.CNOT(wires=[0, 1])
    return qml.expval(qml.PauliZ(1))

# 3. Función de pérdida (clásica)
def loss(params, x, y_true):
    y_pred = qnn(params, x)
    return (y_pred - y_true) ** 2

# 4. Datos y optimización
params = np.array([0.1], requires_grad=True)
x, y_true = 1.2, -0.5

opt = qml.GradientDescentOptimizer()
for _ in range(100):
    params = opt.step(lambda p: loss(p, x, y_true), params)
