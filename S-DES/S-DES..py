#=================================================================================================#
# Desc: S-DES binary input conversion program
# Nathan Yorio, 2022
#=================================================================================================#

from itertools import permutations
from itertools import islice

#========================================= Functions =============================================#

# Convert the chosen binary into a list of the bits
def bin_to_list(binary):
    bins = []
    for integer in binary:
        bins.append(int(integer))
    return bins 

def list_to_bin(five_bit_input):
    #five_bit_input = [0,1,1,0,0] 
    bits_int = 0 
    for binary_digit in five_bit_input:
        bits_int = 2 * bits_int + binary_digit # combine the list into an int
        print(type(bits_int))
    #print(type(bits_bin))
    return bits_int

#define custom bit shifting within fixed 5 bit set, one shift left
def custom_five_bit_shift(five_bit_input):
    shifted_bits = [0] * 5
    shifted_bits[0] = five_bit_input[1]
    shifted_bits[1] = five_bit_input[2]
    shifted_bits[2] = five_bit_input[3]
    shifted_bits[3] = five_bit_input[4]
    shifted_bits[4] = five_bit_input[0]
    return shifted_bits

#define custom bit shifting within fixed 5 bit set, two shifts left
def custom_five_bit_shift_two(five_bit_input):
    shifted_bits = [0] * 5
    shifted_bits[0] = five_bit_input[3]
    shifted_bits[1] = five_bit_input[4]
    shifted_bits[2] = five_bit_input[0]
    shifted_bits[3] = five_bit_input[1]
    shifted_bits[4] = five_bit_input[2]
    return shifted_bits

#P10 Permutation is: P10(k1, k2, k3, k4, k5, k6, k7, k8, k9, k10) = (k3, k5, k2, k7, k4, k10, k1, k9, k8, k6)
def perm_ten(input_list):
    new_list = [0] * 10
    print("Input P10 list is:",input_list)
    new_list[0] = input_list[2]
    new_list[1] = input_list[4]
    new_list[2] = input_list[1]
    new_list[3] = input_list[6]
    new_list[4] = input_list[3]
    new_list[5] = input_list[9]
    new_list[6] = input_list[0]
    new_list[7] = input_list[8]
    new_list[8] = input_list[7]
    new_list[9] = input_list[5]
    print("P10 Permutated list is:",new_list)
    return new_list

#P8 permutation is: P8(k1, k2, k3, k4, k5, k6, k7, k8, k9, k10) = (k6, k3, k7, k4, k8, k5, k10, k9)
def perm_eight(input_list):
    new_list = [0] * 8
    print("Input P8 list is:",input_list)
    new_list[0] = input_list[5]
    new_list[1] = input_list[2]
    new_list[2] = input_list[6]
    new_list[3] = input_list[3]
    new_list[4] = input_list[7]
    new_list[5] = input_list[4]
    new_list[6] = input_list[9]
    new_list[7] = input_list[8]
    print("P8 Permutated list is:",new_list)
    return new_list


#=================================================================================================#
#===============================================MAIN==============================================#

#===============================================KEY1==============================================#

chosen_binary = input("Please choose a 10 bit binary value\n")

# Needs to be formatted from input string into binary   
chosen_bin_binary = str.format(chosen_binary,'b')
print("Chosen 10 bit binary value is:",chosen_bin_binary)

# Convert the binary number into a list bit by bit
chosen_bin_list = bin_to_list(chosen_bin_binary)
print("Chosen Binary as a list looks like:    ",chosen_bin_list)

# Convert the input binary value into the 10th permutation
tenth_perm = perm_ten(chosen_bin_list)
print("the tenth permutation of that list is:",tenth_perm)

# use islice from itertools to cut the binary list into 2 halves
# islice(iterable, start, stop, step)
key_one_left  = list(islice(tenth_perm, 0, 5, 1))
key_one_right = list(islice(tenth_perm, 5, 10, 1))
print("left half of p10 key is: ", key_one_left)
print("right half of p10 key is: ", key_one_right)

#shift each key half left 1 bit, but restricted to a 5 bit sequence
key_one_bin_left_shifted_left       = custom_five_bit_shift(key_one_left)
key_one_bin_left_shifted_right      = custom_five_bit_shift(key_one_right)
print("left bin key shifted left by one within 5 bits is: ",key_one_bin_left_shifted_left)
print("right bin key shifted left by one within 5 bits is: ",key_one_bin_left_shifted_right)


#combine the new shifted lists back together into one list
first_permutation = key_one_bin_left_shifted_left + key_one_bin_left_shifted_right
print("the first permutation after P10 is: ", first_permutation)

#get the first final key from the P8 permutation
key_one_final = perm_eight(first_permutation)
print("First key is: ", key_one_final)

#=================================================================================================#
#===============================================KEY2==============================================#
#shift each key half left 2 bit, but restricted to the same 5 bit sequence
key_two_bin_left_shifted_left       = custom_five_bit_shift_two(key_one_left)
key_two_bin_left_shifted_right      = custom_five_bit_shift_two(key_one_right)
print("second left bin key shifted left by two within 5 bits is: ",key_two_bin_left_shifted_left)
print("second right bin key shifted left by two within 5 bits is: ",key_two_bin_left_shifted_right)

second_permutation = key_two_bin_left_shifted_left + key_two_bin_left_shifted_right
print("the second permutation after P10 is: ", second_permutation)

#get the second final key from the P8 permutation
key_two_final = perm_eight(second_permutation)
print("Second key is: ", key_two_final,"\n\n\n\n")

print("First key is: ", key_one_final)
print("Second key is: ", key_two_final,"\n\n\n\n")
#=================================================================================================#
