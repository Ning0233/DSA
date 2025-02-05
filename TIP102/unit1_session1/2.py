def final_value_after_operations(operations):
  t = 1
  for op in operations:
        if op == "flouncy" or op =="bouncy":
            t += 1
        if op == "trouncy" or op == "pouncy":
            t -= 1
  return t







if __name__ == "__main__": 
    operations = ["trouncy", "flouncy", "flouncy"]
    print(final_value_after_operations(operations))

    operations = ["bouncy", "bouncy", "flouncy"]
    print(final_value_after_operations(operations))






