# Create a function about kinetic and potential energy. 
# Formula Kinetic = 1/2 * mass * velocity ** 2
# Formula Potential = mass * gravitational acceleration * height.


def calc_kinetic_energy(m,v):
    ke = 1/2 * m * v**2
    return ke


def calc_potential_energy(m,g,h):
    pe = m * g * h 
    return pe

 
data = int(input("0/1 (0=Kinetic Energy) (1=Potential Energy: "))

if data == 0:
    
    mass = int(input("Enter mass:"))
    
    velocity = int(input("Enter velocity: "))
    
    print(calc_kinetic_energy(mass,velocity))

elif data == 1:
    
    mass = int(input("Enter mass: "))
    
    gravitational = int(input("Enter gravitational acceleration: "))
    
    height = int(input("Enter height: "))
    
    print(calc_potential_energy(mass,gravitational,height))

else:
    print("Error! Please try again!")