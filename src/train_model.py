import torch
import torch.nn as nn
import torch.optim as optim
import pandas as pd
from models.model import LogicDepthModel  # Assuming model definition

def load_data(csv_path="data/training_dataset.csv"):
    """Loads training dataset from CSV."""
    df = pd.read_csv(csv_path)
    X = torch.tensor(df.drop(columns=["logic_depth"]).values).float()
    y = torch.tensor(df["logic_depth"].values).float().unsqueeze(1)
    return X, y

def train_model():
    """Trains the GNN + ML hybrid model."""
    X, y = load_data()

    model = LogicDepthModel()
    criterion = nn.MSELoss()
    optimizer = optim.Adam(model.parameters(), lr=0.001)

    epochs = 100
    for epoch in range(epochs):
        optimizer.zero_grad()
        predictions = model(X)
        loss = criterion(predictions, y)
        loss.backward()
        optimizer.step()

        if (epoch + 1) % 10 == 0:
            print(f"Epoch [{epoch+1}/{epochs}], Loss: {loss.item():.4f}")

    torch.save(model.state_dict(), "models/gnn_ml_model.pth")
    print("Model training complete! Saved to models/gnn_ml_model.pth")

if __name__ == "__main__":
    train_model()

