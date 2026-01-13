from tkinter import

class Table:
    
    def __init__(self,root):
        
        for i in range(total_rows):
            for j in range(total_columns):
                
                self.e = Entry(root, width=20, fg='blue',
                               font=('Arial',16,'bold'))
                
                self.e.grid(row=i, column=j)
                self.e.insert(END, lst[i][j])

lst = [(1,'9 +','10',19),
       (2,'9 +','9',18),
       (3,'10 +','10',20),
       (4,'5 +','16',21),
       (5,'30 -','9',21)]
 
total_rows = len(lst)
total_columns = len(lst[0])
 
root = Tk()
t = Table(root)
root.mainloop()