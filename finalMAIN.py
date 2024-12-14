from finalGUI import *
def main():
    window = Tk()
    window.title('Sigma Kappa Recruitment Database')
    window.geometry('500x500')
    window.resizable(False, True)
    Gui(window)
    window.mainloop()
    
if __name__ == "__main__":
    main()