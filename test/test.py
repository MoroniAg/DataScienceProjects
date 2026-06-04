import torch
import pandas as pd
import numpy as np

print("Torch:", torch.__version__)
print("CUDA:", torch.cuda.is_available())

df = pd.DataFrame({
    "a": np.random.rand(5),
    "b": np.random.rand(5)
})

print(df)