from tkinter import simpledialog, messagebox, Tk
import webbrowser


# Use this function to play a video from the internet
def play_video(url):
    webbrowser.open(url)

# =================== DO NOT MODIFY THE CODE ABOVE ===========================


if __name__ == '__main__':
    # TODO 1) Make a new window variable, window = Tk()
    window = Tk()
    #      2) Hide the window using the window's .withdraw() method
    window.withdraw()
    #      3) Ask the user how many cats they have
    catNum = simpledialog.askstring(prompt="cats",title=" how many cats do you have ? ")
    #      4) If they have 3 or more cats, tell them they are a crazy cat lady
    if int(catNum) > 3:
        messagebox.showinfo(message="you are a crazy cat lady ! ")
    #      5) If they have less than 3 cats AND more than 0 cats, call the
    if int(catNum) < 3 and int(catNum)> 0 :
     play_video("https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=&cad=rja&uact=8&ved=2ahUKEwit66G0zuf4AhWaKkQIHXIVChkQwqsBegQIBBAB&url=https%3A%2F%2Fwww.youtube.com%2Fwatch%3Fv%3DuHKfrz65KSU&usg=AOvVaw1mcWi_2g_Z4JArRhgSq5wU")
    #         play_video function below to show them a cat video
    # 6) If they have 0 cats, show them a video of A Frog Sitting on a
    if int(catNum) < 0 :
      play_video("https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=&cad=rja&uact=8&ved=2ahUKEwionZDqzuf4AhVzJEQIHe-sC8MQtwJ6BAgGEAI&url=https%3A%2F%2Fwww.youtube.com%2Fwatch%3Fv%3Doj_yLBltPE8&usg=AOvVaw2lIiqBSUKiZc7xrcHk1wDf")
    #         Bench Like a Human

    pass
