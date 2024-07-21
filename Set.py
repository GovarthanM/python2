num_inputs = int(input("Number of inputs: "))
unique_inputs = set()
for _ in range(num_inputs):
    user_input = input("Enter a value: ")
    unique_inputs.add(user_input)

print(f"Unique inputs: {len(unique_inputs)}")


#input: 3
#       banana
#       apple
#       banana



#output: Unique inputs: 2