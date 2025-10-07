
def chatbot():
    print("Hello! I am a simple chatbot. Ask me a questiion or type 'quit' to exit.")
    while True:
      user_input=input("You: ").lower()
      if user_input == "quit" :
         print("Chatbot: Have a nice day!")
         break
      elif "hi" in user_input or "hello" in user_input:
         print("Chatbot: Hello there!")
      elif "how are you" in user_input:
          print("Chatbot: I'm just a program, but I'm doing fine! How are you doing?")
      elif "fine" in user_input or "good" in user_input:
          print("I'm glad to hear that!")
      elif "name" in user_input:
          print("Chatbot: I don't have a name, but you can call me Chatbot 1.0")
      elif "bye" in user_input:
          print("Chatbot: Goodbye!") 
      elif "who made you" in user_input:
          print("Chatbot: My creator is Andra Stefania Paraianu.")
      elif "joke" in user_input:
         print("Chatbot: What do you call a chatbot that only speaks in Python? A syntax therapist!")   
      else:
          print("Chatbot: Sorry I don't understand.")
chatbot()


