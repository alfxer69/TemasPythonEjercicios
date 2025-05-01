import pennylane as qml
import torch
from torch import optim

# Definir un circuito cuántico
@qml.qnode(qml.device("default.qubit", wires=2))
def circuit(params):
    qml.RX(params[0], wires=0)
    qml.CNOT(wires=[0, 1])
    return qml.expval(qml.PauliZ(1))

# Optimizar con PyTorch
params = torch.tensor([0.1], requires_grad=True)
optimizer = optim.SGD([params], lr=0.1)

for _ in range(100):
    loss = circuit(params)
    loss.backward()
    optimizer.step()
