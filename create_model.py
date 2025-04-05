import pickle

# Example: Create a dummy model (replace this with your actual model)
dummy_model = {"example": "This is a placeholder model"}

# Save the model to a file
with open("titanic_model.pkl", "wb") as f:
    pickle.dump(dummy_model, f)

print("Dummy model 'titanic_model.pkl' created successfully.")
