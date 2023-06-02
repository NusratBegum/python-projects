"""
1.Write a function called f_to_c that takes an input f_temp, a temperature in Fahrenheit, and converts it to c_temp, that temperature in Celsius.

2.Let’s test your function with a value of 100 Fahrenheit.Define a variable f100_in_celsius and set it equal to the value of f_to_c with 100 as an input.

3.Write a function called c_to_f that takes an input c_temp, a temperature in Celsius, and converts it to f_temp, that temperature in Fahrenheit.

4.Let’s test your function with a value of 0 Celsius.Define a variable c0_in_fahrenheit and set it equal to the value of c_to_f with 0 as an input.

5.Define a function called get_force that takes in mass and acceleration. It should return mass multiplied by acceleration.

6.Print the string “The GE train supplies X Newtons of force.”, with X replaced by train_force

7.Define a function called get_energy that takes in mass and c.c is a constant that is usually set to the speed of light, which is roughly 3 x 10^8. Set c to have a default value of 3*10**8.

8.Test get_energy by using it on bomb_mass, with the default value of c. Save the result to a variable called bomb_energy.

9.Print the string “A 1kg bomb supplies X Joules.”, with X replaced by bomb_energy.

10.Define a final function called get_work that takes in mass, acceleration, and distance.

11.Test get_work by using it on train_mass, train_acceleration, and train_distance. Save the result to a variable called train_work.

12.Print the string "The GE train does X Joules of work over Y meters.", with X replaced with train_work and Y replaced with train_distance

"""

#Uncomment this when you reach the "Use the Force" section
train_mass = 22680
train_acceleration = 10
train_distance = 100
bomb_mass = 1


# Write your code below: 
def f_to_c (f_temp):
   return( f_temp - 32) * 5/9 
print(f_to_c(32)) 


f100_in_celsius = f_to_c (100)
print(f100_in_celsius)

def c_to_f(c_temp):
  return (c_temp * 9/5) + 32

c0_in_fahrenheit = c_to_f(0)
print(c0_in_fahrenheit)

def get_force (mass, acceleration ):
   return (mass*acceleration)

train_force = get_force (train_mass, train_acceleration )
print(train_force)

print("The GE train supplies", train_force ,"Newtons of force.")

def get_energy (mass,c = 3*10**8):
  return (mass*c**2 )

bomb_energy = get_energy (bomb_mass)

print("A 1kg bomb supplies",bomb_energy,"Joules")


def get_work (mass,acceleration,distance):
  force = get_force(mass,acceleration)
  return (force * distance)
train_work = get_work (train_mass,train_acceleration,train_distance)
  
print("The GE train does", train_work, "Joules of work over",train_distance, "meters.")

    








