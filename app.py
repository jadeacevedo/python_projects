import tkinter as tk
from tkinter import messagebox

class PatientTrackerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Patient Tracker")
        self.root.geometry("600x400")

        # List to store patient details
        self.patients = []

        # Create UI components
        self.create_widgets()

    def create_widgets(self):
        # Input fields
        tk.Label(self.root, text="Name:").grid(row=0, column=0, padx=10, pady=10)
        self.name_entry = tk.Entry(self.root)
        self.name_entry.grid(row=0, column=1, padx=10, pady=10)

        tk.Label(self.root, text="Age:").grid(row=1, column=0, padx=10, pady=10)
        self.age_entry = tk.Entry(self.root)
        self.age_entry.grid(row=1, column=1, padx=10, pady=10)

        tk.Label(self.root, text="Condition:").grid(row=2, column=0, padx=10, pady=10)
        self.condition_entry = tk.Entry(self.root)
        self.condition_entry.grid(row=2, column=1, padx=10, pady=10)

        # Buttons
        self.add_button = tk.Button(self.root, text="Add Patient", command=self.add_patient)
        self.add_button.grid(row=3, column=0, columnspan=2, pady=10)

        self.delete_button = tk.Button(self.root, text="Delete Selected", command=self.delete_patient)
        self.delete_button.grid(row=4, column=0, columnspan=2, pady=10)

        # Patient list
        self.patient_listbox = tk.Listbox(self.root, width=50, height=15)
        self.patient_listbox.grid(row=0, column=2, rowspan=5, padx=10, pady=10)

    def add_patient(self):
        # Get input values
        name = self.name_entry.get().strip()
        age = self.age_entry.get().strip()
        condition = self.condition_entry.get().strip()

        # Validate input
        if not name or not age or not condition:
            messagebox.showerror("Input Error", "All fields are required.")
            return

        if not age.isdigit():
            messagebox.showerror("Input Error", "Age must be a number.")
            return

        # Add patient to the list
        patient = f"{name} (Age: {age}, Condition: {condition})"
        self.patients.append(patient)
        self.update_patient_list()

        # Clear input fields
        self.name_entry.delete(0, tk.END)
        self.age_entry.delete(0, tk.END)
        self.condition_entry.delete(0, tk.END)

    def delete_patient(self):
        # Get selected patient
        selected_index = self.patient_listbox.curselection()
        if not selected_index:
            messagebox.showerror("Selection Error", "No patient selected.")
            return

        # Remove from the list
        del self.patients[selected_index[0]]
        self.update_patient_list()

    def update_patient_list(self):
        # Refresh the listbox
        self.patient_listbox.delete(0, tk.END)
        for patient in self.patients:
            self.patient_listbox.insert(tk.END, patient)

# Run the app
if __name__ == "__main__":
    root = tk.Tk()
    app = PatientTrackerApp(root)
    root.mainloop()
