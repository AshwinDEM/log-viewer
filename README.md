# Log Viewer
In windows, if you create a new text file and write .LOG in the first line of the file, it becomes a log file.
This project aims to create a way to easily view and understand log files.

Basic structure of a windows log file
```
.LOG 
HH:MM DD-MM-YYYY <Log Entry> 
HH:MM DD-MM-YYYY <Log Entry>
```

The aim is to create a project that can view log files in a manner that is easy for people, and maybe also manipulate the log entries.

## Setup Instructions

### Prerequisites

- Python 3.x
- pip (Python package installer)

### Installation

1. **Clone the repository**:
    ```sh
    git clone https://github.com/AshwinDEM/log-viewer.git
    cd log-viewer
    ```

2. **Create a virtual environment**:
    ```sh
    python -m venv venv
    ```

3. **Activate the virtual environment**:
    - On Windows:
        ```sh
        venv\Scripts\activate
        ```
    - On macOS/Linux:
        ```sh
        source venv/bin/activate
        ```

4. **Install the required packages**:
    ```sh
    pip install -r requirements.txt
    ```

### Running the Application

1. **Start the Flask application**:
    ```sh
    python app.py
    ```

2. **Open your web browser and navigate to**:
    ```
    http://127.0.0.1:5000/
    ```

### Running Tests

1. **Run the tests using pytest**:
    ```sh
    pytest
    ```

### Deactivating the Virtual Environment

- When you are done, you can deactivate the virtual environment:
    ```sh
    deactivate
    ```

### Cleaning Up

- To remove the virtual environment, simply delete the [`venv`] directory:
    ```sh
    rm -rf venv
    ```

Now you should be able to set up and run the Log Viewer application on your local machine.