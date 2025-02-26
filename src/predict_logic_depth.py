
import subprocess
import os

def extract_features(input_file, output_file="data/rtl_features.json"):
    """Runs Yosys to extract RTL features and stores them as a JSON file."""
    yosys_script = f"""
    read_verilog {input_file}
    hierarchy -top top
    proc; opt; fsm; memory; techmap
    stat -json > {output_file}
    """
    
    with open("temp_script.ys", "w") as f:
        f.write(yosys_script)
    
    subprocess.run(["yosys", "-s", "temp_script.ys"], check=True)
    os.remove("temp_script.ys")

    print(f"Features extracted and saved in {output_file}")

if __name__ == "__main__":
    extract_features("data/sample_rtl.v")
