import torch
import json
import os
from models.model import LogicDepthModel  # Assuming model is in models/

def load_model(model_path="models/gnn_ml_model.pth"):
    """Loads the trained GNN + ML model."""
    model = LogicDepthModel()
    model.load_state_dict(torch.load(model_path))
    model.eval()
    return model

def predict_logic_depth(input_file, model):
    """Predicts the combinational logic depth using the trained model."""
    with open(input_file, "r") as f:
        features = json.load(f)  # Load extracted features

    # Convert features to model input (this depends on training setup)
    model_input = torch.tensor([features[key] for key in sorted(features.keys())]).float()
    
    with torch.no_grad():
        prediction = model(model_input)

    return prediction.item()

if __name__ == "__main__":
    input_file = "data/rtl_features.json"
    output_file = "results/logic_depth_predictions.json"

    if not os.path.exists(input_file):
        print("Feature extraction missing! Run extract_features.py first.")
        exit()

    model = load_model()
    prediction = predict_logic_depth(input_file, model)

    with open(output_file, "w") as f:
        json.dump({"predicted_logic_depth": prediction}, f, indent=4)

    print(f"Prediction saved in {output_file}")

