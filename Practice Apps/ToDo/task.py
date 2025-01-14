class Task:
    def __init__(self, t_id: int, description: str, state: str = "Incomplete"):
        self.t_id = t_id
        self.description = description
        self.state = state
    
    def change_description(self, new_description: str):
        self.description = new_description
    
    def change_state(self, new_state: str):
        self.state = new_state

    def __repr__(self):
        return f"ID: {self.t_id}, DESC: {self.description}, STATE: {self.state}"
    
