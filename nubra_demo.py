from nubra_python_sdk.start_sdk import InitNubraSdk, NubraEnv

# Demonstrates SDK usage (required by guidelines)
sdk = InitNubraSdk(
    env=NubraEnv.UAT,
    env_creds=True
)

print("Nubra SDK initialized successfully")

# Example: list available modules
print(dir(sdk))

# nubra_marketdata_example.py
from nubra_python_sdk.marketdata import ticker

print(dir(ticker))
