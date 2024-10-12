# OCR_ML
Medicine Alternative Suggester

Features:

- Text Processing: Utilizes LabelEncoder to convert categorical medicine names into numerical values
- Machine Learning: Employs K-Nearest Neighbors (KNN) algorithm to find similar medicines based on their compositions
- Image Processing: Allows users to input medicine names through images, employing Optical Character Recognition (OCR) to extract text

Working:

- Installs and imports necessary libraries such as pytesseract, pandas, cv2 (OpenCV), and sklearn (Scikit-learn)
- Reads medication data from a CSV file named "meds.csv" using Pandas
- Concatenates relevant columns from the dataset to create all_data
- Encodes categorical data using LabelEncoder from Scikit-learn
- Splits the data into features (X) and target labels (y)
- Initializes a K-Nearest Neighbors (KNN) classifier with k=5 and fits the classifier with the features (X) and target labels (y)
- Prompts the user to choose between providing the medicine name as text input or through an image
- If the user chooses image input, it reads the image using OpenCV and performs Optical Character Recognition (OCR) using Tesseract to extract the text
- For each medicine input by the user, it attempts to find alternate medicines by querying the trained KNN classifier
- Decodes the predicted labels back to medicine names using inverse transformation and appends the predicted alternate medicines to a list
- Prints the alternate medicines for each input medicine
  
Purpose:

This tool aims to facilitate decision-making for healthcare professionals and individuals by offering convenient access to data-driven alternative medicine suggestions, ultimately enhancing accessibility and promoting informed healthcare choices.
