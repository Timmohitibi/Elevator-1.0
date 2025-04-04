import tkinter as tk
from tkinter import messagebox, simpledialog
import random

class ElevatorSimulator:
    def __init__(self):
        """Initialize the ElevatorSimulator."""
        # Set the initial floor to "A"
        self.current_floor = "A"
        # Define valid floors
        self.valid_floors = {"A", "B", "C"}

        # Create the main Tkinter window
        self.root = tk.Tk()
        self.root.title("Elevator Simulator")

        # Label to display the current floor
        self.floor_label = tk.Label(self.root, text="Elevator is now at Floor " + self.current_floor)
        self.floor_label.pack(pady=20)

        # Frame to hold the floor buttons
        button_box = tk.Frame(self.root)
        button_box.pack()

        # Create buttons for each valid floor
        for floor in self.valid_floors:
            floor_button = tk.Button(button_box, text="Floor " + floor,
                                     command=lambda f=floor: self.move_elevator(f))
            floor_button.pack(side=tk.LEFT, padx=10)

        # Create a button to request a specific floor
        request_button = tk.Button(button_box, text="Request Floor", command=self.request_floor_dialog)
        request_button.pack(side=tk.LEFT, padx=10)

    def move_elevator(self, target_floor):
        """Simulate moving the elevator to the target floor."""
        if not self.is_elevator_busy():
            # Update the current floor
            self.current_floor = target_floor
            # Show a dialog indicating the elevator has arrived
            self.show_info_dialog("Arrived at Floor " + self.current_floor)
            # Update the UI to reflect the new floor
            self.update_ui()
        else:
            # Show a dialog indicating the elevator is busy
            self.show_info_dialog("Elevator is busy. Please wait.")

    def update_ui(self):
        """Update the UI to reflect the current floor."""
        self.floor_label.config(text="Elevator is now at Floor " + self.current_floor)

    def is_elevator_busy(self):
        """Randomly determine if the elevator is busy."""
        return random.random() < 0.3  # 30% chance the elevator is busy

    def request_floor_dialog(self):
        """Prompt the user to enter a floor and move the elevator if valid."""
        selected_floor = self.show_input_dialog("Enter the floor you wish to go to:", self.current_floor)
        if self.is_valid_floor(selected_floor):
            self.move_elevator(selected_floor)
        else:
            self.show_info_dialog("Invalid floor. Please enter A, B, or C.")

    def is_valid_floor(self, floor):
        """Check if the entered floor is valid."""
        return floor and floor.upper() in self.valid_floors

    def show_input_dialog(self, prompt, default_text):
        """Show an input dialog."""
        return simpledialog.askstring("Input Dialog", prompt, initialvalue=default_text)

    def show_info_dialog(self, message):
        """Show an information dialog."""
        messagebox.showinfo("Information", message)

    def run(self):
        """Set the window size and start the Tkinter event loop."""
        self.root.geometry("300x150")
        self.root.mainloop()

if __name__ == "__main__":
    # Create an instance of the ElevatorSimulator class and run the application
    elevator_simulator = ElevatorSimulator()
    elevator_simulator.run()
