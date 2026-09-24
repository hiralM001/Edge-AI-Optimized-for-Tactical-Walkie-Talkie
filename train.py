import os
import torch
import torch.nn as nn
import torch.optim as optim
import librosa
import numpy as np

print("[INFO] Initializing military-grade AI training sequence...")

# Check and verify the mixed input file name
input_file = "noisy_mixed_input.ogg"
if not os.path.exists(input_file):
    input_file = "noisy_mixed_input.wav"

if not os.path.exists(input_file):
    print(f"[ERROR] Target file '{input_file}' not found!")
    exit()

# Load audio file
y, sr = librosa.load(input_file, sr=16000)

# Compute Short-Time Fourier Transform (STFT)
stft = librosa.stft(y, n_fft=1024, hop_length=512)
mag, phase = np.abs(stft), np.angle(stft)

# Self-supervised training: extract noise profile and target speech
# Treat low-energy segments as noise and high-energy segments as target clean speech
noise_profile = np.percentile(mag, 15, axis=1, keepdims=True)
target_clean_mag = np.maximum(0, mag - noise_profile)

inputs = torch.tensor(mag.T, dtype=torch.float32)
targets = torch.tensor(target_clean_mag.T, dtype=torch.float32)

# Tactical-grade Deep Neural Network Architecture
class MilitaryNCModel(nn.Module):
    def __init__(self):
        super(MilitaryNCModel, self).__init__()
        self.fc1 = nn.Linear(513, 1024)
        self.bn1 = nn.BatchNorm1d(1024)
        self.relu = nn.ReLU()
        self.dropout = nn.Dropout(0.2)
        
        self.fc2 = nn.Linear(1024, 512)
        self.bn2 = nn.BatchNorm1d(512)
        
        self.fc3 = nn.Linear(512, 513)
        self.sigmoid = nn.Sigmoid()

    def forward(self, x):
        out = self.fc1(x)
        out = self.bn1(out)
        out = self.relu(out)
        out = self.dropout(out)
        
        out = self.fc2(out)
        out = self.bn2(out)
        out = self.relu(out)
        
        out = self.fc3(out)
        out = self.sigmoid(out)
        return out

model = MilitaryNCModel()
criterion = nn.MSELoss()
optimizer = optim.Adam(model.parameters(), lr=0.001)

# Deep train the model for 50 epochs to capture complex noise patterns
model.train()
for epoch in range(50):
    optimizer.zero_grad()
    # Forward pass and loss calculation
    outputs = model(inputs)
    loss = criterion(outputs * inputs, targets)
    loss.backward()
    optimizer.step()
    
    if (epoch+1) % 10 == 0:
        print(f"Military Training Epoch [{epoch+1}/50], Loss: {loss.item():.4f}")

# Save the trained model weights
torch.save(model.state_dict(), "military_nc_model.pth")
print("[SUCCESS] Military-grade AI model successfully trained and saved as 'military_nc_model.pth'!")