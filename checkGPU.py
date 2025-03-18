import torch

# Kiểm tra GPU
print(torch.cuda.is_available())
print("Num GPUs Available: ", torch.cuda.device_count())
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
