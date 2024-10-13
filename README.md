
# LogicTime  
*Created by Alex Losev*

---

## Introduction

**LogicTime** is a Python-based attendance management software that processes raw attendance data from CSV files exported by attendance machines. It analyzes employee work hours, calculates total hours, and generates a new CSV file with detailed reports. This tool simplifies attendance tracking by automating the calculation of work hours and providing an easy way to generate reports for further analysis.

---

## Features

- **CSV File Processing:** Import raw data from attendance machines in CSV format.
- **Time Calculation:** Automatically calculate total work hours for each employee.
- **Report Generation:** Create CSV reports with calculated work hours.

---

## Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/Cyb3r-G33k/LogicTime
   cd LogicTime
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**
   ```bash
   python main.py
   ```

---

## Usage

1. **Launch the application:**  
   Run `main.py` to open the GUI.

2. **Select Attendance File:**  
   Use the interface to select the raw attendance CSV file exported from the attendance machine.

3. **Process the Data:**  
   Click **Process** to calculate total hours worked for each employee.

4. **Generate Report:**  
   Save the calculated results as a new CSV file by clicking the **Export Report** button.

---

## Configuration

1. **Settings File:**  
   A `config.ini` file is generated on the first run. Use it to:
   - Set the working hours and overtime rules.
   - Configure report output formats and directories.

2. **Adjust Work Rules:**  
   Modify attendance rules directly through the settings panel or by editing the `config.ini` file.

---

## Logs and Reports

- **Logs:**  
  Any issues or processing steps are logged and saved in the `/logs` directory.

- **Reports:**  
  Generated reports are saved as new CSV files in the `/reports` folder.

---

## Development Roadmap

- [x] CSV file import and processing  
- [x] Calculation of total work hours  
- [x] Report generation in CSV format  
- [ ] Add support for multiple attendance formats  
- [ ] Integration with payroll systems  
- [ ] Add visual analytics and dashboards  

---

## Contributing

We welcome contributions from the community! Follow these steps to contribute:

1. Fork the repository.  
2. Create a new branch:
   ```bash
   git checkout -b feature-branch
   ```
3. Commit your changes:
   ```bash
   git commit -m "Added new feature"
   ```
4. Push to the branch:
   ```bash
   git push origin feature-branch
   ```
5. Create a pull request.

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
