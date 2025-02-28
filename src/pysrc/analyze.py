import numpy as np


def read_from_file(name: str) -> np.ndarray:
    with open(name, "r") as file:
        next(file)
        z: list[float] = []
        for line in file.readlines():
            z.append(float(line.strip()))
        return np.array(z)


def main() -> None:
    predictions: np.ndarray = read_from_file("src/pysrc/predictions.txt")
    targets: np.ndarray = read_from_file("src/pysrc/targets.txt")
    assert len(predictions) == len(targets)
    correlation = np.corrcoef(predictions, targets)[0, 1]
    print("\nCorrelation = " + str(correlation) + "\n")


# Correlation = 0.11231864302989218

if __name__ == "__main__":
    main()
