# daily_activity_gui.py
import tkinter as tk
from tkinter import ttk, messagebox
from activity_tracker import ActivityTracker
from activity_visualization import visualize_activity, export_chart_as_image, get_time_insights

class DailyActivityGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Enhanced Daily Activity Tracker")

        self.activity_tracker = ActivityTracker()

        # Modern styling options
        style = ttk.Style()
        style.configure("TFrame", background="#f5f5f5")
        style.configure("TButton", background="#4CAF50", foreground="white")
        style.map("TButton", background=[("active", "#45a049")])

        # GUI components
        self.frame = ttk.Frame(root, padding=(20, 10))
        self.frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        self.activity_label = ttk.Label(self.frame, text="Activity:")
        self.activity_label.grid(row=0, column=0, padx=10, pady=10, sticky=tk.W)

        self.activity_entry = ttk.Entry(self.frame)
        self.activity_entry.grid(row=0, column=1, padx=10, pady=10, sticky=tk.W)

        self.category_label = ttk.Label(self.frame, text="Category:")
        self.category_label.grid(row=1, column=0, padx=10, pady=10, sticky=tk.W)

        self.category_entry = ttk.Entry(self.frame)
        self.category_entry.grid(row=1, column=1, padx=10, pady=10, sticky=tk.W)

        self.log_button = ttk.Button(self.frame, text="Log Activity", command=self.log_activity)
        self.log_button.grid(row=2, column=0, columnspan=2, pady=10)

        self.visualize_button = ttk.Button(self.frame, text="Visualize Activities", command=self.visualize_activities)
        self.visualize_button.grid(row=3, column=0, columnspan=2, pady=10)

        self.export_chart_button = ttk.Button(self.frame, text="Export Chart", command=self.export_chart)
        self.export_chart_button.grid(row=4, column=0, columnspan=2, pady=10)

        self.time_insights_button = ttk.Button(self.frame, text="Time Insights", command=self.get_time_insights)
        self.time_insights_button.grid(row=5, column=0, columnspan=2, pady=10)

    def log_activity(self):
        activity = self.activity_entry.get()
        category = self.category_entry.get()

        if activity and category:
            self.activity_tracker.log_activity(activity, category)
            messagebox.showinfo("Success", "Activity logged successfully!")
        else:
            messagebox.showerror("Error", "Please enter both activity and category.")

    def visualize_activities(self):
        chart_fig = visualize_activity(self.activity_tracker.activities)

    def export_chart(self):
        if hasattr(self, 'chart_fig'):
            export_chart_as_image(self.chart_fig)
        else:
            messagebox.showwarning("No Chart", "Please visualize activities first.")

    def get_time_insights(self):
        get_time_insights(self.activity_tracker.activities)

if __name__ == "__main__":
    root = tk.Tk()
    app = DailyActivityGUI(root)
    root.mainloop()
