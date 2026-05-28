class Patient:
    def __init__(self, patientID, name, age, department, urgency, status="Waiting"):
        # Validate that patientID is an integer
        if not isinstance(patientID, int):
            raise ValueError("Invalid ID")
        
        # Validate urgency level (must be between 1 and 5)
        if urgency < 1 or urgency > 5:
            raise ValueError("Urgency must be 1-5")
        
        # Assign patient attributes
        self.patientID = patientID      # Unique identifier for the patient
        self.name = name                # Patient's name
        self.age = age                  # Patient's age
        self.department = department    # Assigned hospital department
        self.urgency = urgency          # Urgency level (1 = most critical, 5 = least)
        self.status = status            # Current status (default = "Waiting")

    def __str__(self):
        # Return a formatted string representation of the patient object
        return f"{self.patientID} | {self.name} | {self.department} | U:{self.urgency} | {self.status}"