import pennylane as qml
import matplotlib.pyplot as plt 

# we indicate the name of the registers and their number of qubits.
wires = qml.registers({"x": 4, "y":4, "output":6,"work_wires": 4})

def product_basis_state(x=0,y=0):
    qml.BasisState(x, wires=wires["x"])
    qml.BasisState(y, wires=wires["y"])

dev = qml.device("default.qubit", shots=1)
@qml.qnode(dev)
def circuit(x,y):
    product_basis_state(x, y)
    return [qml.sample(wires=wires[name]) for name in ["x", "y", "output"]]

def state_to_decimal(binary_array):
    # Convert a binary array to a decimal number
    return sum(bit * (2 ** idx) for idx, bit in enumerate(reversed(binary_array)))

output = circuit(x=1,y=4)
print("x register: ", output[0]," (binary) ---> ", state_to_decimal(output[0]), " (decimal)")
print("y register: ", output[1]," (binary) ---> ", state_to_decimal(output[1]), " (decimal)")
print("output register: ", output[2]," (binary) ---> ", state_to_decimal(output[2]), " (decimal)")


@qml.qnode(dev)
def circuit(x):

    product_basis_state(x)          # |x>
    qml.Adder(5, wires["x"])        # |x+5>

    return qml.sample(wires=wires["x"])

print(circuit(x=1), " (binary) ---> ", state_to_decimal(circuit(x=1))," (decimal)")

fig, _ = qml.draw_mpl(circuit, decimals = 2, style = "pennylane", level='device')(x=1)
plt.show()

@qml.qnode(dev)
def circuit(x,y):

    product_basis_state(x, y)                                  #    |x> |y> |0>
    qml.OutAdder(wires["x"], wires["y"], wires["output"])      #    |x> |y> |x+y>

    return qml.sample(wires=wires["output"])

print(circuit(x=2,y=3), " (binary) ---> ", state_to_decimal(circuit(x=2,y=3)), " (decimal)")

@qml.qnode(dev)
def circuit(x):

    product_basis_state(x)                                           #    |x>
    qml.Multiplier(3, wires["x"], work_wires=wires["work_wires"])    #    |3x>

    return qml.sample(wires=wires["x"])

print(circuit(x=2), " (binary) ---> ", state_to_decimal(circuit(x=2))," (decimal)")

@qml.qnode(dev)
def circuit(x,y):

    product_basis_state(x, y)                                     #    |x> |y> |0>
    qml.OutMultiplier(wires["x"], wires["y"], wires["output"])    #    |x> |y> |xy>

    return qml.sample(wires=wires["output"])

print(circuit(x=4,y=2), " (binary) ---> ", state_to_decimal(circuit(x=4,y=2))," (decimal)")

#Resta

@qml.qnode(dev)
def circuit(x):

    product_basis_state(x)                     # |x>
    qml.adjoint(qml.Adder(3, wires["x"]))      # |x-3>

    return qml.sample(wires=wires["x"])

print(circuit(x=6), " (binary) ---> ", state_to_decimal(circuit(x=6)), " (decimal)")

#Polinomio f(x,y)=4+3xy+5x+3y

def adding_3xy():
    # |x> --->  |3x>
    qml.Multiplier(3, wires["x"], work_wires=wires["work_wires"])

    # |3x>|y>|0> ---> |3x>|y>|3xy>
    qml.OutMultiplier(wires["x"], wires["y"], wires["output"])

    # We return the x-register to its original value using the adjoint operation
    # |3x>|y>|3xy>  ---> |x>|y>|3xy>
    qml.adjoint(qml.Multiplier)(3, wires["x"], work_wires=wires["work_wires"])

def adding_5x_3y():

    # |x>|y> --->  |5x>|3y>
    qml.Multiplier(5, wires["x"], work_wires=wires["work_wires"])
    qml.Multiplier(3, wires["y"], work_wires=wires["work_wires"])

    # |5x>|3y>|0> --->  |5x>|3y>|5x + 3y>
    qml.OutAdder(wires["x"], wires["y"], wires["output"])

    # We return the x and y registers to their original value using the adjoint operation
    # |5x>|3y>|5x + 3y> --->  |x>|y>|5x + 3y>
    qml.adjoint(qml.Multiplier)(5, wires["x"], work_wires=wires["work_wires"])
    qml.adjoint(qml.Multiplier)(3, wires["y"], work_wires=wires["work_wires"])
    
    
@qml.qnode(dev)    
def circuit(x,y):

    product_basis_state(x, y)      #    |x> |y> |0>
    qml.Adder(4, wires["output"])  #    |x> |y> |4>
    adding_3xy()                   #    |x> |y> |4 + 3xy>
    adding_5x_3y()                 #    |x> |y> |4 + 3xy + 5x + 3y>

    return qml.sample(wires=wires["output"])

print(circuit(x=1,y=4), " (binary) ---> ", state_to_decimal(circuit(x=1,y=4)), " (decimal)")

#usando un cable menos

wires = qml.registers({"x": 4, "y": 4, "output": 5,"work_wires": 4})

print(circuit(x=1,y=4), " (binary) ---> ", state_to_decimal(circuit(x=1,y=4)), " (decimal)")

#Forma mas directa paratrabajar con polinomios
def f(x, y):
    return 4 + 3*x*y + 5*x + 3*y

wires = qml.registers({"x": 4, "y":4, "output":6})
@qml.qnode(dev)
def circuit_with_Poly(x,y):

   product_basis_state(x, y)                         #    |x> |y> |0>
   qml.OutPoly(
       f,
       input_registers= [wires["x"], wires["y"]],
       output_wires = wires["output"])               #    |x> |y> |4 + 3xy + 5x + 3y>

   return qml.sample(wires = wires["output"])

print(circuit_with_Poly(x=1,y=4), " (binary) ---> ", state_to_decimal(circuit_with_Poly(x=1,y=4)), " (decimal)")



