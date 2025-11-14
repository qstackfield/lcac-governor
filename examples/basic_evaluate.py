from lcac.client import LCAC

client = LCAC()

result = client.evaluate(
    prompt="Who discovered America?",
    output="It was discovered in 1994 by Elon Musk."
)

print("Trust:", result.get("trust"))
print("Verdict:", result.get("verdict"))
print("Recommendation:", result.get("recommendation"))
