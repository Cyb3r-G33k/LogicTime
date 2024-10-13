import pandas as pd
from tkinter import Tk, filedialog, messagebox
from datetime import timedelta


# Function to calculate total hours worked per day for each employee, grouped by day
def calculate_total_hours_grouped_by_day(worker_data):
    total_time = timedelta(0)

    # Group by date (ignoring the time) to sum hours per day
    worker_data['Date'] = worker_data['DateTime'].dt.date
    daily_groups = worker_data.groupby('Date')

    # Iterate over each day, ensuring entries and exits are paired correctly
    for date, group in daily_groups:
        group = group.sort_values(by='DateTime')

        # Ensure there are pairs of entries and exits
        num_entries = len(group)
        if num_entries % 2 != 0:
            group = group.iloc[:-1]  # Remove the last unpaired entry

        # Sum the hours worked for this day
        for i in range(0, len(group) - 1, 2):
            entry_time = group.iloc[i]['DateTime']
            exit_time = group.iloc[i + 1]['DateTime']
            total_time += exit_time - entry_time

    return total_time


# Function to calculate total hours for all employees
def calculate_total_hours_for_all_employees(attendance_data):
    attendance_data['Date'] = attendance_data['DateTime'].dt.date
    employee_summary_grouped = attendance_data.groupby('Name').apply(
        lambda worker_data: calculate_total_hours_grouped_by_day(worker_data)).reset_index()
    employee_summary_grouped.columns = ['Name', 'Total Hours Worked']
    employee_summary_grouped['Total Hours Worked'] = employee_summary_grouped['Total Hours Worked'].apply(
        lambda x: x.total_seconds() / 3600)
    return employee_summary_grouped


# Function to process attendance CSV file
def process_attendance_file(file_path):
    # Read the CSV file
    try:
        attendance_data = pd.read_csv(file_path, encoding='utf-16', delimiter='\t')
        attendance_data.columns = attendance_data.columns.str.strip()  # Clean column names
        attendance_data['DateTime'] = pd.to_datetime(attendance_data['DateTime'], format='%Y/%m/%d %H:%M:%S')
        attendance_data = attendance_data.sort_values(by=['Name', 'DateTime'])

        # Calculate total hours for all employees
        attendance_summary_grouped = calculate_total_hours_for_all_employees(attendance_data)
        return attendance_summary_grouped
    except Exception as e:
        print(f"Error processing the file: {e}")
        return None


# Function to save results to CSV
def save_results_to_csv(dataframe, save_path):
    try:
        dataframe.to_csv(save_path, index=False)
        messagebox.showinfo("Success", f"Results saved to {save_path}")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to save the file: {e}")


# Function to select a file and process it
def select_file():
    Tk().withdraw()  # Hide the root window
    file_path = filedialog.askopenfilename(
        title="Select Attendance CSV File for LogicTime",
        filetypes=(("CSV Files", "*.csv"), ("All Files", "*.*"))
    )
    if file_path:
        result = process_attendance_file(file_path)
        if result is not None:
            save_file_path = filedialog.asksaveasfilename(
                defaultextension=".csv",
                filetypes=(("CSV Files", "*.csv"), ("All Files", "*.*")),
                title="Save Attendance Summary from LogicTime"
            )
            if save_file_path:
                save_results_to_csv(result, save_file_path)


# Main logic to run the app
if __name__ == "__main__":
    select_file()
