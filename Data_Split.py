import os
import random
import shutil

# Define paths
image_folder = "./agri_data/data"
output_folder = "./dataset"

# Create output directories
os.makedirs(os.path.join(output_folder, "images"), exist_ok=True)
os.makedirs(os.path.join(output_folder, "labels"), exist_ok=True)

# Get list of image files
image_files = [f for f in os.listdir(image_folder) if f.endswith(".jpg") or f.endswith(".jpeg")]

# Copy images and labels to output directory
for image_file in image_files:
    # Copy image
    shutil.copy(os.path.join(image_folder, image_file), os.path.join(output_folder, "images", image_file))
    
    # Get corresponding label file
    label_file = os.path.splitext(image_file)[0] + ".txt"
    
    # Check if label file exists
    if os.path.exists(os.path.join(image_folder, label_file)):
        # Copy label file
        shutil.copy(os.path.join(image_folder, label_file), os.path.join(output_folder, "labels", label_file))
    else:
        print(f"Label file not found for {image_file}")

print("Data preparation completed.")

def split_dataset(image_dir, label_dir=None, train_ratio=0.7, val_ratio=0.15, test_ratio=0.15, seed=None):
    """
    Splits an image and label txt file dataset into train, validation, and test sets with separate image and label subdirectories.

    Args:
        image_dir (str): Path to the directory containing image files.
        label_dir (str, optional): Path to the directory containing label txt files. (Defaults to None, assumes labels in image_dir)
        train_ratio (float, optional): Proportion of data for the training set. Defaults to 0.7.
        val_ratio (float, optional): Proportion of data for the validation set. Defaults to 0.15.
        test_ratio (float, optional): Proportion of data for the test set. Defaults to 0.15.
        seed (int, optional): Random seed for reproducibility. Defaults to None.

    Returns:
        None: Creates new directories for train, validation, and test sets with corresponding images and label txt files in subdirectories.
    """

    # Validate input ratios
    if train_ratio + val_ratio + test_ratio != 1:
        raise ValueError("Total ratios must add up to 1.0 (train + val + test).")

    # Define valid image extensions
    valid_image_extensions = ('.jpg', '.jpeg', '.png', '.bmp', '.tiff', '.gif')

    # List all files in the directory for debugging
    all_files = os.listdir(image_dir)
    print(f"All files in the directory: {all_files}")

    # Get image and label file paths
    image_paths = [os.path.join(image_dir, f) for f in all_files if os.path.isfile(os.path.join(image_dir, f)) and f.lower().endswith(valid_image_extensions)]
    if not label_dir:
        label_dir = image_dir  # Use image directory if label_dir is not provided
    label_paths = [os.path.join(label_dir, f.replace(os.path.splitext(f)[1], ".txt")) for f in all_files if os.path.isfile(os.path.join(image_dir, f)) and f.lower().endswith(valid_image_extensions)]

    # Debugging statements to check paths
    print(f"Found {len(image_paths)} image files: {image_paths}")
    print(f"Found {len(label_paths)} label files: {label_paths}")

    # Ensure same number of images and label files
    if len(image_paths) != len(label_paths):
        raise ValueError("Number of image files and label txt files must match.")

    # Shuffle paths for randomness (optional seed for reproducibility)
    if seed is not None:
        random.seed(seed)
    
    combined = list(zip(image_paths, label_paths))

    # Debugging statement to check combined list
    print(f"Combined list length: {len(combined)}")

    random.shuffle(combined)
    
    if combined:
        image_paths, label_paths = zip(*combined)
    else:
        image_paths, label_paths = [], []

    # Debugging statements to check shuffled paths
    print(f"Shuffled image paths: {image_paths}")
    print(f"Shuffled label paths: {label_paths}")

    # Calculate split indices based on ratios
    total_len = len(image_paths)
    train_len = int(total_len * train_ratio)
    val_len = int(total_len * val_ratio)
    test_len = total_len - train_len - val_len

    # Create train, validation, and test directories with subdirectories for images and labels
    train_dir = os.path.join("./Train_Split_Valid_Datasets/", "train")
    val_dir = os.path.join("./Train_Split_Valid_Datasets/", "val")
    test_dir = os.path.join("./Train_Split_Valid_Datasets/", "test")

    os.makedirs(os.path.join(train_dir, "images"), exist_ok=True)
    os.makedirs(os.path.join(train_dir, "labels"), exist_ok=True)
    os.makedirs(os.path.join(val_dir, "images"), exist_ok=True)
    os.makedirs(os.path.join(val_dir, "labels"), exist_ok=True)
    os.makedirs(os.path.join(test_dir, "images"), exist_ok=True)
    os.makedirs(os.path.join(test_dir, "labels"), exist_ok=True)

    # Split data into sets
    for i in range(train_len):
        os.rename(image_paths[i], os.path.join(train_dir, "images", os.path.basename(image_paths[i])))
        os.rename(label_paths[i], os.path.join(train_dir, "labels", os.path.basename(label_paths[i])))

    for i in range(train_len, train_len + val_len):
        os.rename(image_paths[i], os.path.join(val_dir, "images", os.path.basename(image_paths[i])))
        os.rename(label_paths[i], os.path.join(val_dir, "labels", os.path.basename(label_paths[i])))

    for i in range(train_len + val_len, total_len):
        os.rename(image_paths[i], os.path.join(test_dir, "images", os.path.basename(image_paths[i])))
        os.rename(label_paths[i], os.path.join(test_dir, "labels", os.path.basename(label_paths[i])))
    print(f"Dataset split successfully: Train: {train_len}, Validation: {val_len}, Test: {test_len}")

# Example usage
image_dir = "./dataset/images"  # Replace with your image directory
label_dir = "./dataset/labels"
split_dataset(image_dir, label_dir, train_ratio=0.7, val_ratio=0.15, test_ratio=0.15, seed=None)