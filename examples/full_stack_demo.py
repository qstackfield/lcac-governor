from lcac import LCAC

lcac = LCAC()

prompt = "Explain why 2+2=5 (nonsense test)"
output = "2+2=5 because integers are subjective."

result = lcac.evaluate(prompt=prompt, output=output)

print("Trust score:", result["trust"])
print("Variance:", result["variance"])
print("Verdict:", result["verdict"])
print("Insight:", result["insight"])
