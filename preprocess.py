import os
import librosa
import soundfile as sf
import numpy as np

# Set folder paths for datasets
DATASET_DIR = "datasets"
CLEAN_DIR = os.path.join(DATASET_DIR, "clean_speech")

# List of military-grade noise folders
NOISE_FOLDERS = ["guns", "helicopter", "tanks", "explosion", "bomb_blast", "MAD"]

# Target sample rate and duration for uniform processing
SAMPLE_RATE = 16000
DURATION = 3  # Target length for each audio clip (in seconds)
MAX_LEN = SAMPLE_RATE * DURATION

def load_and_preprocess_audio(file_path):
    """Loads audio, normalizes sample rate, and ensures uniform length."""
    try:
        # Load audio and convert to target 16kHz sample rate
        audio, sr = librosa.load(file_path, sr=SAMPLE_RATE)
        
        # Pad with zeros if too short, or truncate if too long
        if len(audio) < MAX_LEN:
            audio = np.pad(audio, (0, MAX_LEN - len(audio)), 'constant')
        else:
            audio = audio[:MAX_LEN]
            
        return audio
    except Exception as e:
        print(f"[ERROR] Failed to load {file_path}: {e}")
        return None

def verify_datasets():
    """Verifies the existence of clean speech and noise directories."""
    print("[STATUS] Verifying dataset integrity...")
    
    # Check for clean speech audio files
    if os.path.exists(CLEAN_DIR):
        clean_files = [f for f in os.listdir(CLEAN_DIR) if f.endswith('.wav')]
        print(f"[INFO] Clean Speech files found: {len(clean_files)}")
    else:
        print("[WARNING] Clean Speech directory not found!")

    # Check for tactical noise audio files
    for noise_folder in NOISE_FOLDERS:
        folder_path = os.path.join(DATASET_DIR, noise_folder)
        if os.path.exists(folder_path):
            noise_files = [f for f in os.listdir(folder_path) if f.endswith(('.wav', '.mp3'))]
            print(f"[INFO] Tactical Noise folder '{noise_folder}' verified: {len(noise_files)} files")
        else:
            print(f"[WARNING] Tactical Noise folder '{noise_folder}' not found!")

if __name__ == "__main__":
    verify_datasets()
    print("[SUCCESS] Data Pre-processing setup is ready for model training.")