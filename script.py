import toml
import sys


def parse_toml(file_path):
    try:
        with open(file_path, 'r') as f:
            return toml.load(f)
    except Exception as e:
        print(f"Error reading TOML file: {e}")
        sys.exit(1)


def convert_to_custom_language(data):
    output_lines = []

    for key, value in data.items():
        if isinstance(value, dict):
            output_lines.append(f"(def {key} {{")
            for sub_key, sub_value in value.items():
                output_lines.append(f"  {sub_key} : {sub_value},")
            output_lines.append("})")
        else:
            output_lines.append(f"(def {key} {value})")

    return "\n".join(output_lines)


def main():
    if len(sys.argv) != 2:
        print("Usage: python script.py <path_to_toml_file>")
        sys.exit(1)

    file_path = sys.argv[1]
    toml_data = parse_toml(file_path)
    transformed_output = convert_to_custom_language(toml_data)
    print(transformed_output)


if __name__ == "__main__":
    main()
