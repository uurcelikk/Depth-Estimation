import argparse

from predictor import DepthEstimationModel

def main():
    parser = argparse.ArgumentParser(description="Depth Estimation")
    parser.add_argument("image_path", help="Path to the input image")
    parser.add_argument("output_path", help="Path to the output image")
    args = parser.parse_args()

    model = DepthEstimationModel()
    result = model.calculate_depthmap(args.image_path, args.output_path)
    print(result)

if __name__ == "__main__":
    main()