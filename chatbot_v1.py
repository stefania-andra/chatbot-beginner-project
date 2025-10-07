
def chatbot():
    print("Hello! I am your chatbot. Type 'quit' to exit.")
    while True:
      user_input=input("You: ").lower()
      if user_input == "quit" :
         print("Chatbot: Goodbye!")
         break
      elif "hi" in user_input or "hello" in user_input:
         print("Chatbot: Hello there!")
      elif "how are you" in user_input:
          print("Chatbot: I'm just a program, but I'm doing fine!")
      elif "name" in user_input:
          print("Chatbot: I don't have a name, but you can call me Chatbot 1.0")
      else:
          print("Chatbot: Sorry I don't understand.")
chatbot()

