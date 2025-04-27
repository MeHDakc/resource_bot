from app.resource_finder import find_and_gather_resource

if __name__ == "__main__":
    preferred_resources = ["gold", "wood", "stone", "food"]
    result = find_and_gather_resource(preferred_resources)
    if result:
        print(f"Resource found at {result}")
    else:
        print("No resources found.")
