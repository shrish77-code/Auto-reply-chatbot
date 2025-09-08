import pyautogui
import time
import pyperclip
from openai import OpenAI
# Small delay before starting (so you can switch windows if needed)
time.sleep(2)

client = OpenAI(
  api_key="YOUR API KEY HERE"
)
def is_last_message_from_sender(chat_text, name="ENTER THE NAME OF THE PERSON HERE"):
    """
    Check if the last message in the chat text is from Cutuuuu.
    
    text: str -> full copied WhatsApp chat text
    name: str -> the name to check
    """
    # Split by lines
    lines = [line.strip() for line in chat_text.strip().splitlines() if line.strip()]
    
    if not lines:
        return False
    
    # Last line of the chat
    last_line = lines[-1]
    
    # WhatsApp format: [time, date] Sender: Message
    if "]" in last_line and ":" in last_line:
        try:
            sender = last_line.split("]")[1].split(":")[0].strip()
            return sender == name
        except IndexError:
            return False
    return False





 

# Step 1: Click on the icon at (1346, 1043)
pyautogui.click(1346, 1043)
# wait for window/app to open
time.sleep(2)     
 
while True:
   
    # Step 2: Drag from (672,191) to (1858,916) to select text
    pyautogui.moveTo(672, 191)
    pyautogui.mouseDown()
    pyautogui.moveTo(1858, 916, duration=1)  # drag with smooth movement
    pyautogui.mouseUp()
    time.sleep(0.5)

    # Step 3: Copy selection (CTRL + C)
    pyautogui.hotkey("ctrl", "c")
    pyautogui.click(1381,878)
    time.sleep(0.5)

    # Step 4: Get clipboard content into variable
    chatHistory = pyperclip.paste()

    # Print to confirm
    print("Copied text:\n", chatHistory)
    print(is_last_message_from_sender(chatHistory)) 
    if is_last_message_from_sender(chatHistory):
        completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a person name shrish , he speaks hindi aswell as english. he is from india. he is also a coder . You analyze chat history and respond like shrish , output should be next chat respose as shrish" },
            {"role": "user", "content": chatHistory}
        ]
        )

        response = completion.choices[0].message.content
        pyperclip.copy(response)



        # Step 5: Click at (1169, 968)
        pyautogui.click(1169, 968)
        time.sleep(0.5)

        # Step 6: Paste the copied text
        pyautogui.hotkey("ctrl", "v")
        time.sleep(0.5)

        # Step 7: Press Enter
        pyautogui.press("enter")
        time.sleep(0.5)