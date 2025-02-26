# LogicLens-AI-powered-insights-into-RTL-logic-complexity.
## Project Overview
**LogicDepthAI** is an **AI-driven solution** designed for **VLSI engineers** to predict the **combinational logic depth** of signals in RTL designs **before synthesis**. Traditional synthesis-based timing analysis is **time-consuming**, but our **Graph Neural Network (GNN) + traditional ML hybrid model** enables **fast and accurate** depth estimation. This helps in **early detection of timing violations**, optimizing the design process, and reducing iteration time.

**Key Features:**
- **Uses Graph Neural Networks (GNNs)** to model RTL circuit structure.
- **Extracts key RTL features** (fan-in, fan-out, gate types, etc.).
- **Predicts combinational logic depth** without full synthesis.
- **Faster than traditional STA tools** like Synopsys Design Compiler.

---

## Installation Instructions

### 1️ Clone the Repository
```bash
git clone https://github.com/your-username/LogicDepthAI.git
cd LogicDepthAI
```

### 2 Create a Virtual Environment (Recommended for Python users)
```bash
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate  # Windows
```

### 3️ Install Dependencies
```bash
pip install -r requirements.txt
```

---

##  How to Run the Code

1. **Prepare RTL Input Files**
   - Place RTL files (Verilog/VHDL) in the `data/` directory.
   - Ensure feature extraction is performed using an EDA tool like **Yosys**.

2. **Run the Prediction Script**
```bash
python src/predict_logic_depth.py --input data/sample_rtl.v
```

3. **View Results**
   - The output will display **predicted combinational logic depth** for critical signals.
   - Results are stored in `results/logic_depth_predictions.json`.

---

## How to Train the Model

1. **Prepare Training Data**
   - Use a dataset of RTL circuits with **labeled combinational depths** from synthesis reports.
   - Store in `data/training_dataset.csv`.

2. **Run Training Script**
```bash
python src/train_model.py --dataset data/training_dataset.csv
```

3. **Save the Model**
   - The trained model will be saved in `models/gnn_ml_model.pth`.

---

## Dataset Description

The dataset consists of **RTL netlists and extracted features**, including:
- **Fan-in/Fan-out of signals**  
- **Number of logic gates in the path**  
- **Signal dependencies (modeled as a graph)**  
- **Actual logic depth from synthesis reports**  

**Sources**:
- Generated from open-source RTL designs.
- Extracted using Yosys/OpenSTA.

---

## Future Work
- Improve **model accuracy** using advanced GNN architectures.
- Integrate with **real-time EDA tools** for automated analysis.
- Optimize **runtime performance** for large circuits.

🔗 **GitHub Repository**: [https://github.com/your-username/LogicDepthAI](https://github.com/your-username/LogicDepthAI)
