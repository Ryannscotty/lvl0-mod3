from tkinter import Tk, simpledialog, messagebox


if __name__ == '__main__':
    # TODO: Look at the AreYouHappy.png image

    #       Use pop-ups to recreate the chart using if and elif statements
    user_input = simpledialog.askstring(prompt="input 1", title="are you happy ?")
    if user_input == "yes":
        messagebox.showinfo(message="keep doing whatever you are doing ! ")
    if user_input == "no":

        user_input2 = simpledialog.askstring(prompt="input 2", title="do you want to be happy ? ")

        if user_input2 == "yes":

         messagebox.showinfo(message="change something ! ")
        else:
         messagebox.showinfo(message="keep doing whatever you are doing ! ")



pass
