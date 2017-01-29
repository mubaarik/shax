
import Tkinter as tk

class TkPract:
    def __init__(self, master):
        self.frame = tk.Frame(master)
        self.frame.pack(fill=tk.Y)
        self.canvas = tk.Canvas(master)
        self.canvas.pack(fill=tk.X)
        self.names = ["00", "03", "06",
              "11", "13", "15",
              "22", "23", "24",
              "30", "31", "32",
              "34", "35", "36",
              "42", "43", "44",
              "51", "53", "55",
              "60", "63", "66"]
        self.x= [50, 250, 450,
            100, 250, 400,
            150, 250, 350,
            50, 100, 150,
            350, 400, 450,
            150, 250, 350,
            100, 250, 400,
            50, 250, 450]
        
        self.y = [50, 50, 50,
             100, 100, 100,
             150, 150, 150,
             250, 250, 250,
             250, 250, 250,
             350, 350, 350,
             400, 400, 400,
             450,450,450]
        self.shax_create()
    def shax_create(self):
        for i in range(len(self.names)):
            b = tk.Button(text = self.names[i], command = self.frame.quit)
            if i>0:
                self.canvas.create_rectangle(self.x[i-1], self.y[i-1], self.x[i], self.y[i], fill="blue")
            b.place(x = self.x[i], y = self.y[i])
    def add_rect(self):
        pass
def main():
    root = tk.Tk()
    TkPract(root)
    root.mainloop()

if __name__ == '__main__':
    main() 
