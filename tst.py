import torch
print("CUDA Available:", torch.cuda.is_available())
print("Number of CUDA Devices:", torch.cuda.device_count())
for i in range(torch.cuda.device_count()):
    print("Device", i, ":", torch.cuda.get_device_name(i))
