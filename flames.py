from tkinter import *


def remove_match_char(list1, list2):
    i = 0
    while i < len(list1):
        for j in range(len(list2)):
            if list1[i] == list2[j]:
                c = list1[i]
                list1.remove(c)
                list2.remove(c)
                list3 = list1 + ["*"] + list2
                return [list3, True]
        i += 1
    list3 = list1 + ["*"] + list2
    return [list3, False]

def tell_status():
    p1 = Player1_field.get().lower().replace(" ", "")
    p2 = Player2_field.get().lower().replace(" ", "")
    
    p1_list = list(p1)
    p2_list = list(p2)
    
    proceed = True
    while proceed:
        ret_list = remove_match_char(p1_list, p2_list)
        con_list = ret_list[0]
        proceed = ret_list[1]
        
        star_index = con_list.index("*")
        p1_list = con_list[:star_index]
        p2_list = con_list[star_index + 1:]

    count = len(p1_list) + len(p2_list)
    result = ["Friends", "Love", "Affection", "Marriage", "Enemy", "Siblings"]

    while len(result) > 1:
        split_index = (count % len(result)) - 1
        if split_index >= 0:
            right = result[split_index + 1:]
            left = result[:split_index]
            result = right + left
        else:
            result = result[:len(result) - 1]

    Status_field.delete(0, END)
    Status_field.insert(10, result[0])


def clear_all():
    Player1_field.delete(0, END)
    Player2_field.delete(0, END)
    Status_field.delete(0, END)
    Player1_field.focus_set()


if __name__ == "__main__":
    root = Tk()
    root.configure(background="#ECA427")
    root.geometry("500x250")
    root.title("Flames Game")

   
    label1 = Label(root, text="Your Name:", fg='black', bg="gold", font=('Arial', 12, 'bold'))
    label2 = Label(root, text="Your crush's  Name:", fg='black', bg="gold", font=('Arial', 12, 'bold'))
    label3 = Label(root, text="Relationship Status:", fg='black', bg="gold", font=('Arial', 12, 'bold'))

    label1.grid(row=0, column=0, padx=10, pady=10, sticky="W")
    label2.grid(row=1, column=0, padx=10, pady=10, sticky="W")
    label3.grid(row=2, column=0, padx=10, pady=10, sticky="W")


    Player1_field = Entry(root, width=35)
    Player2_field = Entry(root, width=35)
    Status_field = Entry(root, width=35)

    Player1_field.grid(row=0, column=1, padx=10, pady=10)
    Player2_field.grid(row=1, column=1, padx=10, pady=10)
    Status_field.grid(row=2, column=1, padx=10, pady=10)

   
    button1 = Button(root, text="Submit", bg="red", fg="white", font=('Arial', 12, 'bold'), command=tell_status)
    button2 = Button(root, text="Clear", bg="red", fg="white", font=('Arial', 12, 'bold'), command=clear_all)

    button1.grid(row=3, column=0, padx=10, pady=20)
    button2.grid(row=3, column=1, padx=10, pady=20)

    root.mainloop()
