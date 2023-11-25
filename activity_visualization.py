# activity_visualization.py
import tkinter as tk
from tkinter import ttk, filedialog
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import pandas as pd

def visualize_activity(activity_data):
    df = pd.DataFrame(activity_data)
    category_counts = df['category'].value_counts()

    # Create a figure and axis
    fig, ax = plt.subplots(figsize=(8, 5))
    category_counts.plot(kind='bar', color='skyblue', ax=ax)
    ax.set_title('Distribution of Activities by Category')
    ax.set_xlabel('Categories')
    ax.set_ylabel('Number of Activities')

    # Embed the plot in the Tkinter window
    canvas = FigureCanvasTkAgg(fig, master=tk.Toplevel())
    canvas_widget = canvas.get_tk_widget()
    canvas_widget.pack()

    # Display the plot
    canvas.draw()

    return fig  # Return the figure for further customization

def export_chart_as_image(fig):
    file_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")])
    if file_path:
        fig.savefig(file_path, bbox_inches='tight')
        tk.messagebox.showinfo("Export Successful", "Chart exported successfully!")

def get_time_insights(activity_data):
    df = pd.DataFrame(activity_data)
    df['timestamp'] = pd.to_datetime(df['timestamp'])
    df['hour'] = df['timestamp'].dt.hour

    hour_counts = df['hour'].value_counts().sort_index()

    # Create a new figure for time insights
    fig, ax = plt.subplots(figsize=(8, 5))
    hour_counts.plot(kind='bar', color='salmon', ax=ax)
    ax.set_title('Distribution of Activities by Hour of the Day')
    ax.set_xlabel('Hour of the Day')
    ax.set_ylabel('Number of Activities')

    # Embed the plot in the Tkinter window
    canvas = FigureCanvasTkAgg(fig, master=tk.Toplevel())
    canvas_widget = canvas.get_tk_widget()
    canvas_widget.pack()

    # Display the plot
    canvas.draw()

if __name__ == "__main__":
    # For testing the new features
    activity_data = [...]  # Add sample activity data
    chart_fig = visualize_activity(activity_data)
    export_chart_as_image(chart_fig)
    get_time_insights(activity_data)
